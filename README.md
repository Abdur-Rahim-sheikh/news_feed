### An app to show personalized news for each user

#### Instructions to run

For project simplicity, I have dockerized the whole project.
So to run the project you need docker.

1. clone the repo

```bash
git clone https://github.com/Abdur-Rahim-sheikh/news_feed.git
```

2. Open terminal here

```bash
cd news_feed
```

3. create dot env file in both `frontend` and `backend` provide due credentials.
4. Run any of the below command from root directory
   ```bash
       docker compose up
   ```
   or
   ```
        make run
   ```

### .env setup

#### example frontend env setup

SERVER_URL=http://backend:8000
DEBUG=true

#### example backend env setup

1. POSTGRES_PASSWORD=pass123$
2. POSTGRES_USER=postgres
3. POSTGRES_HOST=db

4. NEWS_API=your newsapi.org api
5. CORS_ALLOWED_ORIGINS=http://localhost:3000
6. ALLOWED_HOST=http://backend:8000,http://localhost:8000

7. JWT_SECRET=secret_news
8. JWT_ALGORITHM=HS256
