import json
import logging

from urllib.parse import urlparse
from pathlib import Path

import requests

API_URL = "https://ll.thespacedevs.com/2.0.0/launch/upcoming/"

DATA_DIR = Path("launch_data")
IMAGE_DIR = Path("downloaded_images")

DATA_FILE = DATA_DIR / "data.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def get_launches() -> None:
    """Fetch upcoming launch data and save it as JSON."""
    
    logger.info("Fetching upcoming launch data")
    
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        
    except requests.RequestException as e:
        logger.error("Failed to retrieve launch data: %s", e)
        raise
    
    try:
        data = response.json()
    
    except ValueError as e:
        logger.error("API returned invalid JSON")
        raise ValueError("Invalid JSON response") from e
    


    # Safely create the directory if it does not exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Save the response data to a file
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
    logger.info("Launch data saved to %s", DATA_FILE     )


def save_images() -> None:
    """Download rocket images from the saved launch data."""
    
    logger.info("Reading launch data from %s", DATA_FILE)
    
    try:
        # Open the file in read mode ('r')
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)  # Parses the file back into a dict

    except FileNotFoundError:
        logger.error("Launch data file does not exist: %s", DATA_FILE)
        raise
    
    except json.JSONDecodeError as e:
        logger.error("Launch data contains invalid JSON")
        raise ValueError("Invalid launch data JSON") from e

    results = saved_data.get("results", [])
    
    logger.info("Found %d launches", len(results))
    
    # Create directory if it does not exist
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)


    # loop through image urls
    for launch in results:
        
        # image_url = launch["image"]
        image_url: str = launch.get("image")
        
        if not image_url:
            logger.warning("Launch has no image URL; skipping")
            continue
        
        try: 
            response = requests.get(image_url, stream=True, timeout=10)
            response.raise_for_status()
            
        except requests.RequestException as e:
            logger.error("Failed to download image %s: %s", image_url, e)
            continue
        
        # image_url_split = image_url.split("/")
        # image_name = image_url_split[-1]
        parsed_url = urlparse(image_url)
        image_name = Path(parsed_url.path).name
        
        if not image_name:
            logger.warning("Could not determine filename from URL: %s", image_url)
            continue

        file_path = IMAGE_DIR / image_name

        logger.info("Downloadiing %s", image_name)

        with open(file_path, "wb") as img_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            img_file.write(chunk)
                            
        logger.info("Saving image to %s", file_path)  
        
        
        
def main() -> None:
    get_launches()
    save_images()                  

if __name__ == "__main__":
    main()                                               