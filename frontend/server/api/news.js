
export default defineEventHandler(async (event) => {
    console.debug("Fetching news data...");
    try {
        let response = await backend(event, '/v1/news')
        let articles = await response.json();
        let data = articles.map(article => ({
            source_url: article.news_url,
            title: article.title,
            summary: article.description,
            thumbnail_url: article.thumbnail_url,
            publish_date: new Date(article.publish_date).toISOString()
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