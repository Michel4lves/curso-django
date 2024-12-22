from django.test import Client

from cursodjango.django_assertions import assert_contains


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_title(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Curso de Python e Django</title>')
