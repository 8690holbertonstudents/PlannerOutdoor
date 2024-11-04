from rest_framework import routers
from django.urls import path, include
from .views import UsersViewSet, ActivitiesViewSet, AllergensViewSet, UserActivitiesViewSet
from .views import UserAllergensViewSet, PlannedActivitiesViewSet, GeoCodingViewSet
from .views import WeatherViewSet, WeatherDetailsViewSet, WeatherPollutionViewSet

router = routers.DefaultRouter()
router.register(r'po_app/Users', UsersViewSet)
router.register(r'po_app/Activities', ActivitiesViewSet)
router.register(r'po_app/Allergens', AllergensViewSet)
router.register(r'po_app/UserActivities', UserActivitiesViewSet)
router.register(r'po_app/UserAllergens', UserAllergensViewSet)
router.register(r'po_app/PlannedActivities', PlannedActivitiesViewSet)
router.register(r'po_app/Weather', WeatherViewSet, basename='weather')
router.register(r'po_app/WeatherDetails',
                WeatherDetailsViewSet, basename='weatherdetails')
router.register(r'po_app/Geocode', GeoCodingViewSet, basename='geocode')
router.register(r'po_app/WeatherPollution',
                WeatherPollutionViewSet, basename='weatherpollution')

"""app_name = 'po_app'"""
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
