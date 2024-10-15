from django.db import models

# Create your models here.

class Problems(models.Model):
    problem_number=models.IntegerField(unique=True)
    problem_info=models.TextField()
    animals_info=models.TextField()
    animals_name = models.CharField(max_length=100,default="Unnamed")
    animals_origin_image=models.ImageField(upload_to='problems/origin',blank=True,null=True)
    animals_skeleton_image=models.ImageField(upload_to='problems/skeleton',blank=True,null=True)


from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=200)

class AnimalGuess(models.Model):
    user_input = models.CharField(max_length=100)
    is_correct = models.BooleanField()