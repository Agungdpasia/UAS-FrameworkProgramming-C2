from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis
from .models import Transaksi
from .models import Detailtrans
#presentasi
from .models import Databuku
from .models import Datapeminjaman

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields= ['kodebrg','nama']
    list_filter= ('jenis_id',)
    list_per_page= 5
#presentasi
class kolomDatabuku(admin.ModelAdmin):
    list_display = ['no','judul','penulis','penerbit','tahunterbit','tebal']
    search_fields= ['no','judul','penulis','penerbit','tahunterbit','tebal']
    list_filter= ('tahunterbit',)
    list_per_page= 5
    
class kolomDatapeminjaman(admin.ModelAdmin):
    list_display = ['no','nama','jenisbuku','tglpinjam']
    search_fields= ['no','nama','jenisbuku','tglpinjam']
    list_filter= ('nama',)
    list_per_page= 5

admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)
#presentasi
admin.site.register(Databuku, kolomDatabuku)
admin.site.register(Datapeminjaman, kolomDatapeminjaman)

