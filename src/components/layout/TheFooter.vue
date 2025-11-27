<script setup lang="ts">
const isDark = useDark()
const { currentLocale, t } = useI18n()

const getCheatsheetsUrl = () => {
  const baseUrl = 'https://labex.io/cheatsheets'
  const localeMap: Record<string, string> = {
    en: '',
    zh: '/zh',
    es: '/es',
    fr: '/fr',
    de: '/de',
    ja: '/ja',
    ru: '/ru',
    ko: '/ko',
    pt: '/pt',
  }
  const localePath = localeMap[currentLocale.value] || ''
  return `${baseUrl}${localePath}`
}
</script>

<template>
  <footer class="mt-5 border-t dark:border-t-slate-800">
    <div class="pt-5 flex items-center justify-between">
      <a
        href="https://labex.io/learn"
        target="_blank"
        class="flex items-center text-slate-600 transition duration-300 hover:text-primary-500 dark:text-slate-400 dark:hover:text-primary-400"
      >
        <img
          class="h-5 w-auto"
          :src="
            isDark
              ? 'https://cdn.jsdelivr.net/gh/labex-labs/files@master/images/labex-logo-light.svg'
              : 'https://cdn.jsdelivr.net/gh/labex-labs/files@master/images/labex-logo-dark.svg'
          "
          alt="LabEx"
          height="20"
          width="20"
        />
      </a>
      <a
        :href="getCheatsheetsUrl()"
        target="_blank"
        class="inline-flex items-center gap-1.5 text-sm font-medium text-primary-600 underline underline-offset-4 transition duration-300 hover:text-primary-700 dark:text-primary-400 dark:hover:text-primary-300"
      >
        {{ t('footer.moreCheatsheets') }}
        <external-link-icon />
      </a>
    </div>
  </footer>
</template>
