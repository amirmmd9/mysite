from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('<str:slug>/<int:id>/',views.detailes,name="detailes"),
    path('<str:slug>/<int:id>/<str:name>/',views.khedmat,name="khedmat"),
    path('about_page/',views.about,name="about_page"),
    path('rezome/',views.rezome,name="rezome"),
    path('maghale/',views.maghale,name="maghale"),
    path('maghale/<str:slug>/<int:id>/<str:name>/',views.maghale_detail,name="maghale_detail"),
    path('blog/login/',views.log_in_and_join,name="login_view"),
    path('blog/logout/',views.logout_view,name="logout_view"),
    path('blog/changepassword/',views.changpassword,name="changpassword")

]