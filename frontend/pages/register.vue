<script setup>
definePageMeta({
    title: "Register",
    layout: "auth",
})
const route = useRoute()
let first_name = ref("")
let last_name = ref("")
let email = ref("")
let username = ref("")
let password = ref("")
let confirm_passowrd = ref("")

const submit_data = async () => {
    let response = await $fetch("/api/add_user", {
        method: "POST",
        body: {
            first_name: first_name.value,
            last_name: last_name.value,
            email: email.value,
            username: username.value,
            password: password.value,
        }
    })
    if (response.status === 200) {
        // Handle successful registration
        console.log("User registered successfully")
        route.push('/login')
        // Optionally redirect or show a success message
    } else {
        // Handle error
        console.error("Registration failed", response)
    }
    console.log(response)
}
</script>

<template>
    <div class="w-full flex justify-center pt-30">
        <form v-on:submit.prevent="submit_data" class="bg-white shadow-md rounded px-8 pb-8 mb-4">

            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="first_name">First Name</label>
                <input type="text" id="first-name" v-model="first_name"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="last_name">Last Name</label>
                <input v-model="last_name"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="last-name">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="email">Email</label>
                <input v-model="email"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="email" id="email">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
                <input v-model="username"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="username">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
                <input v-model="password"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="password">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="confirm_password">Confirm
                    Passowrd</label>
                <input v-model="confirm_passowrd"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="confirm-password">
            </div>
            <div class="flex items-center justify-end mt-4">
                <button
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">Submit</button>
            </div>
        </form>
    </div>
</template>