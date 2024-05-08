from django.db import models

# Create your models here.
class Kasir(models.Model):
    nama_barang = models.CharField(max_length=100)
    harga = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama_barang
