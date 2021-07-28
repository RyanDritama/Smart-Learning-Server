from django.contrib import admin
from .models import *

admin.site.register(user)
admin.site.register(kelas)
admin.site.register(anggota)
admin.site.register(jadwal)
admin.site.register(pertemuan)
admin.site.register(presensi)
admin.site.register(tugas)
admin.site.register(submisi)
admin.site.register(ujian)
admin.site.register(userJadwal)
admin.site.register(userPresensi)
admin.site.register(userTugas)
admin.site.register(userUjian)
# admin.site.register(kelas)
# admin.site.register(ujian)
# admin.site.register(tugas)
# admin.site.register(submisi)
# admin.site.register(anggota)

# Register your models here.
