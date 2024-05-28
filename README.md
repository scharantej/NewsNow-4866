## Flask Application Design for Displaying Recent News Articles ##

### HTML Files

- **index.html:**
Serves as the homepage of the application. Contains a title and a section to display news articles.
- **news.html:**
Provides a detailed view of an individual news article, including its title, publication date, author, and content.

### Routes

- **`/`:**
Function that handles the homepage. Renders the `index.html` template with a list of recent news articles.
- **`/news/<article_id>`:**
Function that handles displaying an individual news article. Queries the database to retrieve the article details and renders the `news.html` template with the retrieved data.