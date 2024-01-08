from django.urls import path
from authsys import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('Login/', views.handleLogin, name='Login'),
    path('Logout/', views.handleLogout, name='Logout'),
    # path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(), name='activate')

 
    
]