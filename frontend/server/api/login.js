import getBackend from "../utils/getBackend";


export default defineEventHandler(async (event) => {
    let backend = getBackend(event)
    let data = await readBody(event)
    console.log("login data:", data)
    try {
        let response = await backend.request('/v1/login', {
            method: "POST",
            body: {
                unifier: data.unifier,
                password: data.password
            }
        })
        data = response._data
        console.log("login response found", data.auth_token, data.user)
        setCookie(event, "auth_token", data.auth_token)
        setCookie(event, "tokenExpiresAt", data.token_expires_at)
        setCookie(event, "user", JSON.stringify(data.user))
        return {
            success: true,
            statusMessage: "User is authenticated",
        }
    } catch (error) {
        console.error("login error: ", error)
        return {
            success: false,
            message: error.message
        }
    }



})