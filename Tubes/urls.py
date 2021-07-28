"""Tubes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from user.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ujian', userUjianViewSet)
router.register('jadwal', userJadwalViewSet)
router.register('tugas', userTugasViewSet)
router.register('mahasiswa', kelasViewSet)
router.register('presensi', presensiViewSet)
router.register('persentase', userPresensiViewSet)
router.register('submisi', userSubmisiViewSet)
router.register('cekpresensi', cekPresensiViewSet)
router.register('cekpertemuan', cekPertemuanViewSet)
router.register('ceksubmisi', cekSubmisiViewSet)
router.register('history', historyViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls', 'account_api')),
    path('api/time/', timeView.as_view()),
]
