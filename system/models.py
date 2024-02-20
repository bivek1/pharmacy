from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length = 300)
    generic_name = models.CharField(max_length = 300)
    mg_dose = models.CharField(max_length = 200)
    exipiry_date = models.DateField()
    manufacture_date = models.DateField()

    objects = models.Manager()


    def __str__(self):
        return self.name
    
class QR(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = "qr/", null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.name