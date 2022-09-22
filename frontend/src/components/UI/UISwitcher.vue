<template>
  <span class="isolate inline-flex rounded-md shadow-sm">
    <button type="button" class="relative inline-flex items-center rounded-l-md border border-gray-300 bg-white px-2 py-2 text-sm font-medium text-gray-500 hover:bg-gray-50 focus:z-10 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500">
      <span class="sr-only">Previous</span>
      <CurrencyEuroIcon class="h-5 w-5" aria-hidden="true" />
    </button>
    <button type="button" class="relative -ml-px inline-flex items-center rounded-r-md border border-gray-300 bg-white px-2 py-2 text-sm font-medium text-gray-500 hover:bg-gray-50 focus:z-10 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500">
      <span class="sr-only">Next</span>
      <CurrencyDollarIcon class="h-5 w-5" aria-hidden="true" />
    </button>
  </span>
</template>

<script setup>
import { CurrencyDollarIcon,CurrencyEuroIcon } from '@heroicons/vue/20/solid'
</script>