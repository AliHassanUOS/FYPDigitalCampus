from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import  PostList , post_detail

class TestUrls(SimpleTestCase):

    
    # def test_Post_Detail_test(self):
    #     url = reverse('post_detail', args= ['some-slug'])
    #     # print(resolve(url))
    #     self.assertEquals(resolve(url).func, post_detail)

    def test_Post_Detail_test(self):
        url = reverse('home')
        print(resolve(url))
        # self.assertEquals(resolve(url).func.view_class, PostList)