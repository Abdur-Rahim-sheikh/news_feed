import getBackend from "../utils/getBackend"

export default defineEventHandler(async (event) => {
    const backend = getBackend(event)
    let data = await readBody(event)
    console.debug("data is consoling", data)
    try {
        const response = await backend.request('/v1/user', {
            method: 'PUT',
            body: {
                country_codes: data.selected_country_codes,
                source_ids: data.selected_source_ids,
                keywords: data.selected_keywords
            }
        })
    } catch (e) {
        return {
            success: false,
            message: e.message || 'updating failed'
        }
    }
    return {
        success: true,
        message: 'Successfully update the backend'
    }
})