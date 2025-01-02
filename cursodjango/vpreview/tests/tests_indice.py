import pytest
from django.urls import reverse
from cursodjango.django_assertions import assert_contains


# Create your tests here.
@pytest.fixture
def resp(client):
    resp = client.get(reverse('vpreview:indice'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Preview do Curso de Python e Django:',
        'Curso de Python e Django: Variáveis:'
    ],
)
def test_video_title(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'preview',
        'variaveis'
    ]
)
def test_link_title(resp, slug):
    assert_contains(resp, reverse('vpreview:video', args=(slug,)))
