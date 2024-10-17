from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    dob = models.DateField(auto_now=False)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)
    location = models.TextField()
    pimage= models.ImageField(upload_to="pimages",blank=True)
    doc = models.FileField(upload_to="rdocs",blank=True)
    