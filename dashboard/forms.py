from django.forms import ModelForm
from dashboard.models import Barang, Datapeminjaman, Databuku
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'stok' : forms.NumberInput({'class':'form-control'}),
            'harga' : forms.NumberInput({'class':'form-control'}),
            'link_gbr' : forms.TextInput({'class':'form-control'}),
            'jenis_id' : forms.Select({'class':'form-control'}),
        }
        
class FormDatabuku(ModelForm):
    class Meta :
        model=Databuku
        fields='__all__'

        widgets = {
            'no' : forms.TextInput({'class':'form-control'}),
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'tahunterbit' : forms.NumberInput({'class':'form-control'}),
            'tebal' : forms.NumberInput({'class':'form-control'}),
        }
class FormDatapeminjaman(ModelForm):
    class Meta :
        model=Datapeminjaman
        fields='__all__'

        widgets = {
            'no' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jenisbuku' : forms.TextInput({'class':'form-control'}),
            'tglpinjam' : forms.NumberInput({'class':'form-control'}),
        }