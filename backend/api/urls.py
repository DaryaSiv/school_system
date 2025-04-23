from django.urls import path
from .views import RegisterView, get_user_info, TeacherProfileView, LessonCreateAPIView, LessonListAPIView, LessonDetailAPIView, LessonDeleteAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', get_user_info),
    path('teacher/profile/', TeacherProfileView.as_view(), name='teacher-profile'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson-delete'),
]
