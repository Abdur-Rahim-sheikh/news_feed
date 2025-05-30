<script setup>
const props = defineProps(["id", "name"])
const emit = defineEmits(["remove"])
console.log(props)
const remove_pill = () => {
    emit('remove', props.id)
}
</script>

<template>
    <div @click="remove_pill"
        class="inline-flex items-center space-x-1 bg-blue-500 hover:bg-blue-700 text-white font-bold px-3 py-1 rounded-full cursor-pointer">
        <span>{{ props.name }}</span>
        <img src="/icons/close.svg" alt="close icon" class="w-4 h-4" />
    </div>

</template>