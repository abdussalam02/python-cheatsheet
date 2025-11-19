<script setup lang="ts">
import EditIcon from '~/components/icons/EditIcon.vue'
import QuestionIcon from '~/components/icons/QuestionIcon.vue'
import BugIcon from '~/components/icons/BugIcon.vue'
import { SUPPORTED_LOCALES } from '~/composables/useI18n'

const props = defineProps<{
  repository?: string
}>()

const route = useRoute()
const { t } = useI18n()

// Convert route path to GitHub file path
// For docs directory:
//   Route: /zh/cheatsheet/basics -> File: /cheatsheet/zh/basics.md
//   Route: /cheatsheet/basics -> File: /cheatsheet/en/basics.md
// For src/pages directory (contributing, changelog):
//   Route: /contributing -> File: /contributing.md
//   Route: /zh/contributing -> File: /contributing.md (redirects to English)
const getGitHubFilePath = (path: string): string => {
  const segments = path.split('/').filter(Boolean)
  
  if (segments.length === 0) {
    return ''
  }

  // Check if first segment is a locale
  const firstSegment = segments[0]
  const isLocaleFirst = SUPPORTED_LOCALES.includes(firstSegment as typeof SUPPORTED_LOCALES[number])
  
  // Handle docs directory structure: {section}/{locale}/{file}.md
  if (isLocaleFirst && segments.length >= 3) {
    // Format: /{locale}/{section}/{file} -> /{section}/{locale}/{file}.md
    const [, section, ...fileParts] = segments
    const file = fileParts.join('/')
    return `/${section}/${firstSegment}/${file}.md`
  } else if (segments.length >= 2) {
    // Format: /{section}/{file} -> /{section}/en/{file}.md (English default)
    const [section, ...fileParts] = segments
    const file = fileParts.join('/')
    return `/${section}/en/${file}.md`
  } else {
    // Single segment (e.g., /contributing, /changelog)
    // For src/pages, these are .md files directly
    // For locale versions that redirect, still point to the English .md file
    return `/${segments[0]}.md`
  }
}

const EditLink = computed(() => ({
  linkHeader: t('footer.editThisPageOn'),
  linkText: t('footer.github'),
  url: `${props.repository}${getGitHubFilePath(route.path)}`,
  icon: EditIcon,
}))

const footerLinks = computed(() => [
  {
    linkHeader: t('footer.doYouHaveAQuestion'),
    linkText: t('footer.askTheCommunity'),
    url: 'https://github.com/labex-labs/python-cheatsheet/discussions',
    icon: QuestionIcon,
  },
  {
    linkHeader: t('footer.doYouSeeABug'),
    linkText: t('footer.openAnIssueOnGithub'),
    url: 'https://github.com/labex-labs/python-cheatsheet/issues',
    icon: BugIcon,
  },
])

const routesWithoutGithub = ['index', 'blog']
</script>

<template>
  <footer class="mt-5 border-t dark:border-t-slate-800">
    <div class="justify-between pt-5 sm:flex">
      <div
        class="grid text-xs"
        :class="route.name !== 'index' ? 'space-y-1.5' : ''"
      >
        <div
          v-if="!routesWithoutGithub.includes(route.name as string)"
          class="flex items-center text-slate-600 dark:text-slate-400"
        >
          <component :is="EditLink.icon" class="mr-2 h-4 w-4" />
          {{ EditLink.linkHeader }}
          <a
            target="_blank"
            :href="EditLink.url"
            class="ml-1 flex text-primary-500 hover:text-primary-600 dark:text-primary-400 dark:hover:text-primary-500"
          >
            {{ EditLink.linkText }}
          </a>
        </div>

        <div
          v-for="link in footerLinks"
          :key="link.url"
          class="flex items-center text-slate-600 dark:text-slate-400"
        >
          <component :is="link.icon" class="mr-2 h-4 w-4" />
          {{ link.linkHeader }}
          <a
            target="_blank"
            :href="link.url"
            class="ml-1 flex text-primary-500 hover:text-primary-600 dark:text-primary-400 dark:hover:text-primary-500"
          >
            {{ link.linkText }}
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>
