from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg = models.CharField(max_length=8, default='BRG')
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "{}.{}.{}.{}.{}.{}".format(self.kodebrg,self.nama, self.stok,self.harga,self.link_gbr, self.waktu_posting)

class Transaksi(models.Model):
    kodetrans = models.CharField(max_length=10)
    tgltrans = models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()

    def __str__(self):
        return "{}. {}.{}".format(self.kodetrans, self.tgltrans,self.total)

class Detailtrans(models.Model):
    kodetrans = models.CharField(max_length=10)
    kodebrg = models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()


    def __str__(self):
        return "{}. {}".format(self.kodetrans, self.kodebrg)

 #presentasi

class Databuku(models.Model):
    no = models.IntegerField()
    judul = models.CharField(max_length=20)
    penulis = models.CharField(max_length=15)
    penerbit = models.CharField(max_length=20)
    tahunterbit = models.IntegerField()
    tebal = models.BigIntegerField()

    def __str__(self):
        return "{}.{}.{}.{}.{}.{}".format(self.no, self.judul, self.penulis, self.penerbit, self.tahunterbit, self.tebal)

class Datapeminjaman(models.Model):
    no = models.IntegerField()
    nama = models.CharField(max_length=20)
    jenisbuku = models.CharField(max_length=20)
    tglpinjam = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}.{}.{}".format(self.no, self.nama, self.jenisbuku, self.tglpinjam)