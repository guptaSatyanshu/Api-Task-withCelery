
from django.contrib import admin
from django.urls import path, include
from myapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', views.SerForm1Views)
router.register('tasktracker', views.SerForm2Views)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celerymail/', views.celerymail, name='celerymail'),
    path('', include(router.urls))

]
