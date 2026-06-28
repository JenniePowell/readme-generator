def validate_email(value):
    if "@" in value and "." in value:
        return True
    return False