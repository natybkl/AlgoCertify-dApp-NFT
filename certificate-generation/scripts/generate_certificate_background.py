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
Generate a professional and clean certificate template.  
The certificate should have enough space for the recipient's Full Name, a Logo, Date. 
The design should feature a space for a logo at the top, followed by a central header stating "Certificate of Achievement." Below the header, include areas for the recipient's Full Name and the achieved Description. 
Provide a section for the Date and a Signature line at the bottom.
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
