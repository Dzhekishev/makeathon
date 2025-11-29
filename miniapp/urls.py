from django.urls import path, include
from .views import*
from miniapp import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.Sensordata_View.as_view(), name='Sensordata_View'),
    path('index',sensordata, name='sensordata')
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns=format_suffix_patterns(urlpatterns)