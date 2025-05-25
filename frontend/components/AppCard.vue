<script setup>
defineProps(["article"])
</script>


<template>
  <div
    class="max-w-md flex flex-col bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700 overflow-hidden">
    <a :href="article.source_url" target="_blank">
      <img class="w-full h-16 object-cover rounded-t-lg" :src="article.thumbnail_url" alt="" />
    </a>

    <div class="flex flex-col flex-1 p-4 overflow-hidden">
      <h5 class="text-lg font-bold text-gray-900 dark:text-white">
        {{ article.title }}
      </h5>


      <p class="text-sm text-gray-700 dark:text-gray-400 overflow-clip mt-2">
        {{ article.summary }}
      </p>
      <div class="mt-auto">
        <a :href="article.source_url" target="_blank"
          class="mt-3 inline-flex items-center justify-center px-3 py-2 text-sm font-medium text-white bg-blue-700 hover:bg-blue-800 rounded focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
          Read more
          <img src="public/icons/read_more.svg" alt="read more in original source" class="ml-2" />
        </a>
      </div>
    </div>
  </div>



</template>