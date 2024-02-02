from django.contrib import admin
from django.urls import path, include
from asfo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asfo/', include('asfo.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]