<script setup>
import { ref, computed } from 'vue'

import {
    Combobox,
    ComboboxInput,
    ComboboxButton,
    ComboboxOptions,
    ComboboxOption,
    TransitionRoot,
} from '@headlessui/vue'


defineProps(["idNameMapping"])
const emit = defineEmits(["selectedId"])
const idNameMapping = [
    { id: 1, name: "abir" },
    { id: 2, name: "nadia" },
    { id: 3, name: "kabira" }
]

let selected = ref('')
let query = ref('')

let filteredSource = computed(() =>
    query.value === ''
        ? idNameMapping
        : idNameMapping.filter((entry) =>
            entry.name
                .toLowerCase()
                .replace(/\s+/g, '')
                .includes(query.value.toLowerCase().replace(/\s+/g, ''))
        )
)
watch(selected, (newSelected) => {
    emit("selectedId", newSelected.id)
})
</script>
<template>
    <Combobox v-model="selected">
        <div class="relative">
            <div
                class="relative w-full flex items-center bg-white ring-2 ring-gray-300 focus-within:ring-gray-500 rounded-2xl">
                <img src="/icons/search.svg" alt="search icon" class="absolute left-2 pointer-events-none h-4 w-4" />
                <ComboboxInput
                    class="w-full ps-8 py-1 font-semibold placeholder-gray-300 text-black border-none rounded-2xl focus:outline-none"
                    :displayValue="(entry) => entry.name" placeholder="Search" @change="query = $event.target.value" />
                <ComboboxButton class="absolute right-2">
                    <img src="/icons/unfold_more.svg" class="h-4 w-4 text-gray-400" aria-hidden="true" />
                </ComboboxButton>
            </div>

            <TransitionRoot leave="transition ease-in duration-100" leaveFrom="opacity-100" leaveTo="opacity-0"
                @after-leave="query = ''">
                <ComboboxOptions
                    class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 sm:text-sm">
                    <div v-if="filteredSource.length === 0 && query !== ''"
                        class="relative cursor-default select-none px-4 py-2 text-gray-700">
                        Nothing found.
                    </div>

                    <ComboboxOption v-for="entry in filteredSource" as="template" :key="entry.id" :value="entry"
                        v-slot="{ selected, active }">
                        <li class="relative cursor-default select-none py-2 pl-10 pr-4" :class="{
                            'bg-teal-600 text-white': active,
                            'text-gray-900': !active,
                        }">
                            <span class="block truncate" :class="{ 'font-medium': selected, 'font-normal': !selected }">
                                {{ entry.name }}
                            </span>
                            <span v-if="selected" class="absolute inset-y-0 left-0 flex items-center pl-3"
                                :class="{ 'text-white': active, 'text-teal-600': !active }">
                                <img src="/icons/check.svg" class="h-5 w-5" aria-hidden="true" />
                            </span>
                        </li>
                    </ComboboxOption>
                </ComboboxOptions>
            </TransitionRoot>
        </div>
    </Combobox>
</template>