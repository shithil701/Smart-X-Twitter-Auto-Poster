import os
import requests
from urllib.parse import urlparse


def download_image(url, save_folder='temp_images'):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    # Extract filename from URL
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path) or 'twitter_image.jpg'
    filepath = os.path.join(save_folder, filename)
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    
    return filepath

image_url = "https://m.media-amazon.com/images/I/81UQDoHG7pL._AC_SY355_.jpg"
local_path = download_image(image_url)
current_path = os.getcwd()
the_path = current_path + "\\" + local_path
final_path = the_path.replace("\\", "\\\\")
print(final_path)
