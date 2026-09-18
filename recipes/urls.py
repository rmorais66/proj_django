from django.urls import path
from recipes.views import sobre, home, contato

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]