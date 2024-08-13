from django.db import models

# Create your models here.

class Film(models.Model):
    isim = models.CharField(max_length=50, null = True, blank = True)
    aciklama = models.TextField(null = True, blank = True)
    yuklenme_tarihi = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    resim = models.FileField(upload_to = 'resimler/', verbose_name="Film Resmi", null = True, blank = True)

    def __str__(self):
        return self.isim
    
    