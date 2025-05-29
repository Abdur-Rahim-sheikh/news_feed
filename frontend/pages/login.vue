<script setup>
definePageMeta({
    title: "Register",
    layout: "auth",
})
const router = useRouter()
let unifier = ref("")
let password = ref("")
let form_ok = ref(true)
const submit_data = async () => {
    form_ok.value = true
    let response = await $fetch("/api/login", {
        method: "POST",
        body: {
            unifier: unifier.value,
            password: password.value,
        }
    })
    console.log("login response: ", response)
    if (response.status === 'success') {
        // Handle successful registration
        console.log("User is valid")
        router.push('/')
        // Optionally redirect or show a success message
    } else {
        // Handle error
        form_ok.value = false
        console.error("authentication failed", response)
    }
    console.log(response)
}
</script>

<template>
    <div class="w-full flex justify-center pt-30">
        <form v-on:submit.prevent="submit_data" class="bg-white shadow-md rounded px-8 pb-8 mb-4"
            :class="{ 'border border-red-500': !form_ok }">


            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Id</label>
                <input v-model.strip="unifier" placeholder="Username / Email"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text" id="unifier">
            </div>
            <div class="mt-2">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
                <input v-model.strip="password" placeholder="Password"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="password" id="password">
            </div>

            <div class="flex items-center justify-end mt-4">
                <button
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">Submit</button>
            </div>
        </form>
    </div>
</template>