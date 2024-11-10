"""
"""
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users, Activities, Allergens, UserActivities, UserAllergens, PlannedActivities


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ["url", "id", "username", "email", "password", "address"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(UsersSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(
                validated_data["password"])
        return super(UsersSerializer, self).update(instance, validated_data)

    def validate_username(self, value):
        if Users.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value


class ActivitiesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activities
        fields = ["url", "activity_id", "activity_name",
                  "activity_desc"]


class AllergensSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergens
        fields = ["url", "allergen_id", "allergen_name", "allergen_desc"]


class UserActivitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserActivities
        fields = ["url", "user_activity_id", "user_id",
                  "activity_id"]


class UserAllergensSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAllergens
        fields = ["url", "user_allergen_id", "user_id", "allergen_id"]


class PlannedActivitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlannedActivities
        fields = ["url", "planned_activity_id", "user_id",
                  "activity_id", "location", "start_date", "end_date"]
