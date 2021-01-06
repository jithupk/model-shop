from django.urls import path
from .import views

urlpatterns = [
    path('', views.productListView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
    path('add/', views.add, name="additem"),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='delete')
    
]

