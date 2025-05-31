<script setup>
definePageMeta({
    title: "Register",
    layout: "auth",
})
const router = useRouter()
let first_name = ref("")
let last_name = ref("")
let email = ref("")
let username = ref("")
let password = ref("")
let confirm_passowrd = ref("")
let form_ok = ref(true)
let password_ok = ref(true)
const submit_data = async () => {
    form_ok.value = true
    password_ok.value = true
    if (password.value.length < 5 || password.value !== confirm_passowrd.value) {
        password_ok.value = false
        return
    }
    let response = await $fetch("/api/register", {
        method: "POST",
        body: {
            first_name: first_name.value,
            last_name: last_name.value,
            email: email.value,
            username: username.value,
            password: password.value,
        }
    })
    console.log("add_user response: ", response)
    if (response.status === 'success') {

        console.log("User registered successfully")
        router.replace('/login')
    } else {
        form_ok.value = false
        console.error("Registration failed", response)
    }
    console.log(response)
}
</script>

<template>
    <div class="w-full flex justify-center pt-30">
        <form v-on:submit.prevent="submit_data" class="bg-white shadow-md rounded px-8 pb-8 mb-4"
            :class="{ 'border border-red-500': !form_ok }">

            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="first_name">First Name</label>
                <input type="text" id="first-name" v-model.strip="first_name" placeholder="First Name"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="last_name">Last Name</label>
                <input v-model.strip="last_name" placeholder="Last Name"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="last-name">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="email">Email</label>
                <input v-model.strip="email" placeholder="Email"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="email" id="email">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
                <input v-model.strip="username" placeholder="Username"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="username">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
                <input v-model.strip="password" placeholder="Password"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="password">
                <span v-if="!password_ok" class="text-red-400 block">At least length 5</span>
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="confirm_password">Confirm
                    Passowrd</label>
                <input v-model.strip="confirm_passowrd" placeholder="Confirm Password"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="confirm-password">
                <span v-if="!password_ok" class="block text-red-400">Both password should match</span>
            </div>
            <div class="flex items-center justify-end mt-4">
                <button
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">Submit</button>
            </div>
        </form>
    </div>
</template>