# plik ankiety/urls.py



from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-tools/', include('admin_tools.urls'),),
    path('ankiety/', include('ankiety.urls'),)
]