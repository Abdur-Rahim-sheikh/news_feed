import getBackend from "../utils/getBackend";

export default defineEventHandler(async (event) => {
    const backend = getBackend(event)
    const response = await backend.request("/v1/sources", { method: 'GET' })
    const data = response._data
    return data.sources
});