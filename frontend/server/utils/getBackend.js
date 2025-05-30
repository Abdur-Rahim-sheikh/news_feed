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
    const authToken = getCookie(event, "auth_token")
    const csrfToken = getCookie(event, "csrfToken")
    const option = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
            'Authorization': `Bearer ${authToken}`,
            'Cookie': `authorizationToken=${authToken}`
        }
    }

    return new Backend(option)
}