import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

# Load environment variables
load_dotenv()

# Assuming you have an instance of OpenAI named 'client'
client = OpenAI()

# Set API key
api_key = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = api_key

# Load the base certificate background image
base_image_filename = "../generated_certificates/certificate_background.jpg"
with open(base_image_filename, "rb") as image_file:
    base_image = image_file.read()

# Generate variations
response = client.images.create_variation(
    image=base_image,
    n=5,  # Number of variations to generate
    size="1792x1024"  # Maintain the same size as the base image
)

# Save the variations
for i, variation_data in enumerate(response.data):
    variation_url = variation_data.url
    variation_image = requests.get(variation_url)

    filename = f"../generated_certificates/certificate_variation_{i+1}.jpg"
    with open(filename, "wb") as image_file:
        image_file.write(variation_image.content)

    print(f"Certificate variation {i+1} generated and saved to: {filename}")