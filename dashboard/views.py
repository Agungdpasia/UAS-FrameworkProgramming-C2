from django.shortcuts import render, redirect
from dashboard.forms import FormBarang, FormDatabuku, FormDatapeminjaman
from dashboard.models import Barang, Datapeminjaman, Databuku
from django.contrib import messages

#presentasi
from dashboard.models import Databuku
from dashboard.models import Datapeminjaman
# # Create your views here.
#presentasi
def Peminjaman_view(request):
    datapeminjamans=Datapeminjaman.objects.all()
    titelnya="Data peminjaman"
    konteks={
        'datapeminjaman':datapeminjamans,
        'titel':titelnya,
    } 
    return render(request, 'datapeminjaman.html', konteks)

def Buku_view(request):
    databukus=Databuku.objects.all()
    titelnya="Data Buku"
    konteks={
        'databuku':databukus,
        'titel':titelnya,
    }
    return render(request, 'databuku.html', konteks)

def Barang_view(request):
    barangs=Barang.objects.all()
    titelnya="Data Barang"
    konteks={
        'barang':barangs,
        'titel':titelnya, 
    }
    return render(request, 'tampil_brg.html',konteks)

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormBarang()
            titelnya="Registrasi"
            konteks={
                'form':form,
                'titel':titelnya,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_peminjaman(request):
    if request.POST:
        form= FormDatapeminjaman(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormDatapeminjaman()
            titelnya="Registrasi"
            konteks={
                'form':form,
                'titel':titelnya,
            }
            return render(request,'tambah_peminjaman.html',konteks)
    else:
        form=FormDatapeminjaman()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_peminjaman.html',konteks)

def tambah_buku(request):
    if request.POST:
        form= FormDatabuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormDatabuku()
            titelnya="Registrasi"
            konteks={
                'form':form,
                'titel':titelnya,
            }
            return render(request,'tambah_buku.html',konteks)
    else:
        form=FormDatabuku()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_buku.html',konteks)

def hapus_brg(request, id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    barangs=Barang.objects.all()
    titelnya="Data Barang"
    konteks={
        'barang':barangs,
        'titel':titelnya, 
    }
    messages.success(request,"Data Terhapus")
    return render(request,'tampil_brg.html', konteks)

def hapus_buku(request, id_databuku):
    databukus=Databuku.objects.filter(id=id_databuku)
    databukus.delete()
    databukus=Databuku.objects.all()
    titelnya="Data buku"
    konteks={
        'databuku':databukus,
        'titel':titelnya, 
    }
    messages.success(request,"Data Terhapus")
    return render(request,'databuku.html', konteks)

def hapus_lg(request, id_datapeminjaman):
    datapeminjamans=Datapeminjaman.objects.filter(id=id_datapeminjaman)
    datapeminjamans.delete()
    datapeminjamans=Datapeminjaman.objects.all()
    titelnya="Data Peminjaman"
    konteks={
        'datapeminjaman':datapeminjamans,
        'titel':titelnya, 
    }
    messages.success(request,"Data Terhapus")
    return render(request,'datapeminjaman.html', konteks)

def ubah_brg(request, id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs': barangs
        }
    return render(request,'ubah_brg.html',konteks)

def ubah_buku(request, id_databuku):
    databukus=Databuku.objects.get(id=id_databuku)
    if request.POST:
        form=FormDatabuku(request.POST,instance=databukus)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_buku',id_databuku=id_databuku)
    else:
        form=FormDatabuku(instance=databukus)
        konteks = {
            'form':form,
            'databukus': databukus
        }
    return render(request,'ubah_buku.html',konteks)

def ubah_lg(request, id_datapeminjaman):
    datapeminjamans=Datapeminjaman.objects.get(id=id_datapeminjaman)
    if request.POST:
        form=FormDatapeminjaman(request.POST,instance=datapeminjamans)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_lg',id_datapeminjaman=id_datapeminjaman)
    else:
        form=FormDatapeminjaman(instance=datapeminjamans)
        konteks = {
            'form':form,
            'datapeminjamans': datapeminjamans
        }
    return render(request,'ubah_lg.html',konteks)

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