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
Generate a beautiful and professional certificate base background suitable for acknowledging achievements. 
The design should incorporate elegant graphics, a subtle color palette, and a clean layout. 
The certificate should have space for the recipient's Full Name, a Logo, Date, and other relevant information. 
The overall style should convey a sense of accomplishment and formality.
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
