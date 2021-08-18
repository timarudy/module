from django.urls import path
from .views import MainPage, Login, Register, Logout, Items, ItemsListView, ItemsUpdateView


urlpatterns = [
    path('', MainPage.as_view(), name='mainpage'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('items/add/', Items.as_view(), name='add_item'),
    path('items/', ItemsListView.as_view(), name='items'),
    path('items/update/<slug:pk>/', ItemsUpdateView.as_view(), name='update_item'),
]