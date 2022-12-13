from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import blog
from dashboard.views import blogdetail
from dashboard.views import contact
from dashboard.views import projectdetail
from dashboard.views import tambah_barang,Barang_view
#presentasi
from dashboard.views import Penjualan_view
from dashboard.views import Pelanggan_view

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
    path('databarang/',Barang_view),
    #presentasi
    path('datapenjualan/',Penjualan_view),
    path('datapelanggan/',Pelanggan_view),
]
