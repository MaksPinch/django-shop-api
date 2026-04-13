import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

@pytest.mark.django_db
class TestCart:

    @pytest.fixture(autouse=True)
    def setup_data(self):
        call_command('loaddata', 'fixtures.json')

    def test_get_cart(self, api_client):
        user = User.objects.get(username="maksim")
        api_client.force_authenticate(user=user)

        response = api_client.get('/api/cart/')

        assert response.status_code == 200
        assert len(response.data['cart_items']) == 2
        assert float(response.data['cart_sum']) == 699.0

    def test_add_to_cart(self, api_client):
        user = User.objects.get(username="maksim")
        api_client.force_authenticate(user=user)
        payload = {"product_id": 2, "quantity": 1}

        response = api_client.post('/api/cart/', payload)

        assert response.status_code == 200
        assert response.data == 'Успешно добавлено'
