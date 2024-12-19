from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('logout-user/', views.logout, name="logout_user"),
    path('add-record/', views.add_record, name='add_record'),
    path('update-record/<int:pk>', views.update_record, name="update_record"),
    path('delete-record/<int:pk>/', views.delete_record, name="delete_record"),
    path('search/', views.search, name="search"),
]
