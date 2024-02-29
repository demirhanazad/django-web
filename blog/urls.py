from django.urls import path
from . import views
urlpatterns=[
    path("",views.home ,name="home"),
    path("hobies", views.hobies,name="hobies"),
    path("category/<slug:yol>", views.hobies_by_categories,name="hobies_by_categories"),
    path("about", views.about,name="about"),
    path("hoby/<slug:yol>-<int:id>", views.hobydetails,name="hoby_detail"),
    path('upload_hoby', views.upload_hoby, name = 'upload_hoby'),
    path('success', views.success, name='success'),
    path('hotel_images', views.display_hotel_images, name = 'hotel_images'),
]