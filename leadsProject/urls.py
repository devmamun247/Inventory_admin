"""
URL configuration for leadsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# view import by Mamun
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('admin/', admin.site.urls), # it's default
    #path('admin/', admin.site.urls), # it's default
    #path('', views.demo), # it's default admin page (Mamun)
    #path('demo2', views.demo2), # it's default admin page (Mamun)
    # path('', views.index), # it's goes to admin action views controller index method (Mamun)
    # path('', views.index, name='task_upload_url'), 
    path('', views.index, name='task_upload_url_submit'), 
    path('admin/customer/insert', views.insert, name='customer_insert'),
    path('admin/customer/view', views.show, name='show_customer_data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
