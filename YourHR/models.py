from django.db import models

# Create your models here.
class Apply(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    role=models.TextField()
    why=models.TextField()
    resume=models.FileField(upload_to="YourHR/", max_length=250, null=True, default=None)
    date=models.DateField()