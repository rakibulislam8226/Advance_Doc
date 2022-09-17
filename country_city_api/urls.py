from django.urls import path


from . views import *
urlpatterns = [
    path('countries/',CountryListView.as_view()),
    path('countries/<str:name>/',CountryDetailsView.as_view()),
    # path('cities/', CityListView.as_view()),
    path('cities/<str:country>/', CitySearchView.as_view()),
    path('cities/<str:country>/<str:city>/', CityDetailsView.as_view()),
    # path('cities/', CitySearchView),
]