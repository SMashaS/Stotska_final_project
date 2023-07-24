import requests
import os
url = 'https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg'
if not os.path.exists('images'):
    os.mkdir('images')
file_name = os.path.join('images', url.split('/')[-1])
response = requests.get(url)
with open(file_name, 'wb') as f:
    f.write(response.content)
