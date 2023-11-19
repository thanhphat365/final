from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home, name='home'),
    path('sport/',views.sport),
    path('entertainment/',views.entertainment),
    path('technology/',views.technology),    
    path('health/',views.health),
    path('login/', views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('science/', views.science),
    path('business/', views.business),
    path('about/', views.about),
    path ('create_blog/', views.create_blog),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('<int:post_id>/<str:author>/',views.comment_view,name='comment'),
]
