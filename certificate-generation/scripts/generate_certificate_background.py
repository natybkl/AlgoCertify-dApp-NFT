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
You are working on a project to generate certificate templates using the DALL·E model. The goal is to create a visually appealing and customizable design that can be used for various certificate types.

Prompt:
Design a certificate template using the DALL·E model. The template should include placeholders for the recipient's name, the date, and a logo. The placeholders should be visually distinct and easily identifiable. The overall design should be professional and elegant. Consider incorporating decorative elements, borders, and appropriate typography. Provide options for different color schemes and layout variations. The generated template should be in a high-resolution image format (e.g., PNG) suitable for printing.

Specifications:
- Placeholder for recipient's name: <<NAME>>
- Placeholder for the date: <<DATE>>
- Placeholder for the logo: '..assets/images/logo.png'
- Placeholder for the Signiture: <<SIGNITURE>>
- Visual distinctiveness: Ensure the placeholders stand out from the rest of the design.
- Professional and elegant design: Incorporate appropriate decorative elements, borders, and typography.
- Color schemes and layout variations: Provide options for different color schemes and layout variations to accommodate various certificate types.
- High-resolution image format: Generate the template as a high-resolution image suitable for printing, such as PNG.

Example:
![Certificate Template Example]('../assets/images/Certificate Template.png')

Please generate a certificate template based on the provided specifications. Make sure to incorporate the necessary placeholders and design elements. Feel free to be creative and provide multiple design options if possible.
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
