<script setup>
const tokenExpiresAt = useCookie('tokenExpiresAt')
const signOut = async () => {
    useCookie('user').value = null
    let router = useRouter()
    router.push("/login")
}
const checkTokenExpired = () => {
    const now = Date.now(Date.UTC)
    const expires_at = parseInt(tokenExpiresAt.value)
    const left = expires_at - now
    console.log("left time in seconds", left / 1000)
    if (left > 0) {
        setTimeout(signOut, left)
    } else {
        signOut()
    }
}

onMounted(() => {
    checkTokenExpired()
})
</script>

<template>
    <div>
        <LayoutNavbar />
        <p>
            <slot />
        </p>
    </div>
</template>