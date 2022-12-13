from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang
#presentasi
from dashboard.models import Datapenjualan
from dashboard.models import Datapelanggan
# # Create your views here.
#presentasi
def Pelanggan_view(request):
    datapelanggans=Datapelanggan.objects.all()
    titelnya="Data Pelanggan"
    konteks={
        'datapelanggan':datapelanggans,
        'titel':titelnya,
    } 
    return render(request, 'datapelanggan.html', konteks)

def Penjualan_view(request):
    datapenjualans=Datapenjualan.objects.all()
    titelnya="Data Penjualan"
    konteks={
        'datapenjualan':datapenjualans,
        'titel':titelnya,
    }
    return render(request, 'datapenjualan.html', konteks)


def Barang_view(request):
    barangs=Barang.objects.all()
    titelnya="Data Barang"
    konteks={
        'barang':barangs,
        'titel':titelnya, 
    }
    return render(request, 'tampil_brg.html',konteks)

def tambah_barang(request):
    titelnya="Registrasi Barang"
    form=FormBarang()
    konteks={
        'form':form,
            'titel':titelnya,
    }
    return render(request,'tambah_barang.html',konteks)

def blog(request):
    titelnya="Blog"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'blog.html',konteks)

def blogdetail(request):
    titelnya="Blog Detail"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'blog-detail.html',konteks)

def contact(request):
    titelnya="Contact"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'contact.html',konteks)

def projectdetail(request):
    titelnya="Project Detail"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'project-detail.html',konteks)