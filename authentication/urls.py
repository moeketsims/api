from django.urls import path
from .views import RegisterView, UserDetail

urlpatterns=[
    path('register',RegisterView.as_view()),
    path('register/<int:pk>', UserDetail.as_view()),
]