import pytest
from django.urls import reverse
from django.core.management import call_command

@pytest.mark.django_db
def test_get_products_list(api_client):
    call_command('loaddata', 'fixtures.json')
    url = '/api/products/'

    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    results = data.get('results', data)
    assert len(results) == 3
