import requests
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Users, Activities, Allergens, UserActivities, UserAllergens, PlannedActivities
from .serializers import UsersSerializer, ActivitiesSerializer, AllergensSerializer, UserActivitiesSerializer, UserAllergensSerializer, PlannedActivitiesSerializer


class DetermineOwnerOrAdmin:
    """
    Class to determine permissions rules for UsersViewSet, UserActivitiesViewSet, UserAllergensViewSet.
    """

    def get_permissions(self):
        """
        Returns the appropriate permission classes.
        """
        if self.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_object(self):
        """
        Returns the object the view is displaying.
        """
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj


class ActivitiesAllergensPerms:
    """
    Class to determine permissions rules for ActivitiesViewSet, AllergensViewSet.
    """

    def get_permissions(self):
        """
        Returns the appropriate permission classes.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admin users to view it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return object permissions based on user role.
        """
        if request.user.is_staff:
            return True
        return obj.id == request.user.id


class UsersViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django serializer for Users model.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='account')
    def account(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ActivitiesViewSet(ActivitiesAllergensPerms, viewsets.ModelViewSet):
    """
    Django serializer for Activities model.
    """
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer


class AllergensViewSet(ActivitiesAllergensPerms, viewsets.ModelViewSet):
    """
    Django serializer for Allergens model.
    """
    queryset = Allergens.objects.all()
    serializer_class = AllergensSerializer


class UserActivitiesViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django serializer for UserActivities model.
    """
    queryset = UserActivities.objects.all()
    serializer_class = UserActivitiesSerializer


class UserAllergensViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django serializer for UserAllergens model.
    """
    queryset = UserAllergens.objects.all()
    serializer_class = UserAllergensSerializer


class PlannedActivitiesViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django serializer for PlannedActivities model.
    """
    queryset = PlannedActivities.objects.all()
    serializer_class = PlannedActivitiesSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Custom class to add the access token to the cookie for authenticated user.
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('access')
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=token,
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
        )
        return response


class CookieTokenRefreshView(TokenRefreshView):
    """
    Custom class to add the refresh token to the cookie for authenticated user.
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('access')
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=token,
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
        )
        return response


class WeatherViewSet(viewsets.ViewSet):
    """
    Django serializer for weather data from external OpenWeather API.
    """
    permission_classes = [AllowAny]

    def list(self, request):
        """
        Retrieve weather data for a specified city.
        """
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "Please enter a city"}, status=status.HTTP_400_BAD_REQUEST)

        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={
            city}&cnt=16&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
