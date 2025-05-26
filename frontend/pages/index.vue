<script setup>
let { data: articles } = await useFetch("/api/news")

</script>

<template>
    <ClientOnly>
        <div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 p-4 m-3">
                <AppCard v-for="article in articles" :key="article.title" :article="article" />
            </div>
        </div>
    </ClientOnly>
</template>