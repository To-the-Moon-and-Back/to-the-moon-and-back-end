import json

def test_news(app):
  client = app.test_client()
  resp = client.get('/api/v1/news')
  data = data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert (data['docs'][0]['featured_image'])
  assert (data['docs'][0]['title'])