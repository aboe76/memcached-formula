import requests


def test_server(host_ip, http_port):
    resp = requests.get('http://{0}:{1}'.format(host_ip, http_port), headers={'Host': '127.0.0.1'})
    assert resp.status_code == 200
