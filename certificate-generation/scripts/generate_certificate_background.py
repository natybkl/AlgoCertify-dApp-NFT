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
Design a certificate template which includes placeholders for the recipient's name, the date, and a logo. 

Make sure to include the following no matter what:
- Placeholder for recipient's name as: <<NAME>>
- Placeholder for the date as: <<DATE>>
- Placeholder for the logo as: ![Logo Placeholder Image](https://github.com/natybkl/AlgoCertify-dApp-NFT/blob/feature/certificate-generation/certificate-generation/assets/images/logo.png)
- Placeholder for the Signiture as : <<SIGNITURE>>

Example:
![Certificate Template Example](https://github.com/natybkl/AlgoCertify-dApp-NFT/blob/feature/certificate-generation/certificate-generation/assets/images/Certificate%20Template.png)

Please generate a certificate template based on the provided specifications. Browse the links provided before generating the image.
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
