import json
from models import CelestialBodies, Landmark
from app import db

def test_it_can_return_an_individual_landmark(app):
  mercury = CelestialBodies(name='Mercury',
                    image='https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg',
                    background_image='https://www.howitworksdaily.com/wp-content/uploads/2138184.jpg',
                    celestial_body_type='Planet',
                    gravity=0.37,
                    planet_day=58.65,
                    planet_year=87.96)
  db.session.add(mercury)

  caloris = Landmark(name="Caloris Basin",
                       image="https://cdn.britannica.com/75/145475-050-916827A9/Caloris-Basin-Mercury-spacecraft-Messenger-2008.jpg",
                       landmark_type="Crater",
                       description="The Caloris basin is one of the largest impact craters in the Solar System, measuring at over 900 miles wide. The asteroid that created the impact was likely at least 60 miles wide, larger than the one theorized to have caused the dinosaurs' extinction. The impact was so violent that it caused deformations in the terrain on the exact opposite side of the planet (the antipode).",
                       celestial_body_id=1)

  mercury_pole = Landmark(name="Poles",
                          image="https://api.hub.jhu.edu/factory/sites/default/files/styles/hub_medium/public/mercury_ice.jpg?itok=1baACeWG",
                          landmark_type="Structure",
                          description="Despite being the planet closest to the sun, Mercury can get quite cold. At the poles of the planet, hidden perpetually from the sun in the shadows of craters, there's ample evidence that there is large amounts of ice lying frozen. Though a fraction of what exists on Earth's polar regions, it is still enough to be at least a couple miles deep.",
                          celestial_body_id=1)
    
  db.session.add(caloris)
  db.session.add(mercury_pole)
  db.session.commit()

  client = app.test_client()
  resp = client.get('/api/v1/landmarks/1')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert (data['id']) == caloris.id
  assert (data['name']) == caloris.name
  assert (data['image']) == caloris.image
  assert (data['landmark_type']) == caloris.landmark_type
  assert (data['description']) == caloris.description
  assert (data['celestial_body_id']) == caloris.celestial_body_id

def test_it_responds_with_404_when_landmark_id_does_not_exist(app):
  client = app.test_client()
  resp = client.get('/api/v1/landmarks/1')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 404
  assert (data['errors']) == 'No landmark found with id: 1.'