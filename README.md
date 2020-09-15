# To the Moon and Backend 

This is the final project at Turing School of Software and Design in Denver, CO. It is the backend portion of a service-oriented architecture. Working directly with a front end team, we were provided a detailed wireframe and a list of expected responses. We built an API that consumes multiple external APIs to gather and format that data required. 
Stack: Python3, Flask, Postgres, Heroku 

# Endpoints 

### Celestial Bodies Index Endpoint
``` GET 'https://moon-back-end.herokuapp.com/api/v1/celestial_bodies'```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies’```

```json
{
  "data": [
    {
    "celestial_body_type": "Planet",
    "gravity": 0.37,
    "id": 1,
    "image": "https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg",
    "name": "Mercury",
    "planet_day": 58.65,
    "planet_year": 87.96,
    "travel": {
        "distance": 112788522.23136441,
        "travel_time": 4544.992030599791
      }
    },
    {
      "celestial_body_type": "Planet",
      "gravity": 0.9,
      "id": 2,
      "image": "https://astronomy.com/-/media/Images/News%20and%20Observing/News/2020/04/Venus1__1_.jpg?mw=600",
      "name": "Venus",
      "planet_day": 243.02,
      "planet_year": 224.7,
      "travel": {
          "distance": 89615403.36369385,
          "travel_time": 3611.194526261035
        }
      },
    {
    "celestial_body_type": "Planet",
    "gravity": 0.38,
    "id": 3,
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSY5oCXASYgKXI1MFGmRbgs9WmSnULsnOe_fg&usqp=CAU",
    "name": "Mars",
    "planet_day": 1.02,
    "planet_year": 686.98,
    "travel": {
        "distance": 41416978.76680374,
        "travel_time": 1668.9627162638517
      }
    }, ... 
  ]
}
```

### Celestial Bodies Show Endpoint
```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/(id)’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/9’```

```json
{
    "celestial_body_type": "Star",
    "gravity": 27.95,
    "id": 9,
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRkKZ8nFulIMZAK8MKI8kzvsfGnaa3YlqMMRA&usqp=CAU",
    "name": "Sun",
    "planet_day": 25.38,
    "planet_year": null,
    "travel": {
        "distance": 93464281.86764629,
        "travel_time": 3766.29117777427
    }
}
```
### Landmarks Index Endpoint 

```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/(id)/landmarks’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/celestial_bodies/9/landmarks’```

```json
{
  "data": [
      {
          "celestial_body_id": 9,
          "description": "Deep in the sun's core is the beating heart of the entire solar system. It's hard to believe that so much is powered by a reaction on the atomic scale. Under pressure from the gravity of the sun being so massive, hydrogen atoms fuse into helium, providing the energy that lights up the entire solar system. It produces 1.8 billion times the energy of the largest nuclear bomb detonated on Earth... every single second!",
          "id": 1,
          "image": "https://cdn.mos.cms.futurecdn.net/WtnoFrpeLL37TLcjpzK5A7-970-80.jpg",
          "landmark_type": "Structure",
          "name": "Core"
      },
      {
          "celestial_body_id": 9,
          "description": "When you look up into the sky (but hopefully not directly!) the bright ball of the photosphere is the part of the sun you're looking at. Though often depicted as being yellow, the light from the sun is white. When it hits the Earth's atmosphere, a phenomenon called Rayleigh scattering causes it to look yellow, as well as the sky blue. The same phenomenon is responsible for the brilliant colors of both sunrises and sunsets.",
          "id": 2,
          "image": "https://astronomy.swin.edu.au/cms/cpg15x/albums/scaled_cache/897b42ce97bcd409a597f1392b2dd379-280x229.png",
          "landmark_type": "Structure",
          "name": "Photosphere"
      },
      {
          "celestial_body_id": 9,
          "description": "Just like the Earth, the sun also has an atmosphere. The largest part of it is known as its corona. Though it is not usually visible thanks to the brightness of the photosphere, during eclipses - when the moon's orbit puts it in the right place to block out the majority of the sun's light - it becomes readily apparent. Particles stream out of the corona to create solar wind, which is responsible for phenomena such as the auroras, and comets having tails, among others.",
          "id": 3,
          "image": "https://media.wired.com/photos/5e62e4af2ee19f000853234b/master/w_1600%2Cc_limit/photo_space_corona_1_AFRC2017-0233-006.jpg",
          "landmark_type": "Atmosphere",
          "name": "Corona"
      }, ... 
  ]
}
```
### Landmark Show Endpoint 

```GET ‘https://moon-back-end.herokuapp.com/api/v1/landmarks/(id)’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/landmarks/9’```

```json
{
  "celestial_body_id": 1,
  "description": "Named after the French composer, this crater, along with a similar one named Hakusai, are prominent enough to be detected from Earth using radio telescopes. It has a very noticeable ray pattern stretching out from the impact center, which indicates that it's relatively new. It was one of the first things photographed by the MESSENGER probe, sent to orbit the planet from 2011 to 2015.",
  "id": 9,
  "image": "https://live.staticflickr.com/6170/6176086738_3a98b804a4_b.jpg",
  "landmark_type": "Crater",
  "name": "Debussy"
}
```

### Most Recent Space News Endpoint
```GET ‘https://moon-back-end.herokuapp.com/api/v1/news’```

Example response for this request: ```GET ‘https://moon-back-end.herokuapp.com/api/v1/news’```

```json
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
  },

```



