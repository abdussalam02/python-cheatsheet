import { SUPPORTED_LOCALES, useI18n } from './useI18n'

export function useMeta() {
  const route = useRoute()
  const { t } = useI18n()
  const base_url = import.meta.env.VITE_BASE_URL || 'localhost:3000'

  const description = computed(() => t('meta.description'))
  const cardImage =
    'https://raw.githubusercontent.com/labex-labs/python-cheatsheet/master/public/screenshots/dark.png'
  const themeColor = computed(() => (isDark.value ? '#1f2937' : '#ffffff'))
  const url = computed(() => `https://${base_url}${route.path}`)

  // Get base path (remove locale prefix)
  const getBasePath = (path: string): string => {
    const segments = path.split('/').filter(Boolean)
    if (segments.length > 0 && SUPPORTED_LOCALES.includes(segments[0] as typeof SUPPORTED_LOCALES[number])) {
      segments.shift()
      return segments.length > 0 ? '/' + segments.join('/') : '/'
    }
    return path
  }

  // Generate hreflang links
  const generateHreflangLinks = computed(() => {
    const basePath = getBasePath(route.path)
    const links = []

    // Generate hreflang link for each supported locale
    for (const locale of SUPPORTED_LOCALES) {
      const localePath = locale === 'en' ? basePath : `/${locale}${basePath}`
      const localeUrl = `https://${base_url}${localePath}`
      links.push({
        rel: 'alternate',
        hreflang: locale,
        href: localeUrl,
      })
    }

    // Add x-default (points to default language version)
    const defaultPath = basePath
    const defaultUrl = `https://${base_url}${defaultPath}`
    links.push({
      rel: 'alternate',
      hreflang: 'x-default',
      href: defaultUrl,
    })

    return links
  })

  const title = computed(() => t('meta.title'))
  const keywords = computed(() => t('meta.keywords'))

  const meta = computed(() => ({
    title: title.value,
    description: description.value,
    meta: [
      { name: 'theme-color', content: themeColor.value },
      { name: 'description', content: description.value },
      { name: 'author', content: 'Python Cheatsheet' },
      { name: 'keywords', content: keywords.value },
      { property: 'og:title', content: title.value },
      { property: 'og:description', content: description.value },
      { property: 'og:url', content: url.value },
      { property: 'og:type', content: 'article' },
      { property: 'og:image', content: cardImage },
      { name: 'twitter:title', content: title.value },
      { name: 'twitter:description', content: description.value },
      { name: 'twitter:image', content: cardImage },
      { name: 'twitter:card', content: 'summary' },
    ],
    link: [
      { rel: 'canonical', href: url.value },
      ...generateHreflangLinks.value,
    ],
  }))

  return { meta, description }
}
