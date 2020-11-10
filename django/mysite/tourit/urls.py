from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'tourit'
urlpatterns = [
    path('', views.home, name= 'home' ),
    path('login/', views.loginPage, name= 'login' ),
    path('register/', views.registerPage, name= 'register' ),
    path('list/<int:pk>/', views.ListPage, name= 'list' ),
    path('detail/<int:pk>/', views.DetailPage.as_view(), name = 'detail'),
    path('mytrips/', views.MyTrips, name = 'trip'),
    path('add-to-trip/<int:item_id>/', views.add_to_trip, name='add_to_trip'),
    path('delete/<int:item_id>', views.delete_from_cart, name='delete_item'),


    path('dashboard/', views.dashboardPage, name= 'dashboard' ),
     #admin only page
    path('logout/', views.logoutUser, name= 'logout' ),

    path('user/', views.UserPage, name= 'user' ),
    path('user/profile/', views.accountSettings, name='account'),




]
