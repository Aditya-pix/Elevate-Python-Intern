import os 
from PIL import Image

base_dir = os.path.dirname(os.path.abspath(__file__))

input_folder = os.path.join(base_dir,'input_images')
output_folder = os.path.join(base_dir,'output_images')

os.makedirs(output_folder, exist_ok=True)

desired_size= (300,300)
for image in os.listdir(input_folder):
    try:
        img_path =os.path.join(input_folder, image)
        with Image.open(img_path) as img:
            resize_img = img.resize(desired_size)

            new_filename = os.path.splitext(image)[0] + ".png"
            save_path = os.path.join(output_folder,new_filename)
            resize_img.save(save_path)

            print(f"Successful Processing {image}")
    except Exception as e:
        print(f"Error Processing {image}: {e}")
