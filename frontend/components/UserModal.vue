<script setup>
import ComboInput from './ComboInput.vue'

const props = defineProps(["user"])
const emit = defineEmits(["close"])
const available_sources = useState("sources")
const available_countries = useState("countries")
const _filter_ids = (available, selected) => {
  return available.value.filter(entry => selected.includes(entry.id))
}
let country_codes = ref(_filter_ids(available_countries, props.user.country_codes))
let source_ids = ref(_filter_ids(available_sources, props.user.source_ids))
let keywords = ref(props.user.keywords)
let selected_keyword = ref('')
console.log("Keywords", keywords.value)
const close_modal = () => {
  emit("close")
}

const add_source = (id) => {
  let entry = available_sources.value.filter(entry => entry.id == id)[0]
  source_ids.value.push(entry)
}
const remove_source = (id) => {
  source_ids.value = source_ids.value.filter(entry => entry.id != id)
}
const add_country = (id) => {
  let entry = available_countries.value.filter(entry => entry.id == id)[0]
  country_codes.value.push(entry)
}
const remove_country = (id) => {
  country_codes.value = country_codes.value.filter(entry => entry.id != id)
}
const add_keyword = () => {
  keywords.value.push(selected_keyword.value)
  selected_keyword.value = ''
}
const remove_keyword = (remove_id) => {
  keywords.value = keywords.value.filter(id => id != remove_id)
}

const update_user_choice = async () => {
  const selected_country_codes = country_codes.value.map(entry => entry.id)
  const selected_source_ids = source_ids.value.map(entry => entry.id)
  let response = await $fetch('/api/update_user', {
    method: 'POST',
    body: {
      selected_country_codes,
      selected_source_ids,
      selected_keywords: keywords.value,
    }
  })
  if (response.success) {
    close_modal()
  }
}
</script>

<template>
  <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">

    <div class="fixed inset-0 bg-gray-500/75 transition-opacity" aria-hidden="true"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="flex flex-col">

              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-base font-semibold text-gray-900" id="modal-title">Hello, {{ props.user.first_name }} {{
                  props.user.last_name }}</h3>

              </div>
              <div class="mt-2">
                <label class="font-semibold">Choose countries</label>
                <ComboInput :idNameMapping="available_countries" @selected-id="add_country" />
                <div class="mt-2 space-x-1 space-y-0.5">
                  <Pill v-for="country in country_codes" :key="country.id" :id="country.id" :name="country.name"
                    @remove="remove_country" />
                </div>

              </div>
              <div class="mt-2">
                <label class="font-semibold">Choose Sources</label>
                <ComboInput :idNameMapping="available_sources" @selected-id="add_source" />
                <div class="mt-2 space-x-1 space-y-0.5">
                  <Pill v-for="source in source_ids" :key="source.id" :id="source.id" :name="source.name"
                    @remove="remove_source" />
                </div>
              </div>
              <div class="mt-2">
                <label class="font-semibold">Choose Keywords</label>
                <div class="relative flex items-center">
                  <img src="/icons/search.svg" alt="search icon" class="absolute ms-2 pointer-events-none w-4 h-4">
                  <input v-on:keyup.enter="add_keyword" v-model="selected_keyword" placeholder="Search" class="ps-7 w-full border-[2px] border-gray-300 focus:outline-none focus:ring-0
                              focus:border-gray-500 rounded-full p-1 placeholder-gray-300 placeholder:font-bold">
                </div>

                <div class="mt-2 space-x-1 space-y-0.5 ">

                  <Pill v-for="keyword in keywords" :key="keyword" :id="keyword" :name="keyword"
                    @remove="remove_keyword" />
                </div>
              </div>
            </div>
            <div class="bg-gray-50 px-4 py-3 items-end justify-end sm:flex sm:flex-row sm:px-6">
              <button type="button" v-on:click="close_modal"
                class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>

              <button type="button" v-on:click="update_user_choice"
                class="inline-flex w-full justify-center rounded-md bg-gray-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-gray-700 sm:ml-3 sm:w-auto">Update</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>