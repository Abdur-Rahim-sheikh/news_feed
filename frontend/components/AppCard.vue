<script setup>
defineProps(["article"])
</script>


<template>
  <div class="article-wrap flex flex-col gap-4 lg:flex-row lg:items-start">
    <div class="col-md-6 flex-1 lg:flex-1/2">
      <a :href="article.source_url" target="_blank"><img :src="article.thumbnail_url" alt="article icon"
          class="w-full h-auto block rounded-md object-cover"></a>

    </div>

    <div class="col-md-6 flex-1 lg:flex-1/2">
      <div class="py-2">
        <div>
          <span class="text-amber-700">{{ article.source_name }}</span>
          <time class="ms-2 text-shadow-sm text-gray-700" :datetime="article.published_at">{{
            article.published_at }}</time>
        </div>



        <h2 class="my-2 text-xl font-semibold"><a :href="article.source_url" target="_blank">{{ article.title }}</a>
        </h2>

        <a :href="article.source_url" target="_blank" class="inline-block my-2 font-sans text-sm text-amber-700">READ
          MORE</a>
        <div>
          <p class="m-0 text-base text-gray-600">{{ article.summary }}</p>
        </div>
      </div>
    </div>
  </div>
</template>