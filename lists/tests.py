from django.test import TestCase
from django.urls import resolve
from django.shortcuts import render
from django.http import HttpResponse

from lists.views import home_page

class HomePageTest(TestCase):
    def teste_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
        
    def test_home_page_returns_correct_html(self):
        request = HttpResponse
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

def home_page():
    pass


class HomePage(TestCase):
    def test_root_url_resolve_to_home_page_viwe(self):
        found = resolve('/')
        self.assertEqual(found.func. home_page)
        