<script setup>
let articles = ref([])
console.log("articles", articles.value)
const searchQuery = async (queries) => {
    console.log("queries", queries, queries.fromDate)
    articles.value = await $fetch("/api/news", {
        method: "GET",
        params: {
            fromDate: queries.fromDate,
            toDate: queries.toDate,
            keyword: queries.keyword,
            sourceId: queries.sourceId
        }
    })
}

onMounted(() => {
    searchQuery({
        fromDate: "",
        toDate: "",
        keyword: "",
        sourceId: ""
    })
})
</script>

<template>


    <ClientOnly>
        <TopBar @queries="searchQuery" />


        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 px-20 m-32">
            <AppCard v-for="article in articles" :key="article.title" :article="article" />
        </div>
    </ClientOnly>



</template>