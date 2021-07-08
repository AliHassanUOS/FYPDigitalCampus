from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chat.views import  home,room,checkview,send,getMessages

class TestUrls(SimpleTestCase):

    
    def test_home_url_checl(self):
        url = reverse('home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, home)


    def test_rome_url(self):
        url = reverse('room', args=['some_slug'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, room)
        

    def test_CheckView_url(self):
        url = reverse('checkview')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, checkview)

    def test_send_url(self):
        url = reverse('send')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, send)

    def test_getmessage_url(self):
        url = reverse('getMessages', args=['some_slug' ])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, getMessages)
    
    
    
    

