import os
import sys
sys.path.append(os.getcwd())

import base64, os, shutil
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from django.conf import settings
from SINet.MyTesting import SINet
from django.http import JsonResponse

UPLOAD_FOLDER = os.path.join(settings.BASE_DIR, 'SINet','Dataest','TestDataest','INPUT','Imgs')
RESULT_FOLDER=os.path.join(settings.BASE_DIR, 'SINet','res','SINET_V2','OUTPUT')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class upload_images(APIView):
    parser_classes = (MultiPartParser, FormParser)#
    def post(self,request,*args,**kwargs):
        #请求中是否包含要识别的图像
        file=request.FILES.get('image')
        if not file:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)
        filename=file.name
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        #调用检测模型
        SINet()
        #清理上传的文件
        shutil.rmtree(UPLOAD_FOLDER)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        #返回结果
        Extract_image_path=os.path.join(RESULT_FOLDER,filename)
        print("path:",Extract_image_path)
        if not os.path.isfile(Extract_image_path):
            return JsonResponse({'error': 'Image not found'}, status=404)
        
        try:
            with open(Extract_image_path, 'rb') as img_file:
                image_data = img_file.read()
                image_base64 = base64.b64encode(image_data).decode('utf-8')

            response_data={
                'image':image_base64,
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
