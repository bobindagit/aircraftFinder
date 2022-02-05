from django.urls import include, path
from . import views

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.index),
    path('details/aircraft_id=<str:aircraft_id>', views.details),
]