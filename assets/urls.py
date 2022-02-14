from django.urls import path
from assets.views import home
urlpatterns = [

    # Main Dashboard Link
    path('', home, name='home'),
]