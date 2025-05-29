export default defineEventHandler(async (event) => {
    let backend = getBackend(event)
    let data = await readBody(event)
    console.log("add-user", data)
    try {
        const response = await backend.request('/v1/user', {
            method: "POST",
            body: {
                first_name: data.first_name,
                last_name: data.last_name,
                username: data.username,
                email: data.email,
                password: data.password
            }
        })
    } catch (error) {
        console.log(error)
        return "not registered"
    }
    return "registered"
})