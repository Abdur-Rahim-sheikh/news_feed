let server_url = process.env.SERVER_URL

export default defineEventHandler(async (event, url, method) => {

    const fullUrl = new URL(url, server_url).toString()
    let params = getQuery(event)
    console.debug(`Fetching from backend: ${fullUrl}`)
    return await $fetch(fullUrl, {
        ...event,
        method: method,
    })

})