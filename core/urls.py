
from django.urls import path


from . import views
# from .views import AllKeywordsView

urlpatterns = [
    path('', views.index, name='home'),
    path('exhibitor/', views.exhibitor_dashboard, name='exhibitor_dashboard'),

    # just leave these two above urls dont change

    path('exhibitor/participation_form/', views.participation_form,
         name='participation_form'),

    path('exhibitor/stall_aminities/', views.stall_aminities,
         name='stall_aminities'),

    path('exhibitor/move_in_move_out/', views.move_in_move_out,
         name='move_in_move_out'),
    path('exhibitor/key_contacts/', views.key_contacts,
         name='key_contacts'),

    path('exhibitor/rules_and_regulations/', views.rules_and_regulations,
         name='rules_and_regulations'),

    path('exhibitor/venders/', views.venders,
         name='venders'),

    path('exhibitor/show_info/', views.show_info,
         name='show_info'),
         
    path('exhibitor/exhibitor_downloads/', views.exhibitor_downloads,
         name='exhibitor_downloads'),
   
    path('exhibitor/static_downloads/', views.exhibitor_static_downloads,
         name='exhibitor_static_downloads'),
    
    path('exhibitor/event_promotion_download/', views.event_promotion_download,
         name='event_promotion_download'),
    path('exhibitor/floor_plan/', views.floor_plan,
         name='floor_plan'),

    path('login/', views.loginview,
         name='login'),

     # Visitors urls
    path('registration/', views.visitors_registration,
         name='visitors_registration'),

    path('visitor/', views.visitor_dashboard,
         name='visitor_dashboard'),

   
    path('visitor/exhibitors', views.exhibitor_list,
         name='exhibitor_list'),
    
    path('visitor/exhibitors/<int:pk>', views.exhibitor_detail,
         name='exhibitor_detail'),







    path('test/', views.test,
         name='test'),

    path('product_sub_catagories/', views.get_product_sub_catagory_ajax,
         name='product_sub_catagories_Ajax'),


    path('logout_view', views.logout_view, name="logout_view"),

    path('change_password', views.change_password, name="change_password"),

]
