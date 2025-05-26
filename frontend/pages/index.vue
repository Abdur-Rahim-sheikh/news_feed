<script setup>
let { data: articles } = await useFetch("/api/news")

</script>

<template>
    <ClientOnly>
        <div>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 px-20 m-32">
                <AppCard v-for="article in articles" :key="article.title" :article="article" />
            </div>
        </div>
    </ClientOnly>
</template>