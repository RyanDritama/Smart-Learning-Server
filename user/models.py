from django.db import models
from django.db import connection

DAYS_OF_WEEK = (
    ('0', 'Senin'),
    ('1', 'Selasa'),
    ('2', 'Rabu'),
    ('3', 'Kamis'),
    ('4', 'Jumat'),
)

class user(models.Model):
    nama = models.CharField(max_length=45, null=True)
    nim = models.IntegerField(primary_key = True)
    def __str__(self):
        return(self.nama)


class kelas(models.Model):
    class Meta:
        verbose_name_plural = 'kelas'

    kode = models.CharField(max_length=45)
    nama = models.CharField(max_length=45)
    pengajar = models.CharField(max_length=45)
    tahun = models.IntegerField()
    def __str__(self):
        return(self.nama)


class anggota(models.Model):
    id_kelas = models.ForeignKey(kelas, null=True, on_delete=models.SET_NULL)
    nim = models.ForeignKey(user, null=True, on_delete=models.SET_NULL)

class jadwal(models.Model):
    hari = models.CharField(max_length=2, choices=DAYS_OF_WEEK)
    start = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    end = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    id_kelas = models.ForeignKey(kelas, null=True, blank=True, on_delete=models.SET_NULL)


class pertemuan(models.Model):
    tanggal = models.DateField(auto_now=False, auto_now_add=False)
    id_kelas = models.ForeignKey(kelas, null=True, blank=True, on_delete=models.SET_NULL)

class presensi(models.Model):
    nim = models.ForeignKey(user, null=True, blank=True, on_delete=models.SET_NULL)
    id_pertemuan = models.ForeignKey(pertemuan, null=True, blank=True, on_delete=models.SET_NULL)

class tugas(models.Model):
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    desc = models.CharField(max_length=240)
    id_kelas = models.ForeignKey(kelas, null=True, on_delete=models.SET_NULL)
    nama = models.CharField(max_length=100)
    def __str__(self):
        return(self.nama)

class submisi(models.Model):
    id_tugas = models.ForeignKey(tugas, null=True, on_delete=models.SET_NULL)
    nim = models.ForeignKey(user, null=True, on_delete=models.SET_NULL)
    submisi = models.CharField(max_length=240,null=True)



class ujian(models.Model):
    desc = models.CharField(max_length=240)
    start = models.DateTimeField(null = True)
    end = models.DateTimeField(null = True)
    nama = models.CharField(max_length=100, null=True)
    id_kelas = models.ForeignKey(kelas, null=True, blank=True, on_delete=models.SET_NULL)


class userJadwal(models.Model):
    nimUser = models.ForeignKey(user, null=True, on_delete=models.SET_NULL)
    id_kelas = models.ForeignKey(kelas, null=True, blank=True, on_delete=models.SET_NULL)
    kode = models.CharField(max_length=45)
    nama = models.CharField(max_length=45)
    nama_pengajar = models.CharField(max_length=45,null=True)
    hari = models.CharField(max_length=34, choices=DAYS_OF_WEEK)
    start = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    end = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    def save(self, *args, **kwargs):
        self.userJadwal = userJadwal.objects.raw('SELECT  1 id, user_anggota.id_kelas_id, user_kelas.kode, user_kelas.nama, user_kelas.pengajar as nama_pengajar, user_jadwal.hari, user_jadwal.start, user_jadwal.end FROM user_anggota INNER JOIN user_kelas on user_kelas.id = user_anggota.id_kelas_id INNER JOIN user_jadwal on user_jadwal.id_kelas_id = user_anggota.id_kelas_id INNER JOIN user_user on user_anggota.nim_id = user_user.nim WHERE user_anggota.nim_id = 13217048 ORDER BY user_jadwal.hari ASC, user_jadwal.start ASC')
        super(userJadwal, self).save(*args, **kwargs)

class userPresensi(models.Model):
    id_kelas = models.IntegerField(null=True)
    kode = models.CharField(max_length=45)
    nama = models.CharField(max_length=45)
    total_presensi = models.IntegerField()
    total_pertemuan = models.IntegerField()

class userTugas(models.Model):
    id_tugas = models.IntegerField(null=True)
    id_kelas = models.ForeignKey(kelas, null=True, blank=True, on_delete=models.SET_NULL)
    kode = models.CharField(max_length=45,null = True,blank=True)
    nama_matkul = models.CharField(max_length=45,null = True,blank=True)
    nama = models.CharField(max_length=100,null = True,blank=True)
    desc = models.CharField(max_length=240,null = True,blank=True)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)



class userUjian(models.Model):
    id_ujian = models.IntegerField(null=True)
    id_kelas = models.ForeignKey(kelas, null=True, blank=True, on_delete=models.SET_NULL)
    kode = models.CharField(max_length=45)
    nama_matkul = models.CharField(max_length=45)
    nama = models.CharField(max_length=100)
    desc = models.CharField(max_length=240)
    start = models.DateTimeField(null = True)
    end = models.DateTimeField(null = True)

class history(models.Model):
    path = models.CharField(max_length=45)
    method = models.CharField(max_length=45)
    response = models.CharField(max_length=45)
    time = models.DateTimeField(null = True)
    



