# from CampusDigital.store.views.addform import free_notes
from django.urls import path
from .views import Home,Signup,Login,logout,Cart,Checkout,OrderView
from .middlewares import LoginCheckMiddleware,LogoutCheckMiddleware
from store.views.home import search
from store.views.addform import Notes_Create
from store.views.addform import free_notes
# from store.views.addform import UpdateNotesView


urlpatterns = [
    path('',Home.as_view(), name='home1'),
    path('signup/',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
    path('search', search, name='search'),
    path('notes_create', Notes_Create,name='Notes'),

    path('free_notes', free_notes,name='FreeNotes'),
    # path('notesupdate/edit/<int:pk>', UpdateNotesView, name='update_notes'),  
  
]