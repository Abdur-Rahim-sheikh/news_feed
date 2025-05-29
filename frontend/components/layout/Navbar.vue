<script setup>
const username = useCookie("user", { watch: true }).value.username

</script>

<template>
    <nav class="bg-gray-800">
        <div class="mx-auto px-5">
            <header>
                <div class="relative flex h-16 items-center justify-between">
                    <h2 class="text-white text-4xl">Newsroom</h2>
                    <div class="relative flex content-center justify-between space-x-2">
                        <span class="text-white text-xl content-center">Hi, {{ username }}</span>
                        <img src="public/icons/profile.svg" class="w-10 h-10" alt="profile icon">
                    </div>
                </div>
            </header>
        </div>
    </nav>
</template>