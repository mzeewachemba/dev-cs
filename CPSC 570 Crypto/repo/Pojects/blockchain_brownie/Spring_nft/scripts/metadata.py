import os
import json
from scripts.pinata import upload_folder, get_pinned

def create_metadata(img_dir, metadata_dir):
    pinned = get_pinned()
    base_ipfs = pinned['images'] if 'images' in pinned else upload_folder(img_dir)

    if not os.path.exists(metadata_dir):
        os.mkdir(metadata_dir)

    metadatas = []
    for idx, file in enumerate(os.listdir(img_dir)):
        metadata_file_path = f'{metadata_dir}/{idx+1}.json'
        logo_name = file.split('.')[0]
        metadata = {
            "name": logo_name,
            "description": f'1174066: {logo_name}',
            "image": f'ipfs://{base_ipfs}/{idx+1}',
            "attributes": {
                "logo_size": idx * 2,
                "Powerlevel": idx ** 4
            }
        }
        metadatas.append(metadata)

        with open(metadata_file_path, 'w') as f:
            json.dump(metadata, f, indent=4)

    return metadatas

if __name__ == "__main__":
    create_metadata(".//images//", ".//metadata//")
    upload_folder(".//metadata//")
