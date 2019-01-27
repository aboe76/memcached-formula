from pymemcache.client.base import Client

def test_server(server, port):
    client = Client((server,port))
    client.set('some_key', 'some_value')
    result = client.get('some_key')
    assert result == 'some_value'

