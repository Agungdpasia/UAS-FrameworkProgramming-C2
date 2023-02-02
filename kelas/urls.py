from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import blog
from dashboard.views import blogdetail
from dashboard.views import contact
from dashboard.views import projectdetail
from dashboard.views import *

#presentasi
from dashboard.views import Buku_view
from dashboard.views import Peminjaman_view

def satu(request):
    titelnya="Home"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'home.html',konteks)

urlpatterns = [
    path('admin', admin.site.urls),
    path('',satu),
    path('home/',satu),
    path('blog/',blog),
    path('blogdetail/',blogdetail),
    path('contact/',contact),
    path('projectdetail/',projectdetail),
    path('registrasibrg/', tambah_barang),
    path('regbuku/', tambah_buku),
    path('regpeminjaman/', tambah_peminjaman),
    path('databarang/',Barang_view),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
    path('ubahbuku/<int:id_databuku>',ubah_buku,name='ubah_buku'),
    path('hapusbuku/<int:id_databuku>',hapus_buku,name='hapus_buku'),
    path('ubahlg/<int:id_datapeminjaman>',ubah_lg,name='ubah_lg'),
    path('hapuslg/<int:id_datapeminjaman>',hapus_lg,name='hapus_lg'),
    #presentasi
    path('databuku/',Buku_view),
    path('datapeminjaman/',Peminjaman_view),
]
