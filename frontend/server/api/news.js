import getDate from "../utils/getDate";

export default defineEventHandler(async (event) => {
    console.debug("Fetching news data...");
    try {
        let response = await backend(event, '/v1/news')

        let data = response.articles.map(article => ({
            source_url: article.news_url,
            title: article.title,
            summary: article.summary,
            thumbnail_url: article.thumbnail_url,
            published_at: getDate(article.published_at),
        }));
        console.log("Fetched news data:", data);
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