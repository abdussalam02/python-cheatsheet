<script setup lang="ts">
const { t } = useI18n()

defineProps({
  currentPage: {
    type: Number,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(['prev-page', 'next-page'])

const prev = () => {
  emit('prev-page')
}

const next = () => {
  emit('next-page')
}
</script>

<template>
  <div class="mt-12 flex items-center justify-between gap-x-6 max-w-lg mx-auto">
    <button
      :disabled="currentPage === 1"
      class="flex flex-col rounded-md border border-slate-300/70 px-3 py-2 text-left transition duration-200 hover:border-primary-500 hover:bg-primary-400/5 disabled:cursor-not-allowed disabled:opacity-50 dark:border-slate-800 dark:hover:border-primary-400"
      @click="prev"
    >
      <span class="text-xs text-slate-500 dark:text-slate-400">{{ t('blog.previous') }}</span>
      <span class="text-sm font-medium text-primary-500 dark:text-primary-400">
        {{ t('blog.newerPosts') }}
      </span>
    </button>

    <span class="text-sm font-medium text-slate-700 dark:text-slate-300">
      {{ currentPage }} / {{ totalPages }}
    </span>

    <button
      :disabled="currentPage === totalPages"
      class="flex flex-col rounded-md border border-slate-300/70 px-3 py-2 text-right transition duration-200 hover:border-primary-500 hover:bg-primary-400/5 disabled:cursor-not-allowed disabled:opacity-50 dark:border-slate-800 dark:hover:border-primary-400"
      @click="next"
    >
      <span class="text-xs text-slate-500 dark:text-slate-400">{{ t('blog.next') }}</span>
      <span class="text-sm font-medium text-primary-500 dark:text-primary-400">
        {{ t('blog.olderPosts') }}
      </span>
    </button>
  </div>
</template>
