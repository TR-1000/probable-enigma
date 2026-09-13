import json
import requests

from pathlib import Path


def get_launches() -> None:
    # Get upcoming launch data
    upcoming_launch_url = "https://ll.thespacedevs.com/2.0.0/launch/upcoming/"

    response = requests.get(upcoming_launch_url)
    data = response.json()

    # Define the directory and file path
    output_dir = Path("launch_data")
    file_path = output_dir / "data.json"  # The / operator combines paths

    # Safely create the directory if it does not exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save the file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def save_images() -> None:

    # Open the file in read mode ('r')
    with open('launch_data/data.json', 'r', encoding='utf-8') as file:
        saved_data = json.load(file)  # Parses the file back into a dict

    # print(json.dumps(saved_data, indent=4))
    

    results = saved_data["results"]

    # print(json.dumps(results, indent=4))

    # Define and create image directory
    image_dir = Path("downloaded_images")
    image_dir.mkdir(parents=True, exist_ok=True)

    # loop through image urls
    for launch in results:
        # print(launch["image"])
        image_url = launch["image"]

        response = requests.get(image_url, stream=True, timeout=10)

        image_url_split = image_url.split("/")

        image_name =image_url_split[-1]

        print(image_name)

        file_path = f"{image_dir}/{image_name}"


        with open(file_path, "wb") as img_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        img_file.write(chunk)