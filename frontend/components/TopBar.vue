<script setup>
const sources = ["BBC news", "Abn News"]
const selectedSource = ref(null)
</script>

<template>
    <div class="relative w-full">
        <div class="p-4 mb-2 flex justify-center bg-gray-50 gap-2 space-x-6">
            <div class="flex "><input type="date" name="start_date" id="start-date"
                    class=" p-1 font-semibold placeholder-gray-300 text-black rounded-2xl border-none ring-2 ring-gray-300 focus:ring-gray-500">
                <img src="/icons/range_arrow.svg" alt="range icon">
                <input type="date" name="end_date" id="end-date" class=" p-1 font-semibold placeholder-gray-300 text-black rounded-2xl border-none ring-2 ring-gray-300
                focus:ring-gray-500">

            </div>
            <div class="relative flex items-center ">
                <img src="/icons/search.svg" alt="search icon" class="absolute ms-2 pointer-events-none">
                <input type="search" name="search_term" id="search-term" placeholder="Search"
                    class="ps-10 py-1 font-semibold placeholder-gray-300 text-black rounded-2xl border-none ring-2 ring-gray-300 focus:ring-gray-500">
            </div>




            <div>
                <SourceCombobox />
            </div>
            <div><button type="submit"
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 py-1 mx-1 rounded-full cursor-grabbing">Submit</button>
            </div>


        </div>
    </div>
</template>