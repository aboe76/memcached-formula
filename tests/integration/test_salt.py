def test_memcached_is_installed(host):
    memcached = host.package("memcached")
    assert memcached.is_installed

def test_memcached_running_and_enabled(host):
    memcached = host.service("memcached")
    assert memcached.is_running
