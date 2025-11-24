<script setup lang="ts">
import { ref, provide, useSlots, watch, computed, onMounted } from 'vue'
import { useI18n, SUPPORTED_LOCALES } from '~/composables/useI18n'
import { useQuizTracking } from '~/composables/useQuizTracking'
import { useRoute } from 'vue-router'

const { t } = useI18n()
const route = useRoute()
const slots = useSlots()
const { recordQuizCompletion, getQuizStats } = useQuizTracking()
const selectedOption = ref<string | null>(null)
const correctAnswer = ref<string | null>(null)
const isAnswered = ref(false)
const completionCount = ref<number | null>(null)
const isLoadingStats = ref(false)

const props = defineProps<{
  correct?: string
}>()

if (props.correct) {
  correctAnswer.value = props.correct
}

/**
 * Normalize path to English version by removing language prefix
 * This ensures all language versions of the same page share the same quiz data
 */
function normalizePathToEnglish(path: string): string {
  const segments = path.split('/').filter(Boolean)
  if (segments.length > 0 && SUPPORTED_LOCALES.includes(segments[0] as typeof SUPPORTED_LOCALES[number])) {
    segments.shift()
    return segments.length > 0 ? '/' + segments.join('/') : '/'
  }
  return path
}

// Generate stable quiz ID based on page path and correct answer
// Uses normalized English path to ensure all language versions share the same quiz data
const quizId = computed(() => {
  const pagePath = normalizePathToEnglish(route.path)
  // Use props.correct as primary identifier, fallback to correctAnswer if not available
  const correct = props.correct || correctAnswer.value || 'default'
  // Generate stable hash from page path and correct answer
  const hash = `${pagePath}:${correct}`
  // Simple hash function
  let hashValue = 0
  for (let i = 0; i < hash.length; i++) {
    const char = hash.charCodeAt(i)
    hashValue = (hashValue << 5) - hashValue + char
    hashValue = hashValue & hashValue
  }
  return `quiz-${Math.abs(hashValue).toString(36)}`
})

provide('quizState', {
  selectedOption,
  correctAnswer,
  isAnswered,
  selectOption: (value: string) => {
    if (!isAnswered.value) {
      selectedOption.value = value
      isAnswered.value = true
    }
  },
  setCorrectAnswer: (value: string) => {
    correctAnswer.value = value
  },
})

// Watch quiz completion status and record completion count
watch(isAnswered, async (newValue) => {
  if (newValue && quizId.value) {
    const newCount = await recordQuizCompletion(quizId.value)
    // Update count directly from response to avoid extra API call
    if (newCount !== null) {
      completionCount.value = newCount
    } else {
      // Fallback to loading stats if recording didn't return count
      await loadStats()
    }
  }
})

// Load quiz completion stats
const loadStats = async () => {
  if (!quizId.value) return

  isLoadingStats.value = true
  try {
    const count = await getQuizStats(quizId.value)
    if (count !== null) {
      completionCount.value = count
    }
  } catch (error) {
    console.error('Error loading quiz stats:', error)
  } finally {
    isLoadingStats.value = false
  }
}

// Load stats on mount
onMounted(() => {
  loadStats()
})

// Reload stats when quizId changes (e.g., route change)
watch(quizId, () => {
  completionCount.value = null
  loadStats()
})

const hasQuestionSlot = !!slots.question

// Format completion count text
const completionText = computed(() => {
  if (completionCount.value === null) return ''
  const count = completionCount.value
  return count === 1
    ? `1 ${t('quiz.completion')}`
    : `${count.toLocaleString()} ${t('quiz.completions')}`
})
</script>

<template>
  <div
    class="mb-6 rounded-lg border-2 border-primary-200 bg-gradient-to-br from-primary-50/50 to-white p-6 dark:border-primary-800 dark:from-primary-950/30 dark:to-slate-800/50 relative"
  >
    <div class="absolute -top-3 left-4 flex items-center gap-2">
      <div
        class="px-3 py-1 rounded-full bg-primary-500 text-white text-xs font-semibold uppercase tracking-wide shadow-md dark:bg-primary-600"
      >
        {{ t('quiz.label') }}
      </div>
      <div
        v-if="completionCount !== null"
        class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-medium shadow-sm dark:bg-slate-700 dark:text-slate-300 flex items-center gap-1.5"
        :title="t('quiz.totalCompletions')"
      >
        <svg
          class="w-3.5 h-3.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
          />
        </svg>
        <span>{{ completionText }}</span>
      </div>
    </div>
    <div
      v-if="hasQuestionSlot"
      class="mb-4 prose prose-slate dark:prose-invert"
    >
      <slot name="question" />
    </div>
    <div class="space-y-2">
      <slot />
    </div>
  </div>
</template>
