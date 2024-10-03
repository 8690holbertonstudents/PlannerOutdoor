from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
"""from django.http import HttpResponse < inutile pour l'instant"""

from rest_framework import viewsets
from .models import Users, Activities, Allergens, UserActivities, UserAllergens, PlannedActivities
from .serializers import UsersSerializer, ActivitiesSerializer, AllergensSerializer, UserActivitiesSerializer, UserAllergensSerializer, PlannedActivitiesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]


class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer


class AllergensViewSet(viewsets.ModelViewSet):
    queryset = Allergens.objects.all()
    serializer_class = AllergensSerializer


class UserActivitiesViewSet(viewsets.ModelViewSet):
    queryset = UserActivities.objects.all()
    serializer_class = UserActivitiesSerializer


class UserAllergensViewSet(viewsets.ModelViewSet):
    queryset = UserAllergens.objects.all()
    serializer_class = UserAllergensSerializer


class PlannedActivitiesViewSet(viewsets.ModelViewSet):
    queryset = PlannedActivities.objects.all()
    serializer_class = PlannedActivitiesSerializer
