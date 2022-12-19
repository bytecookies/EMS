
import pprint
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter


from . import views


router= SimpleRouter()
router.register('exhibitors', views.ExhibitorViewSet)
router.register('visitors', views.VisitorViewSet)
router.register('visitor/register',views.VisitorCreate)
router.register('visitor/profile',views.VisitorProfileViewSet)

pprint.pprint(router.urls)

urlpatterns = [
    path('', views.index, name='api_home'),
    # path('visitors/', views.VisitorList.as_view()),
    path('exhibitor/',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('',include(router.urls)),
    
    

]
