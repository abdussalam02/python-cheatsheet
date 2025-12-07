<script setup>
import { generateStructuredData } from '~/composables/structuredData'

const route = useRoute()
const { currentLocale } = useI18n()

// Extract article meta from route
const articleMeta = computed(() => {
  const routeMeta = route.meta || {}
  const childMeta = route.matched[0]?.children?.[0]?.meta || {}

  if (routeMeta.title || routeMeta.date) {
    return {
      title: routeMeta.title,
      description: routeMeta.description,
      date: routeMeta.date,
      updated: routeMeta.updated,
      tags: routeMeta.tags,
      socialImage: routeMeta.socialImage,
    }
  }

  if (childMeta.title || childMeta.date) {
    return {
      title: childMeta.title,
      description: childMeta.description,
      date: childMeta.date,
      updated: childMeta.updated,
      tags: childMeta.tags,
      socialImage: childMeta.socialImage,
    }
  }

  return undefined
})

const { meta } = useMeta(articleMeta.value)
useHead(meta)
useScrollBehavior()
const { t } = useI18n()

// Generate structured data
const structuredData = computed(() => {
  return generateStructuredData(route, currentLocale.value, articleMeta.value)
})

// Inject structured data as JSON-LD
useHead({
  script: computed(() =>
    structuredData.value.map((schema, index) => ({
      type: 'application/ld+json',
      innerHTML: JSON.stringify(schema),
      key: `structured-data-${index}-${route.path}`,
    })),
  ),
})

// Inject Google Analytics script if VITE_GTAG is configured
const gTag = import.meta.env.VITE_GTAG
if (gTag && gTag !== 'tag' && gTag.trim() !== '') {
  useHead({
    script: [
      {
        src: `https://www.googletagmanager.com/gtag/js?id=${gTag}`,
        async: true,
      },
      {
        innerHTML: `
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', '${gTag}');
        `,
      },
    ],
  })
}
</script>

<template>
  <RouterView />
</template>
