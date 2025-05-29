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
    <form v-on:submit.prevent="submit_data">
        <div>
            <div>
                <label for="first_name">First Name</label>
                <input type="text" id="first-name" v-model="first_name">
            </div>
            <div>
                <label for="last_name">Last Name</label>
                <input v-model="last_name" type="text" id="last-name">
            </div>
            <div>
                <label for="email">Email</label>
                <input v-model="email" type="email" id="email">
            </div>
            <div>
                <label for="username">Username</label>
                <input v-model="username" type="text" id="username">
            </div>
            <div>
                <label for="password">Password</label>
                <input v-model="password" type="password" id="password">
            </div>
            <div>
                <label for="confirm_password">Confirm Passowrd</label>
                <input v-model="confirm_passowrd" type="password" id="confirm-password">
            </div>
            <button>Submit</button>
        </div>
    </form>
</template>