"""
Django models creation module
"""
from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class Users(models.Model):
    """
    """
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[validate_password])
    address = models.CharField(max_length=250, unique=True)

    def clean(self):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)

    def save(self, *args, **kwargs):
        self.clean()
        super(Users, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name_plural = "Users"


class Activities(models.Model):
    """
    """
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=50, unique=True)
    activity_desc = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.activity_name

    class Meta:
        verbose_name_plural = "Activities"


class Allergens(models.Model):
    """
    """
    allergen_id = models.AutoField(primary_key=True)
    allergen_name = models.CharField(max_length=50, unique=True)
    allergen_desc = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.allergen_name

    class Meta:
        verbose_name_plural = "Allergens"


class UserActivities(models.Model):
    """
    """
    user_activity_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'activity_id')
        verbose_name_plural = "UserActivities"

    def __str__(self) -> str:
        return f'{self.user_id.username} - {self.activity_id.activity_name}'


class UserAllergens(models.Model):
    """
    """
    user_allergen_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    allergen_id = models.ForeignKey(Allergens, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'allergen_id')
        verbose_name_plural = "UserAllergens"

    def __str__(self) -> str:
        return f'{self.user_id.username} - {self.allergen_id.allergen_name}'


class PlannedActivities(models.Model):
    """
    """
    planned_activity_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    location = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ('user_id', 'activity_id', 'start_date', 'end_date')
        verbose_name_plural = "PlannedActivities"

    def __str__(self) -> str:
        return f'{self.user_id.username} - {self.activity_id.activity_name} - {self.start_date} - {self.end_date}'
