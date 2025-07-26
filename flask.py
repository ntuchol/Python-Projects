pip install devpi-server devpi-web
    devpi-server --host 0.0.0.0 --port 3141 --serverdir ~/.devpi/server
  devpi user -c myuser mypassword
    devpi login myuser
    devpi index -c myindex

from flask import Flask, render_template, request, redirect, url_for
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/submit', methods=['POST'])
    def submit():
        if request.method == 'POST':
            return redirect(url_for('success'))
        return render_template('index.html')
    
    @app.route('/success')
    def success():
        return "Form submitted successfully!"
    
    if __name__ == '__main__':
        app.run(debug=True)

    pip install pytest testinfra
import pytest

def test_os_release(host):
    assert host.system_info.type == "linux"
    assert host.system_info.distribution in ("ubuntu", "centos")
    assert host.system_info.release >= "20.04" if host.system_info.distribution == "ubuntu" else True

def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running and nginx.is_enabled

def test_user_exists(host):
    user = host.user("myuser")
    assert user.exists
    assert user.group == "mygroup"
    assert user.home == "/home/myuser"

container_name_or_id="my_container"

if ! docker ps --quiet --filter "name=$container_name_or_id" ; then
  echo "Container '$container_name_or_id' is not running."
  exit 1
fi

command_to_execute="ls -l /"

echo "Executing command: docker exec $container_name_or_id $command_to_execute"
docker exec $container_name_or_id $command_to_execute

exit 0
