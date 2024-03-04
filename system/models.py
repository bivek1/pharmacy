from django.db import models

# Create your models here.

class Location(models.Model):
    
    location = models.CharField(max_length = 200)

    objects = models.Manager()


    def __str__(self):
        return str(self.location)
    
class Medicine(models.Model):
    name = models.CharField(max_length = 300)
    generic_name = models.CharField(max_length = 300)
    mg_dose = models.CharField(max_length = 200)
    stock = models.IntegerField()
    exipiry_date = models.DateField()
    manufacture_date = models.DateField()
    location = models.ForeignKey(Location, related_name = "medicine_location", on_delete=models.CASCADE, null = True, blank = True)

    objects = models.Manager()


    def __str__(self):
        return self.name





class QR(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = "qr/", null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.name