from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>/<str:title>/',views.detail,name="detail"),
]
