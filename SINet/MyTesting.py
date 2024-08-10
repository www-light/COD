import locale
print("123",locale.getpreferredencoding())  # 检查默认编码
import os
import torch
import torch.nn.functional as F
import numpy as np
#from scipy import misc
import cv2
from .lib.Network_Res2Net_GRA_NCD import Network
from .utils.data_val import test_dataset


def SINet():
    testsize=352
    pth_path='./SINet/snapshot/SINet_V2/Net_epoch_best.pth'

    _data_name='INPUT'
    out_put='OUTPUT'

    data_path = './SINet/Dataest/TestDataest/{}/'.format(_data_name)
    save_path = './SINet/res/{}/{}/'.format(pth_path.split('/')[-2], out_put)
    # 创建模型实例
    model = Network(imagenet_pretrained=False)
    # 加载模型权重
    model.load_state_dict(torch.load(pth_path))
    # 将模型转移到GPU上
    model.cuda()
    # 设置模型为评估模式
    model.eval()

    os.makedirs(save_path, exist_ok=True)
    image_root = '{}Imgs/'.format(data_path)#Images 指的是图像数据，即实际用于输入模型、进行处理或显示的图像文件
    #gt_root = '{}/GT/'.format(data_path)#GT 是指已知的、人工标注的、准确的结果或标签，作为模型训练或评估的参考标准
    test_loader = test_dataset(image_root,testsize)


    for i in range(test_loader.size):
        image, name, _ = test_loader.load_data()
        image = image.cuda()
        print("name:",name)
        # Forward pass through the model to get the output
        res5, res4, res3, res2 = model(image)
        res = res2

        # Apply sigmoid activation and prepare for saving
        res = res.sigmoid().data.cpu().numpy().squeeze()

        # Normalize the result to the range [0, 1]
        res = (res - res.min()) / (res.max() - res.min() + 1e-8)
        print('> {} - {}'.format(_data_name, name))

        # Save the result using cv2
        # 假设读取到的文件名是乱码
        cv2.imencode('.jpg', res*255)[1].tofile(save_path + name)
        #cv2.imwrite(save_path + name, res * 255)
