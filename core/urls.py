
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

    path('move_in_move_out/', views.move_in_move_out,
         name='move_in_move_out'),
    path('key_contacts/', views.key_contacts,
         name='key_contacts'),

    path('rules_and_regulations/', views.rules_and_regulations,
         name='rules_and_regulations'),

    path('venders/', views.venders,
         name='venders'),

    path('show_info/', views.show_info,
         name='show_info'),
         
    path('exhibitor_downloads/', views.exhibitor_downloads,
         name='exhibitor_downloads'),
   
    path('static_downloads/', views.exhibitor_static_downloads,
         name='exhibitor_static_downloads'),

    path('login/', views.loginview,
         name='login'),

     # Visitors urls
    path('registration/', views.visitors_registration,
         name='visitors_registration'),







    path('test/', views.test,
         name='test'),




    path('product_sub_catagories/', views.get_product_sub_catagory_ajax,
         name='product_sub_catagories_Ajax'),


    path('logout_view', views.logout_view, name="logout_view"),
    path('change_password', views.change_password, name="change_password"),

]
