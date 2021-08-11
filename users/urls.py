from django.urls import path
from users.views import remove_from_profile
from users import views as user_views
from users.views import remove_from_profile

app_name = 'profile'

urlpatterns = [
    path('', user_views.profile, name='profile'),
    path('remove_from_profile/', remove_from_profile),
]