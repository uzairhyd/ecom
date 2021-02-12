
from django.urls import path


from products.views import (
    ProductListView, 
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
]
app_name = 'search'