from urllib import response
import pytest
import requests

@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    response = requests.get(url)
    body = response.json()

    assert response.status_code == 200
    assert 'Python' in body['AbstractText']