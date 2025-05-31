### Objectives

Build a Personalized News Aggregator Application that allows users to

- ​[x] Register and securely log in.​
- ​[x] Receive a tailored news feed based on individual preferences.​
- ​[x] Customize news settings: country, sources, and keywords.​
- ​[x] Browse, search, and filter their news feed.​
  - [x] Filter by source
  - [x] Filter by publication date
  - [x] keyword search in title or summary
- ​[x] Access original articles via source links.​

### News retrieval and Storage

- [x] schedule background task every 10 minutes
- [x] fetch the best articles from NewsAPI.org based on user's preference
- [x] store matching articles in the database linked to each user
- [x] prevent duplicate storage using uniqueness constraints
