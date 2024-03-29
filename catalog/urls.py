from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, contacts, ProductDetailView, ProductCreateView, BlogsListView, \
    BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, ProductUpdateView, ProductDeleteView, \
    VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('blog/', BlogsListView.as_view(), name='blogs'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('product/version/<int:pk>', VersionCreateView.as_view(), name='version'),
]
