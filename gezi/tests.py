from django.urls import reverse, resolve
from django.test import TestCase
from .views import index

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('gezi:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/gezi/')
        self.assertEquals(view.func, index)        