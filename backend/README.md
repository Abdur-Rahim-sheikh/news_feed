### Objectives

Build a Personalized News Aggregator Application that allows users to

- ​[ ] Register and securely log in.​
- ​[ ] Receive a tailored news feed based on individual preferences.​
- ​[ ] Customize news settings: country, sources, and keywords.​
- ​[ ] Browse, search, and filter their news feed.​
  - [ ] Filter by source
  - [ ] Filter by publication date
  - [ ] keywords in title or summary
- ​[ ] Access original articles via source links.​

### News retrieval and Storage

- [x] schedule background task every 10 minutes
- [x] fetch the best articles from NewsAPI.org based on user's preference
- [x] store matching articles in the database linked to each user
- [x] prevent duplicate storage using uniqueness constraints
