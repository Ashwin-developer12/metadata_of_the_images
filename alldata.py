from PIL import Image
import exifread
import json
import cv2 as cv
import os

json_objects = []
def extract_metadata(image_path):
    try:
        
        with open(image_path, 'rb') as img_file:
            
            tags = exifread.process_file(img_file)
            metadata = {}
            if tags is None:
                return {}
            name = os.path.basename(image_path)
            print(name)
            try:
                metadata['name'] = name
                size = cv.imread(image_path)
                metadata['shape'] = size.shape
            except:
                pass
            
            for tag, value in tags.items():
                print(f"Tag: {tag}, Value: {value}")
                metadata[tag] = str(value)
    except (IOError, ValueError):
        print("Error while processing the image.")
    return metadata

image_folder = r"C:\Users\user\Desktop\Jupyter\Internship img task"#Provide the folder path where are all the images are stored.
output_file = "metadata2.json"
metadata_list = []
for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(image_folder, filename)
            metadata = extract_metadata(image_path)
            metadata_list.append(metadata)

with open(output_file, 'w') as json_file:
    json.dump(metadata_list, json_file, indent=4)
