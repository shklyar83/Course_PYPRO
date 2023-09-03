from django.db import models


class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'
    

class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')
    is_visible = models.BooleanField(default=True)


class About(models.Model):
    desc = models.TextField(max_length=2000)
    order_table = models.TextField(max_length=50)
    photo = models.ImageField(upload_to='about/')
    video = models.FieldFile(upload_to='about_video/')


class Events(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='events/', blank=True)
    video = models.FieldFile(upload_to='events_video/')
    is_visible = models.BooleanField(default=True)


class Chefs(models.Model):
    name = models.CharField(max_length=50, unique=True)
    surname = models.CharField(max_length=50, unique=True)
    position_level = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='chefs/', blank=True)
    social_twitter = models.URLField(blank=True)
    social_facebook = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    is_visible = models.BooleanField(default=True)







    
    
