# from django.test import TestCase
# from django.urls import reverse
# from.models import Animal, AnimalGuess

# class CheckAnimalNameViewTest(TestCase):
#     def setUp(self):
#         # 在测试开始前创建一些测试数据
#         Animal.objects.create(name='仓鼠', image_name='hamster_image')

#     def test_correct_animal_name(self):
#         response = self.client.post(reverse('backend:check_animal_name'), data={'user_input': '仓鼠', 'image_name': 'hamster_image'})
#         self.assertEqual(response.json()['result'], True)

#     def test_incorrect_animal_name(self):
#         response = self.client.post(reverse('backend:check_animal_name'), data={'user_input': '兔子', 'image_name': 'hamster_image'})
#         self.assertEqual(response.json()['result'], False)
