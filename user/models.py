from django.db import models



class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "user_table"
        
    def __str__(self):
        return self.name