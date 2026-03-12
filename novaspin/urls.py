from django.urls import path, include

urlpatters = [
    path('', include('casino.urls')),
]