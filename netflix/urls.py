
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPIView.as_view()),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('izohlar/', IzohlarAPIView.as_view()),
    path('kinolar/', KinolarAPIView.as_view()),
    path('aktyor/<int:pk>/', AktyorAPIView.as_view()),
    path('izoh/<int:pk>/', IzohAPIView.as_view()),
    path('aktyor_ochir/<int:pk>/', AktyorOchirAPIView.as_view()),
    path('kino_detal/<int:pk>/', KinoDetalView.as_view()),
]
