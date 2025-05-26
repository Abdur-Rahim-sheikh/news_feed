<script setup>
defineProps(["article"])
</script>


<template>
  <div
    class="max-w-md flex flex-col bg-white border border-gray-200 rounded-lg shadow-sm dark:border-gray-700 overflow-hidden">
    <a :href="article.source_url" target="_blank">
      <img class="w-full h-16 object-cover rounded-t-lg" :src="article.thumbnail_url" alt="" />
    </a>
    <div
      class="max-w-md flex flex-col flex-grow bg-gray-400  border border-gray-200 rounded-lg shadow-sm dark:border-gray-700 overflow-hidden m-2">

      <div class="flex flex-col flex-1 p-4 overflow-hidden">
        <h5 class="text-lg font-bold text-gray-900 dark:text-white">
          {{ article.title }}
        </h5>


        <p class="text-md overflow-clip mt-2">
          {{ article.summary }}
        </p>
        <div class="mt-auto">
          <a :href="article.source_url" target="_blank"
            class="mt-3 inline-flex items-center justify-center px-3 py-2 text-sm font-medium text-white bg-gray-500 hover:bg-blue-800 rounded focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-gray-500 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
            Read more
            <img src="/icons/read_more.svg" alt="read more in original source" class="ml-2" />
          </a>
        </div>
      </div>
    </div>
  </div>



</template>