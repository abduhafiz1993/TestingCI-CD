from django.urls import path

from . import views

app_name 'flights'

urlpatterns = [
    path("", views.index, name = "index")
    path("", views.flight, name = "flight")
    path("", views.book, name = "book")
]