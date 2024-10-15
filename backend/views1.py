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
        origin_img_base64 = base64.b64encode(random_animal.animals_origin_image.read()).decode('utf-8')
        skeletion_img_base64 = base64.b64encode(random_animal.animals_skeleton_image.read()).decode('utf-8')
        data = { 
            'problem_number':random_animal.problem_number,
            'problem_info': random_animal.problem_info,
            'animals_info': random_animal.animals_info,
            'animals_name': random_animal.animals_name,
            'animals_origin_image': origin_img_base64,
            'animals_skeletion_image': skeletion_img_base64,
            'animals_skeleton_image_url':  random_animal.animals_skeleton_image.url,
        }  
        print(data['animals_name'])
        return JsonResponse(data)  
    else:  
        return JsonResponse("No animals available", status=404)