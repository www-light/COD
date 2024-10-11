from django.shortcuts import render
from django.http import JsonResponse
from .models import Problems
import base64

def check_animal_name(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', None)
        image_name = request.POST.get('image_name', None)
        
        # 删减轮廓图的url
        image_name = image_name[len('/media/'):] 

        # 匹配轮廓图的url
        correct_name = Problems.objects.filter(animals_skeleton_image=image_name).values_list('animals_name', flat=True).first()

        is_correct = user_input == correct_name if correct_name else False

        return JsonResponse({'result': is_correct})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)