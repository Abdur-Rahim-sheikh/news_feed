<script setup>

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
    console.log(response)
}
</script>

<template>
    <div class="w-full max-w-xs content-center justify-center">
        <form v-on:submit.prevent="submit_data" class="bg-white shadow-md rounded px-8 pb-8 mb-4">

            <div>
                <label class="block text-gray-700 text-sm font-bold mb-2" for="first_name">First Name</label>
                <input type="text" id="first-name" v-model="first_name"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div>
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-2" for="last_name">Last Name</label>
                <input v-model="last_name"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="last-name">
            </div>
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-2" for="email">Email</label>
                <input v-model="email"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="email" id="email">
            </div>
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
                <input v-model="username"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="username">
            </div>
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
                <input v-model="password"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="password">
            </div>
            <div>
                <label class="block text-gray-700 text-sm font-bold mb-2" for="confirm_password">Confirm
                    Passowrd</label>
                <input v-model="confirm_passowrd"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="confirm-password">
            </div>
            <button>Submit</button>

        </form>
    </div>
</template>