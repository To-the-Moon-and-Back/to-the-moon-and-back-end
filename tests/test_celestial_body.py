import json
from models import CelestialBodies
from app import db

def test_it_can_return_one_celestial_body(app):
  mercury = CelestialBodies(name='Mercury',
                    image='https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg',
                    celestial_body_type='Planet',
                    gravity=0.37,
                    planet_day=58.65,
                    planet_year=87.96)

  venus = CelestialBodies(name='Venus',
                    image="https://astronomy.com/-/media/Images/News%20and%20Observing/News/2020/04/Venus1__1_.jpg?mw=600",
                    celestial_body_type='Planet',
                    gravity=0.90,
                    planet_day=243.02,
                    planet_year=224.70)

  db.session.add(mercury)
  db.session.add(venus)
  db.session.commit()

  client = app.test_client()
  resp = client.get('/api/v1/celestial_bodies/1')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert (data['name']) == 'Mercury'
  assert (data['celestial_body_type']) == mercury.celestial_body_type
  assert (data['image']) == mercury.image
  assert (data['gravity']) == mercury.gravity
  assert (data['planet_day']) == mercury.planet_day
  assert (data['planet_year']) == mercury.planet_year
  assert (data['travel']) == mercury.travel_time()

def test_it_returns_sad_path_when_id_does_not_exist(app):
  mercury = CelestialBodies(name='Mercury',
                    image='https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg',
                    celestial_body_type='Planet',
                    gravity=0.37,
                    planet_day=58.65,
                    planet_year=87.96)
  db.session.add(mercury)
  db.session.commit()

  client = app.test_client()
  resp = client.get('/api/v1/celestial_bodies/4')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 404
  assert (data['errors']) == 'No object found with id: 4.'



