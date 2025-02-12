from django.urls import path,include 
from .views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, AchievementViewSet, ContactFormViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'contact-forms', ContactFormViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]


