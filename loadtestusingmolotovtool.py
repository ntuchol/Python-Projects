python -m venv venv
        source venv/bin/activate # On Linux/macOS
        venv\Scripts\activate # On Windows

pip install pytest pytest-testinfra

import pytest

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_port_80_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening

def test_index_file_content(host):
    index_file = host.file("/usr/share/nginx/html/index.html")
    assert index_file.exists
    assert index_file.contains("Welcome to nginx!")