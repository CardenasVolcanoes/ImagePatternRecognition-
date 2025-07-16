import cv2
import pytesseract
import xml.etree.ElementTree as ET

def get_plate_bbox(annotation_path):
    tree = ET.parse(annotation_path)
    root = tree.getroot()
    for obj in root.findall('object'):
        if obj.find('name').text == 'plate':
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)
            return xmin, ymin, xmax, ymax
    return None

def read_plate(image_path, annotation_path):
    img = cv2.imread(image_path)
    bbox = get_plate_bbox(annotation_path)
    if bbox:
        xmin, ymin, xmax, ymax = bbox
        plate_img = img[ymin:ymax, xmin:xmax]
        plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        plate_bin = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)[1]
        text = pytesseract.image_to_string(plate_bin, config='--psm 8')
        return text, plate_img
    else:
        return "", None