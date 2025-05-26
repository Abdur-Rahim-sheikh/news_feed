let server_url = process.env.SERVER_URL

export default defineEventHandler(async (event, url, method) => {

    console.debug(`Backend URL: ${server_url}`)
    const fullUrl = new URL(url, server_url).toString()
    console.debug(`Fetching from backend: ${fullUrl}`)
    return await $fetch(fullUrl, {
        method: method,
        ...event
    })

})