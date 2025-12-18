INSTALLED_APPS = [
    # default Django apps...
    'rest_framework',
    'users',   # our users app (optional; using built-in User)
    'tasks',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # if using JWT
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
DEBUG = True
ALLOWED_HOSTS = []
