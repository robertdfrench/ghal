import ghal
import pytest
import json


@pytest.fixture(scope='module')
def config():
    with open("config.json") as config_file:
        return json.loads(config_file.read())


def test_ghal_says_hello():
    assert ghal.hello()


def test_connect_to_github(config):
    uri = "%s@github.com" % config['GITHUB_USERNAME']
    github = ghal.connect(uri, config['GITHUB_API_KEY'])
    assert github.healthy


@pytest.fixture(scope="module", params=["github", "gitlab"])
def githost(request):
    return request.param


def test_githost_contains_word_git(githost):
    assert githost.startswith('git')


def test_crap():
    raise Exception("bope")
