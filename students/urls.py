from django.urls import path
from .views import StudentListCreateView, StudentDetailView

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('student/<int:id>/', StudentDetailView.as_view()),
]