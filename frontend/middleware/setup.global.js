export default defineNuxtRouteMiddleware((to, from) => {
    const user = useCookie('user')
    if (to.path === '/login' || to.path === '/register') {
        return
    }
    else if (!user.value) return navigateTo('/login')
})