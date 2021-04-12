'''
The real world use case of mosaic data augmentation
'''

import sys
sys.path.append("..")
import os
from skimage import io
from convertmask.utils.auglib.optional.mosaic import mosiacScript_no_reshape


if __name__ == "__main__":
    SAVE_DIR = r'E:\Dataset\SpecialVehicle\mosaic_test_result'
    XML_DIR = r'E:\Dataset\SpecialVehicle\mosaic_test_annotation'
    IMG_DIR = r'E:\Dataset\SpecialVehicle\mosaic_test_image'
    xml_list = os.listdir(XML_DIR)
    img_list = os.listdir(IMG_DIR)
    assert len(xml_list) == len(img_list)
    no_process_num = len(img_list) % 4  # The last "no_process_num" files will not be processed
    print(f'no_process_num is {no_process_num}')
    for i in range(0, len(xml_list)-no_process_num, 4):
        img1 = io.imread(os.path.join(IMG_DIR, img_list[i]))
        img2 = io.imread(os.path.join(IMG_DIR, img_list[i+1]))
        img3 = io.imread(os.path.join(IMG_DIR, img_list[i+2]))
        img4 = io.imread(os.path.join(IMG_DIR, img_list[i+3]))

        xml1 = os.path.join(XML_DIR, xml_list[i])
        xml2 = os.path.join(XML_DIR, xml_list[i+1])
        xml3 = os.path.join(XML_DIR, xml_list[i+2])
        xml4 = os.path.join(XML_DIR, xml_list[i+3])
        mosiacScript_no_reshape([img1, img2, img3, img4],
                                [xml1, xml2, xml3, xml4], SAVE_DIR,
                                True)
