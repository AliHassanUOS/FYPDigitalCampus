from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import Home,Signup,Login,logout,Cart,Checkout,OrderView
from django.test import TestCase

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))

    def test_singup(self):
        url = reverse('signup')
        print(resolve(url))
       
    def test_login(self):
        url = reverse('login')
        print(resolve(url))
    
    def test_logout(self):
        url = reverse('logout')
        print(resolve(url))
    
    def test_checkout(self):
        url = reverse('checkout')
        print(resolve(url))

    def test_checkout(self):
        url = reverse('checkout')
        print(resolve(url))
    
    def test_order(self):
        url = reverse('order')
        print(resolve(url))

    def test_search(self):
        url = reverse('search')
        print(resolve(url))
    

    def test_notes(self):
        url = reverse('Notes')
        print(resolve(url))









