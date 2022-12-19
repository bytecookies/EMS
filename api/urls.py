
import pprint
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter


from . import views


router= SimpleRouter()
router.register('exhibitors', views.ExhibitorViewSet)
router.register('visitors', views.VisitorViewSet)
router.register('visitor/register',views.VisitorCreate)
router.register('visitor/profile',views.VisitorProfileViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# pprint.pprint(router.urls)

urlpatterns = [
    path('', views.index, name='api_home'),
    # path('visitors/', views.VisitorList.as_view()),
    path('exhibitor/',include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
    path('',include(router.urls)),

]
