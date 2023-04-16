from django.urls import path
from cbvapp import views


urlpatterns=[
    path('marksfbv/',views.MarksFbv,name='fbv'),
    path('markscbv',views.MarksCbv.as_view(),name='cbv'),
    path('readfbv/',views.Readfbv,name='readfbv'),
    path('readcbv/',views.ReadCbv.as_view,name='readcbv'),
    path('updatefbv/<pk>/',views.Updatefbv,name='updatefbv'),
    path('updatecbv/<pk>/',views.UpdateCbv.as_view(),name='updatecbv'),
]