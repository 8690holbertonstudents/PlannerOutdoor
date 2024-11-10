import requests
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
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
        if self.action in ["create", "retrieve", "update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        elif self.action == "list":
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
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAdminUser]
        elif self.action in ["list", "retrieve"]:
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
    Django viewset for Users model.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=["get", "patch"], url_path="Account")
    def account(self, request):
        """
        """
        try:
            if request.method == "GET":
                serializer = self.get_serializer(request.user)
                return Response({"message": "", "data": serializer.data})
            elif request.method == "PATCH":
                serializer = self.get_serializer(
                    request.user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Account information updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
                return Response({"message": "Validation errors", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error occurred while processing method"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["post"], url_path="Register")
    def register(self, request):
        """
        """
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "New user added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"message": "Validation errors", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error occurred while processing method"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["post"], url_path="RecoverPassword")
    def recover_password(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        new_password = request.data.get("newPassword")

        try:
            user = Users.objects.get(username=username)
            if user.email != email:
                return Response({"error": "Wrong email for this username"}, status=status.HTTP_400_BAD_REQUEST)
            user.password = make_password(new_password)
            user.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({"error": "Username does not exist"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["delete"], url_path="DeleteAccount")
    def delete_account(self, request):
        try:
            user = request.user
            user.delete()
            return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Error while deleting account"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActivitiesViewSet(ActivitiesAllergensPerms, viewsets.ModelViewSet):
    """
    Django viewset for Activities model.
    """
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer


class AllergensViewSet(ActivitiesAllergensPerms, viewsets.ModelViewSet):
    """
    Django viewset for Allergens model.
    """
    queryset = Allergens.objects.all()
    serializer_class = AllergensSerializer


class UserActivitiesViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django viewset for UserActivities model.
    """
    queryset = UserActivities.objects.all()
    serializer_class = UserActivitiesSerializer

    @action(detail=False, methods=["get"], url_path="GetUserActivities")
    def get_user_activities(self, request):
        try:
            user = request.user
            user_activities = UserActivities.objects.filter(user_id=user)
            serializer = self.get_serializer(user_activities, many=True)
            return Response({"message": "", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Error while reading user activities"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["post"], url_path="PostUserActivities")
    def post_user_activities(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"message": "User activities updated successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": "Error while updating user activities"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": "Serializer errors", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["delete"], url_path="DeleteUserActivities/(?P<user_activity_id>[^/.]+)")
    def delete_user_activities(self, request, user_activity_id=None):
        try:
            user_activity = UserActivities.objects.get(
                user_activity_id=user_activity_id)
            user_activity.delete()
            return Response({"message": f"UserActivity with id {user_activity_id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Error while deleting user activities"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserAllergensViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django viewset for UserAllergens model.
    """
    queryset = UserAllergens.objects.all()
    serializer_class = UserAllergensSerializer

    @action(detail=False, methods=["get", "patch"], url_path="UserSelectedAllergens")
    def get_user_allergens(self, request):
        """
        """
        try:
            if request.method == "GET":
                user_allergens = self.queryset.filter(user_id=request.user.id)
                serializer = self.get_serializer(user_allergens, many=True)
                return Response({"message": "", "data": serializer.data})
            elif request.method == "PATCH":
                selected_allergens = request.data.get("Allergens", [])
                UserAllergens.objects.filter(user_id=request.user.id).delete()
                for allergen_id in selected_allergens:
                    UserAllergens.objects.create(
                        user_id=request.user.id, allergen_id=allergen_id)
                updated_allergens = self.queryset.filter(
                    user_id=request.user.id)
                serializer = self.get_serializer(updated_allergens, many=True)
            return Response({"message": "User allergens updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Error occurred while processing method"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PlannedActivitiesViewSet(DetermineOwnerOrAdmin, viewsets.ModelViewSet):
    """
    Django viewset for PlannedActivities model.
    """
    queryset = PlannedActivities.objects.all()
    serializer_class = PlannedActivitiesSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Custom class to add the access token to the cookie for authenticated user.
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get("access")
        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=token,
            expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
        )
        return response


class CookieTokenRefreshView(TokenRefreshView):
    """
    Custom class to add the refresh token to the cookie for authenticated user.
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get("access")
        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=token,
            expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
        )
        return response


class GeoCodingViewSet(viewsets.ViewSet):
    """
    ViewSet for retrieving geographic coordinates.
    Using OpenWeathermap Geocoding API.
    """
    permission_classes = [AllowAny]

    def list(self, request):
        location = request.query_params.get("location")
        if not location:
            return Response({"error": "Please provide a location"}, status=status.HTTP_400_BAD_REQUEST)

        api_key = settings.OPENWEATHER_API_KEY
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={
            location}&limit=5&appid={api_key}"

        try:
            response = requests.get(geocoding_url)
            data = response.json()
            if response.status_code != 200 or not data:
                return Response({"error": "Location not found"}, status=response.status_code)
            return Response({"message": "", "data": data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Error from Openweathermap geocoding API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeatherViewSet(viewsets.ViewSet):
    """
    Django viewset for weather data for 16 days.
    Using OpenWeathermap Geocoding API.
    """
    permission_classes = [AllowAny]

    def list(self, request):
        """
        Retrieve weather data for a specified city or by latitude and longitude.
        """
        api_key = settings.OPENWEATHER_API_KEY
        city = request.query_params.get("city")
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")

        if lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast/daily?lat={
                lat}&lon={lon}&cnt=16&appid={api_key}"
        elif city:
            url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={
                city}&cnt=16&appid={api_key}"
        else:
            return Response({"error": "Please provide a city name or latitude and longitude"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return Response({"message": "", "data": data}, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": "Error from Openweathermap forecast API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeatherDetailsViewSet(viewsets.ViewSet):
    """
    Django viewset for weather details for the selected day.
    Using OpenWeathermap Geocoding API.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Retrieve weather data for a specified city and a choosen day.
        """
        api_key = settings.OPENWEATHER_API_KEY
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")

        if not lat or not lon:
            return Response({"error": "Latitude, longitude, are required"}, status=status.HTTP_400_BAD_REQUEST)

        url = f"http://api.openweathermap.org/data/2.5/forecast/daily?lat={
            lat}&lon={lon}&cnt=16&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return Response({"message": "", "data": data}, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": "Error from Openweathermap forecast API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeatherPollutionViewSet(viewsets.ViewSet):
    """
    Django viewset for weather pollution for the selected day (maxi 4 days).
    Using OpenWeathermap Geocoding API.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Retrieve pollution data for a specified city and a choosen day.
        """
        api_key = settings.OPENWEATHER_API_KEY
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")

        if not lat or not lon:
            return Response({"error": "Latitude, longitude, are required"}, status=status.HTTP_400_BAD_REQUEST)

        url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={
            lat}&lon={lon}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return Response({"message": "", "data": data}, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": "Error from Openweathermap pollution API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
