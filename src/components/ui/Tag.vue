<template>
  <span
    class="inline-flex items-center rounded-md text-xs font-medium uppercase bg-primary-500 px-2.5 py-1 text-slate-50 shadow-sm transition-all duration-200 hover:bg-primary-600 hover:shadow-md hover:scale-105 dark:bg-primary-600 dark:hover:bg-primary-500 dark:text-white"
  >
    #<slot />
  </span>
</template>

<script setup lang="ts">
// No props needed, tag content is passed via slot
</script>
