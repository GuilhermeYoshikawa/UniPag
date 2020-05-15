from django.contrib import admin
from django.urls import path, include

# from unipag.views import home, inicial

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', home, name='home'),

    path('', include('unipag.urls')),
    path('admin/', admin.site.urls),

]
