import requests
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Users, Activities, Allergens, UserActivities, UserAllergens, PlannedActivities
from .serializers import UsersSerializer, ActivitiesSerializer, AllergensSerializer, UserActivitiesSerializer, UserAllergensSerializer, PlannedActivitiesSerializer


class DetermineOwnerOrAdmin:
    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj


class ActivitiesAllergensPerms:
    # 'create' 'update' 'partial_update' 'destroy' 'list' 'retreive'
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.id == request.user.id


class UsersViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='account')
    def account(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ActivitiesViewSet(ActivitiesAllergensPerms, viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer


class AllergensViewSet(ActivitiesAllergensPerms, viewsets.ModelViewSet):
    queryset = Allergens.objects.all()
    serializer_class = AllergensSerializer


class UserActivitiesViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    queryset = UserActivities.objects.all()
    serializer_class = UserActivitiesSerializer


class UserAllergensViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    queryset = UserAllergens.objects.all()
    serializer_class = UserAllergensSerializer


class PlannedActivitiesViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    queryset = PlannedActivities.objects.all()
    serializer_class = PlannedActivitiesSerializer


"""
class WeatherViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, city=None):
        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            return Response({"error": "City not found"}, status=404)
"""


class WeatherViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "Please enter a city"}, status=status.HTTP_400_BAD_REQUEST)

        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt=16&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
