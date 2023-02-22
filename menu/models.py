from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.title  

class MenuItem(models.Model):
    title = models.CharField(max_length=150)
    Image = models.ImageField(upload_to="food/")
    categories = models.ManyToManyField("menu.Category")


    class Meta:
        verbose_name_plural = "menu_item"
        
    def __str__(self):
        return self.title  