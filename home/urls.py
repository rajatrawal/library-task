
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'genre', views.GenreAPI, basename='genre')
router.register(r'book', views.BookAPI, basename='book')
# router.register(r'author', views.AutherList, basename='genre')

urlpatterns = [
    path('', views.home, name='home'),
    path('api/authors', views.AuthorList.as_view(), name='author_list'),
    path('api/author/<int:pk>', views.AuthorDetail.as_view(), name='author_detail'),
    path('api/author/create', views.AuthorCreate.as_view(), name='author_create'),
    path('api/login', views.LoginView.as_view(), name ='login'),
    path('export/<str:genre>', views.export_data, name ='export'),
    path('api/', include(router.urls)),
]

