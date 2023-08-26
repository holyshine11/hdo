from django.urls import path
from .views import StationList, StationDetail

urlpatterns = [
    path('oil', StationList.as_view()),
    path('oil/<int:pk>',StationDetail.as_view()),
]
