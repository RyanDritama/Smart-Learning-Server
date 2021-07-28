from .models import *
from rest_framework import serializers

class userJadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = userJadwal
        fields = ['id_kelas', 'kode', 'nama','nama_pengajar', 'hari', 'start', 'end']

class userJadwalnewSerializer(serializers.ModelSerializer):
    user_nim = userJadwalSerializer
    class Meta:
        model = user
        fields = ['nim', 'user_nim']


class userPresensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPresensi
        fields = ['id_kelas', 'kode', 'nama', 'total_presensi', 'total_pertemuan']

class userTugasSerializer(serializers.ModelSerializer):
    class Meta:
        model = userTugas
        fields = ['id_tugas','id_kelas', 'kode','nama_matkul','nama', 'desc', 'deadline']
# , 'id_kelas', 'kode','nama_matkul','nama', 'desc', 'deadline'
class userUjianSerializer(serializers.ModelSerializer):
    class Meta:
        model = userUjian
        fields = ['id_ujian', 'id_kelas', 'kode', 'nama_matkul', 'nama', 'desc', 'start', 'end']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['nama', 'nim']

class presensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = presensi
        fields = ['id_pertemuan', 'nim']

class cekPresensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = presensi
        fields = ['id_pertemuan']

class cekPertemuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertemuan
        fields = ['id']

class anggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = anggota
        fields = ['kode', 'nama']


class kelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = kelas
        fields = ['id','kode']

class notifujisnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ujian
        fields = ['desc', 'start', 'end', 'nama', 'id_kelas']

class ujianSerializer(serializers.ModelSerializer):
    ujian = notifujisnSerializer(read_only=True,many = True)
    class Meta:
        model = user
        fields = ['nama', 'nim', 'kelas', 'ujian']

class submisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = submisi
        fields = ['id_tugas', 'nim', 'submisi']

class cekSubmisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = submisi
        fields = ['id', 'submisi']

class historySerializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = ['path', 'method', 'response', 'time']

