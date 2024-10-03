from django.urls import path, include
from .views import UsersViewSet, ActivitiesViewSet, AllergensViewSet, UserActivitiesViewSet, UserAllergensViewSet, PlannedActivitiesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'po_app/Users', UsersViewSet)
router.register(r'po_app/Activities', ActivitiesViewSet)
router.register(r'po_app/Allergens', AllergensViewSet)
router.register(r'po_app/UserActivities', UserActivitiesViewSet)
router.register(r'po_app/UserAllergens', UserAllergensViewSet)
router.register(r'po_app/PlannedActivities', PlannedActivitiesViewSet)

"""app_name = 'po_app'"""
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
