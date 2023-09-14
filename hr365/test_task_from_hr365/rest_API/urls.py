from django.urls import path

from .views import ConvertAPIView

app_name = 'rest_api'

urlpatterns = [
    path('rates', ConvertAPIView.as_view(), name='convert')
]