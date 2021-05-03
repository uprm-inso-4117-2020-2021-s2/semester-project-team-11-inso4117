from django.urls import path

from . import views

urlpatterns = [
    path("registerLawyer", views.registerLawyer,name='registerLawyer'),
    path("registerClient",views.registerClient,name='registerClient'),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout')
]