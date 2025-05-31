<script setup>
let articles = ref([])
let totalArticles = ref(0)
let pageNumber = ref(0)
let totalPage = ref(0)
let selectedStartDate = ref("")
let selectedEndDate = ref("")
let selectedSourceId = ref("")
let selectedKeyword = ref("")
const limit = 6


const searchQuery = async (pageNumber = 0) => {
    console.log("queries", selectedKeyword)
    let response = await $fetch("/api/news", {
        method: "GET",
        params: {
            fromDate: selectedStartDate.value,
            toDate: selectedEndDate.value,
            keyword: selectedKeyword.value,
            sourceId: selectedSourceId.value,
            pageNumber: pageNumber,
            limit: limit,
        }
    })
    articles.value = response.articles
    totalArticles.value = response.totalArticles
    totalPage.value = Math.ceil(totalArticles.value / limit)
    console.log("articles", articles.value)
    console.log("totalArticles", totalArticles.value)

}
const changePage = (value) => {
    pageNumber.value += value
    if (pageNumber.value < 0 || pageNumber.value >= totalPage.value) {
        pageNumber.value -= value;
        return
    }
    searchQuery(pageNumber.value)

}

onMounted(() => {
    searchQuery(0)
})
</script>

<template>


    <ClientOnly>
        <TopBar @search="searchQuery" @startDate="(x) => selectedStartDate = x" @endDate="(x) => selectedEndDate = x"
            @sourceId="(x) => selectedSourceId = x" @keyword="(x) => selectedKeyword = x" />


        <div v-if="totalPage == 0">
            <span class="flex items-center justify-center">Sorry! nothing found!</span>
        </div>
        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-5 px-20 m-32">
            <AppCard v-for="article in articles" :key="article.title" :article="article" />
        </div>
        <div v-if="totalPage" class="flex justify-end items-center gap-4 p-5 mb-8">
            <button @click="changePage(-1)" aria-label="Previous page" class="p-2 rounded-full transition 
           text-blue-600 hover:bg-blue-50 
           disabled:text-gray-300 disabled:hover:bg-transparent 
           disabled:cursor-not-allowed" :disabled="pageNumber == 0">
                <img src="/icons/forward.svg" class="rotate-180 w-15 h-15" alt="Previous page">
            </button>

            <span class="text-sm font-medium text-gray-700">
                {{ pageNumber + 1 }} / {{ totalPage }}
            </span>

            <button @click="changePage(1)" aria-label="Next page" class="p-2 rounded-full transition 
           text-blue-600 hover:bg-blue-50 
           disabled:text-gray-300 disabled:hover:bg-transparent 
           disabled:cursor-not-allowed" :disabled="pageNumber == (totalPage - 1)">
                <img src="/icons/forward.svg" class="w-15 h-15" alt="Next page">
            </button>
        </div>

    </ClientOnly>



</template>