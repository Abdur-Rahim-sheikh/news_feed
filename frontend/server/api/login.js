export default defineEventHandler(async (event) => {
    let backend = getBackend(event)
    let data = await readBody(event)
    console.log("login", data)
    try {
        let response = await backend.request('/v1/login', {
            method: "POST",
            body: {
                unifier: data.unifier,
                password: data.password
            }
        })
        data = response._data
        console.log("response found", data.auth_token, data.user)
        setCookie(event, "auth_token", data.auth_token)
        setCookie(event, "user", JSON.stringify(data.user))
        let tem = getCookie(event, "user")
        console.log("auth_token cookie", getCookie(event, "auth_token"))
        console.log("user cookie", JSON.parse(tem))
        return {
            status: "success",
            statusMessage: "User is authenticated",
        }
    } catch (error) {
        console.log(error)
        return {
            status: error.status,
            message: error.message
        }
    }



})