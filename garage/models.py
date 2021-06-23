from django.db import models
from django.urls import reverse

class Car(models.Model):
    vin = models.CharField(max_length = 100, blank=True)
    make = models.CharField(max_length = 100, blank= True)
    model = models.CharField(max_length = 100, blank = True)
    engine = models.CharField(max_length = 100, blank= True)
    interior_color = models.CharField(max_length = 100, blank= True)
    body_color = models.CharField(max_length = 100, blank= True)
    year = models.IntegerField()
    image = models.ImageField(upload_to="carsimage", blank=True)
    image_url = models.URLField(blank=True)
    speed = models.DecimalField(blank=True, max_digits = 6, decimal_places=1)


    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.model, self.make, self.engine, self.body_color, self.year)

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})