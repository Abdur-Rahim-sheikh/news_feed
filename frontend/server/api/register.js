export default defineEventHandler(async (event) => {
    let backend = getBackend(event)
    let data = await readBody(event)
    try {
        await backend.request('/v1/user', {
            method: "POST",
            body: {
                first_name: data.first_name,
                last_name: data.last_name,
                username: data.username,
                email: data.email,
                password: data.password
            }
        })
        return {
            status: "success",
            statusMessage: "User added successfully",
        }
    } catch (error) {
        console.log(error)
        return {
            status: error.status,
            message: error.message
        }
    }



})