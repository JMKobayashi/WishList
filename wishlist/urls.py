from django.urls import path
from . import views

urlpatterns = [
    path('/', views.WishListView.as_view(), name='wish-list')
]