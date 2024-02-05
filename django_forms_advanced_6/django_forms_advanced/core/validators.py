from django.core.exceptions import ValidationError


def validate_name(value):
    for char in value:
        if char.isdigit():
            raise ValidationError("The name cannot contain digits!")


class FileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(f"File size cannot exceed {self.max_size}")