import pyperclip
from google_images_search import GoogleImagesSearch

def get_key():
    with open("api_key.txt", "r") as keyfile:
        return keyfile.readline()

cx = "e0bfeec5bb1f2dbd2"
client = GoogleImagesSearch(get_key(), cx)

search_query = input("Noogle: ")
fileType = "jpg"

search_params = {
    'q': search_query,
    'num': 1,
    'safe': 'medium',
    'fileType': fileType,
    'imgSize': 'MEDIUM'
}

save_dir = 'C:\\GitHub\\quick image\\saved_images\\'

client.search(search_params=search_params, path_to_dir = save_dir, custom_image_name=search_query)

filepath = save_dir + search_query + '.' + fileType
print(filepath)
with open("most_recent_image", "w") as filepathfile:
    filepathfile.write(filepath)
