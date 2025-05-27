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

const people = [
    { id: 1, name: 'Wade Cooper' },
    { id: 2, name: 'Arlene Mccoy' },
    { id: 3, name: 'Devon Webb' },
    { id: 4, name: 'Tom Cook' },
    { id: 5, name: 'Tanya Fox' },
    { id: 6, name: 'Hellen Schmidt' },
]

let selected = ref(people[0])
let query = ref('')

let filteredPeople = computed(() =>
    query.value === ''
        ? people
        : people.filter((person) =>
            person.name
                .toLowerCase()
                .replace(/\s+/g, '')
                .includes(query.value.toLowerCase().replace(/\s+/g, ''))
        )
)
</script>
<template>
    <Combobox v-model="selected">
        <div class="relative">
            <div
                class="relative w-full flex items-center bg-white ring-2 ring-gray-300 focus-within:ring-gray-500 rounded-2xl">
                <img src="/icons/search.svg" alt="search icon" class="absolute left-2 pointer-events-none h-4 w-4" />
                <ComboboxInput
                    class="w-full ps-8 py-1 font-semibold placeholder-gray-300 text-black border-none rounded-2xl focus:outline-none"
                    :displayValue="(person) => person.name" placeholder="Search"
                    @change="query = $event.target.value" />
                <ComboboxButton class="absolute right-2">
                    <img src="/icons/unfold_more.svg" class="h-4 w-4 text-gray-400" aria-hidden="true" />
                </ComboboxButton>
            </div>

            <TransitionRoot leave="transition ease-in duration-100" leaveFrom="opacity-100" leaveTo="opacity-0"
                @after-leave="query = ''">
                <ComboboxOptions
                    class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 sm:text-sm">
                    <div v-if="filteredPeople.length === 0 && query !== ''"
                        class="relative cursor-default select-none px-4 py-2 text-gray-700">
                        Nothing found.
                    </div>

                    <ComboboxOption v-for="person in filteredPeople" as="template" :key="person.id" :value="person"
                        v-slot="{ selected, active }">
                        <li class="relative cursor-default select-none py-2 pl-10 pr-4" :class="{
                            'bg-teal-600 text-white': active,
                            'text-gray-900': !active,
                        }">
                            <span class="block truncate" :class="{ 'font-medium': selected, 'font-normal': !selected }">
                                {{ person.name }}
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