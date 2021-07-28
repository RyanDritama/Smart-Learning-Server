from django.shortcuts import render
from user.models import user, presensi
from user.serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import datetime

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class presensiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = presensi.objects.all()
    serializer_class = presensiSerializer

class cekPresensiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = presensi.objects.all()
    serializer_class = cekPresensiSerializer
    def get_queryset(self):
        id_pertemuan = self.request.query_params.get('id_pertemuan')
        nimUser = self.request.query_params.get('nimUser')
        query_list = presensi.objects.filter(id_pertemuan_id = id_pertemuan, nim_id = nimUser )
        return query_list

class cekPertemuanViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = pertemuan.objects.all()
    serializer_class = cekPertemuanSerializer
    def get_queryset(self):
        id_kelas = self.request.query_params.get('id_kelas')
        tanggal = self.request.query_params.get('tanggal')
        query_list = pertemuan.objects.filter(id_kelas = id_kelas, tanggal = tanggal )
        return query_list

class kelasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = user.objects.all()
    serializer_class = kelasSerializer

class ujianViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = user.objects.all()
    serializer_class = ujianSerializer

class userJadwalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = userJadwal.objects.all()
    serializer_class = userJadwalSerializer
    def get_queryset(self):
        nimUser = self.request.query_params.get('nimUser', None)
        nimUser = str(nimUser)
        print(nimUser)
        query_list = userJadwal.objects.raw('SELECT  1 id, user_anggota.id_kelas_id, user_kelas.kode, user_kelas.nama, user_kelas.pengajar as nama_pengajar, user_jadwal.hari, user_jadwal.start, user_jadwal.end FROM user_anggota INNER JOIN user_kelas on user_kelas.id = user_anggota.id_kelas_id INNER JOIN user_jadwal on user_jadwal.id_kelas_id = user_anggota.id_kelas_id INNER JOIN user_user on user_anggota.nim_id = user_user.nim WHERE user_anggota.nim_id = %s ORDER BY user_jadwal.hari ASC, user_jadwal.start ASC', [nimUser])
        return query_list

class userPresensiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = userPresensi.objects.all()
    serializer_class = userPresensiSerializer
    def get_queryset(self):
        nimUser = self.request.query_params.get('nimUser', None)
        nimUser = str(nimUser)
        print(nimUser)
        query_list = userPresensi.objects.raw('SELECT 1 id, user_anggota.id_kelas_id as id_kelas, user_kelas.kode, user_kelas.nama, COUNT(user_presensi.id_pertemuan_id) AS total_presensi, COUNT(user_pertemuan.id) AS total_pertemuan FROM user_anggota INNER JOIN user_kelas ON user_kelas.id = user_anggota.id_kelas_id INNER JOIN user_pertemuan ON user_pertemuan.id_kelas_id = user_anggota.id_kelas_id LEFT JOIN user_presensi ON user_presensi.id_pertemuan_id = user_pertemuan.id WHERE user_anggota.nim_id = %s GROUP BY user_anggota.id_kelas_id', [nimUser])
        return (query_list)

class userTugasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = userTugas.objects.all()
    serializer_class = userTugasSerializer
    def get_queryset(self):
        nimUser = self.request.query_params.get('nimUser', None)
        nimUser = str(nimUser)
        print(nimUser)
        query_list = userTugas.objects.raw('SELECT 1 id, user_tugas.id as id_tugas, user_anggota.id_kelas_id, user_kelas.kode, user_kelas.nama as nama_matkul, user_tugas.nama, user_tugas.desc, user_tugas.deadline FROM user_anggota INNER JOIN user_kelas ON user_kelas.id = user_anggota.id_kelas_id INNER JOIN user_tugas ON user_tugas.id_kelas_id = user_anggota.id_kelas_id WHERE  user_anggota.nim_id = %s ORDER BY  user_tugas.deadline ASC', [nimUser])
        return (query_list)
	


class userUjianViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = userUjian.objects.all()
    serializer_class = userUjianSerializer
    def get_queryset(self):
        nimUser = self.request.query_params.get('nimUser', None)
        nimUser = str(nimUser)
        print(nimUser)      
        query_list = userUjian.objects.raw('SELECT 1 id, user_ujian.id as id_ujian, user_anggota.id_kelas_id, user_kelas.kode, user_kelas.nama as nama_matkul, user_ujian.nama, user_ujian.desc, user_ujian.start, user_ujian.end FROM user_anggota INNER JOIN user_kelas ON user_kelas.id = user_anggota.id_kelas_id INNER JOIN user_ujian ON user_ujian.id_kelas_id = user_anggota.id_kelas_id WHERE user_anggota.nim_id = %s ORDER BY user_ujian.start ASC', [nimUser])
        return (query_list)

class userSubmisiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = submisi.objects.all()
    serializer_class = submisiSerializer
    def create(self, request):
        serializer = submisiSerializer(data=request.data)
        if serializer.is_valid():
            submisi = serializer.save()
            pid = submisi.id
            data = serializer.data
            data.update({'id':pid})
            return Response(data)


class cekSubmisiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = submisi.objects.all()
    serializer_class = cekSubmisiSerializer
    def get_queryset(self):
        id_tugas = self.request.query_params.get('id_tugas')
        nimUser = self.request.query_params.get('nimUser')
        query_list = submisi.objects.filter(id_tugas = id_tugas, nim = nimUser )
        return query_list
    
class historyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = history.objects.all()
    serializer_class = historySerializer
    def get_queryset(self):
        username = self.request.query_params.get('username')
        query_list = history.objects.raw('SELECT 1 id, request_request.path, request_request.method, request_request.response, request_request.time FROM request_request INNER JOIN account_account on account_account.id = request_request.user_id WHERE account_account.username = %s ORDER BY request_request.time DESC LIMIT 10 ', [username])
        return (query_list)

class timeView(APIView):
    def get(self, request):
        return Response(datetime.datetime.now())
