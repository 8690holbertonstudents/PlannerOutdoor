import re
from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                "Password must contain at least one uppercase character")
        if not re.findall('[a-z]', password):
            raise ValidationError(
                "Password must contain at least one lowercase character")
        if not re.findall('[0-9]', password):
            raise ValidationError(
                "Password must contain at least one number")
        if not re.findall('[^A-Za-z0-9]', password):
            raise ValidationError(
                "Password must contain at least one special character")

        for char in password:
            if password.count(char) > 1:
                raise ValidationError(
                    "All characters in password must be different")

    def get_help_text(self):
        return "Valid password: At least 8 characters, one uppercase, one lowercase, one number, one special character, and all different"
