import json
from models import CelestialBodies, Landmark
from app import db

def test_it_can_return_all_landmarks_a_celestial_body(app):
  mercury = CelestialBodies(name='Mercury',
                    image='https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg',
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
  resp = client.get('/api/v1/celestial_bodies/1/landmarks')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert len(data['data']) == 2
  assert (data['data'][0]['id']) == caloris.id
  assert (data['data'][0]['name']) == caloris.name
  assert (data['data'][0]['image']) == caloris.image
  assert (data['data'][0]['landmark_type']) == caloris.landmark_type
  assert (data['data'][0]['description']) == caloris.description
  assert (data['data'][0]['celestial_body_id']) == caloris.celestial_body_id

def test_it_can_return_proper_sad_path_and_status_when_no_landmarks_exist(app):
  mercury = CelestialBodies(name='Mercury',
                    image='https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg',
                    celestial_body_type='Planet',
                    gravity=0.37,
                    planet_day=58.65,
                    planet_year=87.96)
  db.session.add(mercury)
  db.session.commit()

  client = app.test_client()
  resp = client.get('/api/v1/celestial_bodies/1/landmarks')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert (data['data']) == 'No landmarks found for celestial_body id: 1.'

def test_it_returns_404_when_no_celestial_body(app):
  client = app.test_client()
  resp = client.get('/api/v1/celestial_bodies/4/landmarks')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 404
  assert (data['errors']) == 'No celestial_body with id: 1'