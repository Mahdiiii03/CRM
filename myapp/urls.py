from django.urls import path
from .views import home_view, login_view, logout_view, signup_view, record_view, delete_view, edit_view, add_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('record/<int:pk>', record_view, name='record'),
    path('delete/<int:pk>', delete_view, name='delete'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('add/', add_view, name='add'),
]
