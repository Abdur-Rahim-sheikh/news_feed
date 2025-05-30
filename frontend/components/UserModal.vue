<script setup>
import ComboInput from './ComboInput.vue'

const props = defineProps(["user"])
const emit = defineEmits(["close"])


const close_modal = () => {
  emit("close")
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
                <ComboInput />
              </div>
              <div class="mt-2">
                <label class="font-semibold">Choose Sources</label>
                <ComboInput />
              </div>
              <div class="mt-2">
                <label class="font-semibold">Choose Keywords</label>
                <ComboInput />
              </div>
            </div>
            <div class="bg-gray-50 px-4 py-3 items-end justify-end sm:flex sm:flex-row sm:px-6">
              <button type="button" v-on:click="close_modal"
                class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>

              <button type="button"
                class="inline-flex w-full justify-center rounded-md bg-gray-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-gray-700 sm:ml-3 sm:w-auto">Submit</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>