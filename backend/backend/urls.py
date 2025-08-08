"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from flora import views
from rest_framework import routers

admin.site.site_header="FLORA DATABASE"

router=routers.DefaultRouter()
router.register(r'flora',views.floraView,'flora')
router.register(r'habitat',views.habitatView,'habitat')
router.register(r'characteristics',views.characteristicsView,'characteristics')
router.register(r'marketValue',views.marketValueView,'marketValue')
router.register(r'Notification',views.NotificationView,'Notification')
router.register(r'Viewer',views.ViewerView,'Viewer')
router.register(r'viewer_email',views.viewer_emailView,'viewer_email')
router.register(r'can_view',views.can_viewView,'can_view')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('get_flora_records',views.get_flora_records,name='get_flora_records'),
    # Other URL patterns
    #path('api/get_filter_options/<str:attribute>/', views.get_filter_options, name='get_filter_options'),
    #path('api/get_flora_details/<str:title>/', views.get_flora_details, name='get_flora_details'),

]

