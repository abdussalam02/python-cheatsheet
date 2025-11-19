<script setup>
const { meta } = useMeta()
useHead(meta)
useScrollBehavior()
const { t } = useI18n()

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
  <BaseBanner storage-key-name="black-friday-2025-banner">
    <template #message>
      <span class="text-white">
        {{ t('banner.title') }}
        <a
          href="https://labex.io/learn/python"
          target="_blank"
          class="font-semibold text-white underline hover:text-slate-200"
          >{{ t('banner.learnPython') }}</a
        >
        {{ t('banner.withLabex') }}
        <a
          href="https://labex.io/pricing"
          target="_blank"
          class="ml-1 font-semibold text-white underline hover:text-slate-200"
        >
          {{ t('banner.getDiscount') }}
        </a>
      </span>
    </template>
    <template #shortMsg>
      <span class="text-white">
        {{ t('banner.shortMessage') }}
        <a
          href="https://labex.io/pricing"
          target="_blank"
          class="ml-1 font-semibold text-white underline hover:text-slate-200"
        >
          {{ t('banner.shortDiscount') }}
        </a>
      </span>
    </template>
  </BaseBanner>
  <RouterView />
</template>
