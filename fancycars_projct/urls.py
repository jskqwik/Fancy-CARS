"""fancycars_projct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from garage.views import (
    CarListView, 
    CarDetailView, 
    CarCreateView, 
    CarUpdateView, 
    CarDeleteView, 
    FilterCarsColorView,
    FilterCarMakeView,
    CarListAPIView,
    CarDetailAPIView,
    CarCreateAPIView,
    UserCreateView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarListView.as_view(), name="car_list"),
    path('cars/<int:pk>/', CarDetailView.as_view(), name="car_detail"),
    path('create/', CarCreateView.as_view(), name="car_create"),
    path('update/<int:pk>/', CarUpdateView.as_view(), name="car_update"),
    path('delete/<int:pk>/', CarDeleteView.as_view(), name="car_delete"),
    path('bycolor/', FilterCarsColorView.as_view(), kwargs={"color": None}, name="find_car_color"),
    path('bymake/', FilterCarMakeView.as_view(), kwargs={"make": None}, name="find_car_make"),
    path('api/', CarListAPIView.as_view(), name="car_apilist"),
    path('api/<int:pk>/', CarDetailAPIView.as_view(), name="car_apidetail"),
    path('createapi/', CarCreateAPIView.as_view(), name="car_apicreate"),
    path('usercreate/', UserCreateView.as_view(), name="user_create"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)