
from django.urls import path

from .views import (
    ProductListView, 
    #ProductDetailView, 
    ProductDetailSlugView
)

urlpatterns = [
    path('', ProductListView.as_view()),
    #path('products/<int:pk>/', ProductDetailView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
]
