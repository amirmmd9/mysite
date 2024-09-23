from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("<int:id>/<str:title>/", views.post_detail, name="post_detail"),
    path('serialiaze/',views.serialiaze_m,name = 'ser'),
    path('cbv/',views.Api_dl.as_view()),
    path('logup_page/',views.logup_m,name='logup'),
    path('login_page/',views.login_a,name='login_page'),
    path('logout/',views.logout_a,name='logout'),
    path('Changepassword/',views.changepassword,name='Changepassword'),
    path('<str:tag_slug>/',views.index,name = "index_tag"),
    path('point_gap/profile/',views.profile,name='prof'),
    path('point_gap/addpost/',views.addpost,name='addpost'),
]
