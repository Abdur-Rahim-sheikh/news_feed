export default defineEventHandler(async (event) => {
    let backend = getBackend(event)
    let data = await readBody(event)
    console.log("login", data)
    try {
        await backend.request('/v1/login', {
            method: "POST",
            body: {
                unifier: data.unifier,
                password: data.password
            }
        })
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