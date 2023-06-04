import cv2
import numpy as np
from PIL import Image, ImageEnhance

def remove_shadow(img: np.ndarray):
    dilated_img = cv2.dilate(img, np.ones((10,10), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(img, bg_img)
    return diff_img


def greyscale(img: np.ndarray):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def binarize(img: np.ndarray, min=0, max=255, invert: bool = True):
    thresh = cv2.THRESH_BINARY_INV if invert is True else cv2.THRESH_BINARY
    thresh += cv2.THRESH_OTSU
    thresh_val, thresh_img = cv2.threshold(img, 0, 255, thresh)
    return thresh_img

def erode(img: np.ndarray, x_morph: int = 3, y_morph: int = 3, iterations: int = 1):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x_morph,y_morph))
    return cv2.erode(img, kernel, iterations=iterations)

def dilate(img: np.ndarray, x_morph: int = 3, y_morph: int = 3, iterations: int = 1):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x_morph,y_morph))
    return cv2.dilate(img, kernel, iterations=iterations)

def get_cnts(dilated_img: np.ndarray):
    cnts = cv2.findContours(dilated_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
    return cnts

def denoise(img: np.ndarray, h=10, template_window_size=7, search_window_size=11, is_grey = False):
    if is_grey is True:
        return cv2.fastNlMeansDenoising(img, None, h, template_window_size, search_window_size)
    else:
        return cv2.fastNlMeansDenoisingColored(img, None, h, template_window_size, search_window_size)

def clean_img(img: np.ndarray, min=0, max=1, invert=True):
    img = greyscale(img)
    img = remove_shadow(img)
    img = denoise(img, is_grey=True)
    img = binarize(img, min=min, max=max, invert=invert)
    return img

def scale_image(image, scale_factor):
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    return image.resize((new_width, new_height), Image.ANTIALIAS)

def enhance_image(image):
    # Enhance image brightness
    brightness_enhancer = ImageEnhance.Brightness(image)
    enhanced_image = brightness_enhancer.enhance(1.5)
    
    # Enhance image contrast
    contrast_enhancer = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = contrast_enhancer.enhance(1.5)
    
    return enhanced_image
