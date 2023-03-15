from django.db import models

# LOCATION model for storing locations
class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.locationName
    
# ITEM model for storing item details
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName