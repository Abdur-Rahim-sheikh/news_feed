import getBackend from "../utils/getBackend";
import getDate from "../utils/getDate";

export default defineEventHandler(async (event) => {
    const query = getQuery(event)
    console.debug("query", query)
    const backend = getBackend(event)

    let url = `v1/news?fromDate=${query.fromDate}&toDate=${query.toDate}&keyword=${query.keyword}&sourceId=${query.sourceId}`

    try {
        let response = await backend.request(url, { method: 'GET' })

        let data = response.articles.map(article => ({
            source_url: article.news_url,
            source_name: article.source_name,
            title: article.title,
            summary: article.summary,
            thumbnail_url: article.thumbnail_url,
            published_at: getDate(article.published_at),
        }));
        console.log("Fetched news data:", data.length);
        return data
    } catch (error) {
        console.error("Error fetching news:", error);
        throw createError({
            statusCode: 500,
            statusMessage: 'Internal Server Error',
            message: 'Failed to fetch news data'
        });
    }
})