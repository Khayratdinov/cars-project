from django.urls import path
from cars.views import transportView,transportDetailView, categoryDetailView

urlpatterns = [
    path('',transportView, name="cars_list"),
    path('car/<slug:slug>', transportDetailView, name="transport_detail" ),
    path('category/<int:pk>', categoryDetailView, name="category_detail" ),

]
