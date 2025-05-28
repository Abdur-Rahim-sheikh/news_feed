<script setup>
const emit = defineEmits(["queries"])
const sources = ["BBC news", "Abn News"]
const PAST_INFINITY = '0001-01-01'
const FUTURE_INFINITY = '275760-09-13'
let sourceId = ref(null)
let startDate = ref(null)
let endDate = ref(null)
let keyword = ref(null)

let getSelectedSourceId = (newSourceId) => {
    console.log("selected source", newSourceId)
    sourceId.value = newSourceId
}

let submitQuery = () => {
    let fromDate = startDate.value || PAST_INFINITY
    let toDate = endDate.value || FUTURE_INFINITY
    let srcId = sourceId.value || ""
    let kwrg = keyword.value || ""
    console.log("TopBar", {
        fromDate,
        toDate,
        sourceId: srcId,
        keyword: kwrg,
    })
    emit("queries", {
        fromDate,
        toDate,
        sourceId: srcId,
        keyword: kwrg,
    })
}
</script>

<template>
    <div class="relative w-full">
        <div class="p-4 mb-2 flex justify-center bg-gray-50 gap-2 space-x-6">
            <div class="flex "><input type="date" v-model="startDate" name="start_date" id="start-date"
                    class=" p-1 font-semibold placeholder-gray-300 text-black rounded-2xl border-none ring-2 ring-gray-300 focus:ring-gray-500">
                <img src="/icons/range_arrow.svg" alt="range icon">
                <input type="date" v-model="endDate" name="end_date" id="end-date" class=" p-1 font-semibold placeholder-gray-300 text-black rounded-2xl border-none ring-2 ring-gray-300
                focus:ring-gray-500">

            </div>
            <div class="relative flex items-center ">
                <img src="/icons/search.svg" alt="search icon" class="absolute ms-2 pointer-events-none">
                <input type="search" v-model="keyword" name="search_term" id="search-term" placeholder="Search"
                    class="ps-10 py-1 font-semibold placeholder-gray-300 text-black rounded-2xl border-none ring-2 ring-gray-300 focus:ring-gray-500">
            </div>

            <div>
                <ComboInput @selectedId="getSelectedSourceId" />
            </div>
            <div><button type="submit" v-on:click="submitQuery"
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 py-1 mx-1 rounded-full cursor-grabbing">Submit</button>
            </div>


        </div>
    </div>
</template>