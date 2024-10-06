from rest_framework import viewsets, permissions
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


class WeatherViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    # logique pour récupérer les données de l'API météo


class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]  # Tout le monde peut s'inscrire


class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]  # Tout le monde peut se connecter
