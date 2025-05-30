<script setup>
const user = useCookie("user", { watch: true })

const source_dict = useState("source_dict", () => null)

if (!source_dict.value) {
    source_dict.value = await $fetch("/api/sources")
}

const modal_active = ref(false)

const toggle_modal = () => {
    modal_active.value = !modal_active.value
}
</script>

<template>
    <nav class="bg-gray-800">
        <div class="mx-auto px-5">
            <header>
                <div class="relative flex h-16 items-center justify-between">
                    <h2 class="text-white text-4xl">Newsroom</h2>
                    <div class="relative flex content-center justify-between space-x-2">
                        <span class="text-white text-xl content-center">Hi, {{ user.username }}</span>
                        <img v-on:click="toggle_modal" src="public/icons/profile.svg" class="w-10 h-10"
                            alt="profile icon">
                    </div>
                </div>
            </header>
        </div>
    </nav>
    <UserModal v-show="modal_active" @close="toggle_modal" :user="user" />
</template>