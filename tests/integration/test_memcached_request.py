import requests


def test_server(server, port):
    resp = requests.get('http://{0}:{1}'.format(server, port), headers={'Host': '127.0.0.1'})
    assert resp.status_code == 200
