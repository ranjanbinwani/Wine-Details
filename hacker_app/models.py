from django.db import models

# Create your models here.

class WineDetailManager():

    def create_wine(self, country, description, designation, points, price, province, region_1, region_2, variety, winery):

        wine = self.model(country=country, description=description, designation=designation, points=points, price=price, province=province, region_1=region_1, region_2=region_2, variety=variety, winery=winery)
        wine.save(using=self._db)

        return wine

class WineDetail(models.Model):

    country = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=255, default='')
    designation = models.CharField(max_length=50, default='')
    points = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    province = models.CharField(max_length=50, default='')
    region_1 = models.CharField(max_length=50, default='')
    region_2 = models.CharField(max_length=50, default='')
    variety = models.CharField(max_length=255, default='')
    winery = models.CharField(max_length=255, default='')

    objects = WineDetailManager()

    def get_wine_desc(self):
        
        return self.description

    def __str__(self):
        return self.description
