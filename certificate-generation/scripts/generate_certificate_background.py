import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = api_key

# Define your prompt
prompt = """
I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS.

Design a certificate template which have enough space for the recipient's name, the date, and a logo. It should be light red and white themed. 

Example:
![Certificate Template Example](https://github.com/natybkl/AlgoCertify-dApp-NFT/blob/feature/certificate-generation/certificate-generation/assets/images/Certificate%20Template.png)

"""

# Assuming you have an instance of OpenAI named 'client'
client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

# Save the generated background to a file
background_image_url = response.data[0].url
background_image = requests.get(background_image_url)

with open('../generated_certificates/certificate_background.jpg', 'wb') as image_file:
    image_file.write(background_image.content)

print("Certificate background generated and saved.")
