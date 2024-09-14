from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("<int:id>/<str:title>/", views.post_detail, name="post_detail"),
    path('serialiaze/',views.serialiaze_m,name = 'ser'),
    path('login_page/',views.login_a,name='login_page'),
    path('logout/',views.logout_a,name='logout'),
    path('Changepassword/',views.changepassword,name='Changepassword'),
    path('<str:tag_slug>/',views.index,name = "index_tag"),
]
