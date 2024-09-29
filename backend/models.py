from django.db import models

# Create your models here.

class Problems(models.Model):
    problem_number=models.IntegerField(unique=True)
    problem_info=models.TextField()
    animals_info=models.TextField()
    animals_name = models.CharField(max_length=100,default="Unnamed")
    animals_origin_image=models.ImageField(upload_to='problems/origin',blank=True,null=True)
    animals_skeleton_image=models.ImageField(upload_to='problems/skeleton',blank=True,null=True)