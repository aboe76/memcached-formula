def test_memcached_is_installed(host):
    memcached = host.package("memcached")
    assert memcached.is_installed

def test_memcached_running_and_enabled(host):
    memcached = host.service("memcached")
    assert memcached.is_running
    assert memcached.is_enabled

def test_memached_is_listening(host):
    memcached = host.socket("tcp://11211")
    assert memcached.is_listening

