from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

PINATA_BASE_URL = "https://api.pinata.cloud"
ENDPOINT = "/pinning/pinFileToIPFS"

# UPLOAD FILES
def upload_file(filepath):
    filename = filepath.split("/")[-1]

    with open(filepath, "rb") as fp:
        image_binary = fp.read()
    
    response = requests.post(
        PINATA_BASE_URL + ENDPOINT,
        files={"file": (filename, image_binary)},
        headers=headers,
    )

    print(f'http status : {response.status_code}')


    if response.status_code != 200:
        pass

    hash = response.json()["IpfsHash"]
    print(f'hash is: {hash}')
    return "ipfs//" + hash

# GET THE LIST OF UPLOADD FILES
def get_pinned():
    response = requests.get(PINATA_BASE_URL + '/data/pinList?status=pinned', headers=headers)
    if response.status_code != 200:
        print(response)  # Print the error response
        exit()
    
    response_data = response.json()
    pinned_data = {}

    file_count = response_data['count']
    files = response_data['rows']

    for file in files:
        filename = file['metadata']['name']
        pinned_data[filename] = file['ipfs_pin_hash']

    return pinned_data

# UPLOADING FOLDER
def upload_folder(folderpath):
    all_files = os.listdir(folderpath)
    folder_path = folderpath.split("//")[-2]
    files = [
        ("file", (f'{folder_path}/{idx + 1}', open(folderpath + file, "rb")))
        for idx, file in enumerate(all_files)
    ]

    response = requests.post(
        PINATA_BASE_URL + ENDPOINT,
        files=files,
        headers=headers,
    )

    if response.status_code != 200:
        print(response)
        exit()
    
    hash = response.json()["IpfsHash"]
    return hash


if __name__== "__main__": 
    # ipfs_address = upload_file(".//images/spring_2.jpeg")
    # print(f'get pinned is: {get_pinned()}')
    upload_folder(".//images//")
