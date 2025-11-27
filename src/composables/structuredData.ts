import type { RouteLocationNormalized } from 'vue-router'
import { SUPPORTED_LOCALES } from './useI18n'

function getSiteUrl(): string {
  const envBaseUrl = import.meta.env.VITE_BASE_URL || 'pythoncheatsheet.org'
  const isDev = import.meta.env.DEV || import.meta.env.MODE === 'development'

  const isLocalhost = typeof window !== 'undefined' &&
    (window.location.hostname === 'localhost' ||
      window.location.hostname === '127.0.0.1' ||
      window.location.hostname.startsWith('192.168.') ||
      window.location.hostname.includes('.local'))

  const isPreviewDomain = envBaseUrl.includes('next.') ||
    envBaseUrl.includes('staging.') ||
    envBaseUrl.includes('preview.')

  if (isDev || isLocalhost || isPreviewDomain) {
    return 'https://pythoncheatsheet.org'
  }

  const baseUrl = envBaseUrl.startsWith('http') ? envBaseUrl : `https://${envBaseUrl}`
  return baseUrl.replace(/\/$/, '')
}

const siteUrl = getSiteUrl()

interface ArticleMeta {
  title?: string
  description?: string
  date?: string
  updated?: string
  tags?: string
  socialImage?: string
}

export function generateWebSiteSchema(locale: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'Python Cheatsheet',
    url: siteUrl,
    description: 'A comprehensive Python cheatsheet with examples and explanations',
    inLanguage: locale,
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: `${siteUrl}/search?q={search_term_string}`,
      },
      'query-input': 'required name=search_term_string',
    },
  }
}

export function generateOrganizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Python Cheatsheet',
    url: siteUrl,
    logo: `${siteUrl}/logo.svg`,
    sameAs: [
      'https://github.com/labex-labs/python-cheatsheet',
    ],
  }
}

export function generateArticleSchema(
  route: RouteLocationNormalized,
  meta: ArticleMeta,
  locale: string
) {
  const articleUrl = `${siteUrl}${route.path}`
  const imageUrl = meta.socialImage
    ? meta.socialImage.startsWith('http')
      ? meta.socialImage
      : `${siteUrl}${meta.socialImage}`
    : `${siteUrl}/screenshots/dark.png`

  const tags = meta.tags
    ? (typeof meta.tags === 'string' 
        ? meta.tags 
        : Array.isArray(meta.tags) 
          ? (meta.tags as string[]).join(',')
          : String(meta.tags)
      ).split(',').map((tag: string) => tag.trim()).filter(Boolean)
    : []

  const parseDate = (dateStr: string | undefined): string | undefined => {
    if (!dateStr) return undefined
    try {
      const date = new Date(dateStr)
      if (isNaN(date.getTime())) return undefined
      return date.toISOString()
    } catch {
      return undefined
    }
  }

  const publishedDate = parseDate(meta.date)
  const modifiedDate = parseDate(meta.updated) || publishedDate

  const schema: any = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: meta.title || '',
    description: meta.description || '',
    image: imageUrl,
    datePublished: publishedDate,
    dateModified: modifiedDate,
    author: {
      '@type': 'Organization',
      name: 'Python Cheatsheet',
      url: siteUrl,
    },
    publisher: {
      '@type': 'Organization',
      name: 'Python Cheatsheet',
      logo: {
        '@type': 'ImageObject',
        url: `${siteUrl}/logo.svg`,
      },
    },
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': articleUrl,
    },
    inLanguage: locale,
  }

  if (tags.length > 0) {
    schema.keywords = tags.join(', ')
  }

  return schema
}

export function generateBreadcrumbSchema(
  route: RouteLocationNormalized
) {
  const segments = route.path.split('/').filter(Boolean)
  const items: any[] = [
    {
      '@type': 'ListItem',
      position: 1,
      name: 'Home',
      item: siteUrl,
    },
  ]

  let currentPath = ''
  let position = 2

  for (const segment of segments) {
    if (SUPPORTED_LOCALES.includes(segment as typeof SUPPORTED_LOCALES[number])) {
      if (segment !== 'en') {
        currentPath += `/${segment}`
        items.push({
          '@type': 'ListItem',
          position: position++,
          name: segment.toUpperCase(),
          item: `${siteUrl}${currentPath}`,
        })
      }
      continue
    }

    currentPath += `/${segment}`
    const name = segment
      .split('-')
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ')

    items.push({
      '@type': 'ListItem',
      position: position++,
      name,
      item: `${siteUrl}${currentPath}`,
    })
  }

  if (items.length <= 1) {
    return null
  }

  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items,
  }
}

export function generateStructuredData(
  route: RouteLocationNormalized,
  locale: string,
  articleMeta?: ArticleMeta
) {
  const schemas: any[] = []

  if (route.path === '/' || route.path === `/${locale}`) {
    schemas.push(generateWebSiteSchema(locale))
    schemas.push(generateOrganizationSchema())
  } else {
    schemas.push(generateOrganizationSchema())
  }

  if (articleMeta && articleMeta.title) {
    schemas.push(generateArticleSchema(route, articleMeta, locale))
  }

  const breadcrumb = generateBreadcrumbSchema(route)
  if (breadcrumb) {
    schemas.push(breadcrumb)
  }

  return schemas
}

