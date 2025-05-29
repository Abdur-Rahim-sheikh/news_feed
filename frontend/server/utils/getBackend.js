
// export default defineEventHandler(async (event, url, method) => {

//     const fullUrl = new URL(url, server_url).toString()
//     console.debug(`Fetching from backend: ${fullUrl}`)
//     return await $fetch(fullUrl, {
//         ...event,
//         method: method,
//     })

// })

class Backend {
    options = {}
    baseUrl = process.env.SERVER_URL
    constructor(options) {
        this.options = options
    }

    async request(url, options) {
        return await $fetch.raw(`${this.baseUrl}${url}`, {
            ...options,
            ...this.options
        })
    }
};

export default function getBackend(event) {
    const authToken = getCookie(event, "authorizationToken")
    const option = {
        headers: {
            Authorization: `Bearer ${authToken}`,
            Cookie: `authorizationToken=${authToken}`,
        }
    }
    return new Backend(option)
}