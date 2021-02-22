from django.urls import path

import rubricas.views.homes as homes

urlpatterns = [
    path("home/", homes.home, name="home"),
    ]
