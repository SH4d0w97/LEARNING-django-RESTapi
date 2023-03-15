from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

urlpatterns = [
    path("item/", ItemList.as_view()), #.as_view() because they are generic class based view
    path("item/<int:pk>/", ItemDetail.as_view()),
    path("location/", LocationList.as_view()),
    path("location/<int:pk>/", LocationDetail.as_view()),

]
 