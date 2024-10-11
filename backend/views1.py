# from django.shortcuts import render, json_response 
from rest_framework.views import APIView 
from django.http import JsonResponse  
from .models import Problems  
import random  
import base64
  
def get_random_animal(request): 
    animals = Problems.objects.all()  
    if animals.exists(): 
        random_id = random.randint(1, animals.count()) 
        random_animal = animals.get(id=random_id) 
        # 对图片进行处理
        img_base64 = base64.b64encode(random_animal.animals_skeleton_image.read()).decode('utf-8')
        data = {  
            'image': img_base64,
            'name': random_animal.animals_name,  
            'problem': random_animal.problem_info,  
        }  
        print(data['name'])
        return JsonResponse(data)  
    else:  
        return JsonResponse("No animals available", status=404)
