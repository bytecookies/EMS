
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),

    # just leave these two above urls dont change

    path('participation_form/', views.participation_form,
         name='participation_form'),

    path('stall_aminities/', views.stall_aminities,
         name='stall_aminities'),
    path('rules_and_regulations/', views.rules_and_regulations,
         name='rules_and_regulations'),

    path('login/', views.loginview,
         name='login'),

    path('logout_view', views.logout_view, name="logout_view"),

]
