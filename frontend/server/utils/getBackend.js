
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
    const csrfToken = getCookie(event, "csrfToken")
    const option = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
            'Authorization': `Bearer ${authToken}`,
            'Cookie': `authorizationToken=${authToken}`
        }
    }
    console.log("getBackend options", option)
    return new Backend(option)
}