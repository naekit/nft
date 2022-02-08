from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_school
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        school = get_school(advanced_collectible.tokenIdToSchool(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{school}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = school
            collectible_metadata["description"] = f"A powerful {school}wiz!"
            image_path = "./img/" + school.lower().replace("_", "-") + "wizard.png"
            image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        PINATA_BASE_URL = "https://api.pinata.cloud/"
        endpoint = "pinning/pinFileToIPFS"
        filename = filepath.split("/")[-1:][0]
        headers = {
            "pinata_api_key": os.getenv("PINATA_API_KEY"),
            "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
        }
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        ipfs_hash = response.json()["IpfsHash"]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
