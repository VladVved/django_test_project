from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.news_list, name="news_list"),
    path('single/<int:pk>', views.new_single, name="new_single"),
    path('filter/<int:pk>', views.news_filter, name="news_filter"),
    path('../accounts/login', views.sign_up, name = "sign_up"),
]