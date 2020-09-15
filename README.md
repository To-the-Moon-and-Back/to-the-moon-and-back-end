# To the Moon and Backend 

This is the final project at Turing School of Software and Design in Denver, CO. It is the backend portion of a service-oriented architecture. Working directly with a front end team, we were provided a detailed wireframe and a list of expected responses. We built an API that consumes multiple external APIs to gather and format that data required. 
Stack: Python3, Flask, Postgres, Heroku 

# Endpoints 

```GET ‘https://moon-back-end.herokuapp.com/api/v1/news’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/news’```

```
{
"docs": [
  {
      "_id": "5f60e35096c53b1fb52b980e",
      "categories": [],
      "date_added": 1599983562,
      "date_published": 1600184411,
      "events": [],
      "featured": false,
      "featured_image": "https://cdn.arstechnica.net/wp-content/uploads/2020/09/tropics-800x505.jpg",
      "id": "",
      "imported_date": "2020-09-13T07:52:42.498Z",
      "launches": [],
      "ll": [],
      "news_site": "arstechnica",
      "news_site_long": "Arstechnica",
      "published_date": "2020-09-15T15:40:11.000Z",
      "tags": [],
      "title": "Hurricane Sally will bring devastating floods to the Southern United States",
      "url": "https://arstechnica.com/science/2020/09/hurricane-sally-will-bring-devastating-floods-to-the-southern-united-states/"
  },...

```
