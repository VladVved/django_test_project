from . import views
from django.urls import path

urlpatterns = [
    #path("", views.MyViews.as_view()),
    path("add-ticket/", views.AddTicket.as_view(), name='add-ticket'),
    path("list-ticket/", views.ListTicket.as_view(), name= 'list-ticket'),
    path("update-ticket/<int:pk>", views.UpdateTicket.as_view(),name = 'update-ticket')
]