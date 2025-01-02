import pytest
from django.urls import reverse
from cursodjango.django_assertions import assert_contains


# Create your tests here.
@pytest.fixture
def resp(client):
    resp = client.get(reverse('vpreview:video', args=('preview',)))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, '<h1>Preview do Curso de Python e Django:</h1>')


def test_video_contains(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/1043031414')
