import time
from PIL import Image
import numpy as np

def modify_image_and_sum_red(image_path, output_path):
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10

    image = Image.open(image_path)
    pixels = np.array(image)

    modified_pixels = pixels + generated_number
    modified_pixels = np.clip(modified_pixels, 0, 255).astype(np.uint8)

    modified_image = Image.fromarray(modified_pixels)
    modified_image.save(output_path)

    red_sum = np.sum(modified_pixels[:, :, 0])
    
    return red_sum

image_path = 'images/chapter1.jpg'
output_path = 'images/chapter1out.jpg'
red_sum = modify_image_and_sum_red(image_path, output_path)

print('code executed successfully.')
print(red_sum)
