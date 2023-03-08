from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Shrinjit's website | Admin"
admin.site.site_title = "Shrinjit's website | Admin"
admin.site.index_title = "Welcome to Shrinjit's website"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
