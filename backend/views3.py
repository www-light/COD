from django.shortcuts import render
from django.http import JsonResponse
from.models import Animal, AnimalGuess

def check_animal_name(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', None)
        image_name = request.POST.get('image_name', None)
        correct_name = Animal.objects.filter(image_name=image_name).values_list('name', flat=True).first()
        is_correct = user_input == correct_name if correct_name else False
        AnimalGuess.objects.create(user_input=user_input, is_correct=is_correct)
        return JsonResponse({'result': is_correct})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)