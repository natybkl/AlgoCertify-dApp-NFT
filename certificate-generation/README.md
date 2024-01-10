# Certificate Generation

This project focuses on generating certificates using Web3 technologies, incorporating decentralized elements such as Algorand Blockchain and NFTs.

## Prerequisites

Before running any scripts in this repository, ensure that you have set up the necessary environment variables. Create a `.env` file in the root directory with the following content:

``````bash
OPENAI_API_KEY=your_openai_api_key_here
``````
Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Folder Structure

- **assets/:** Store font files and logo images.
  - *fonts/:* Place your font file (e.g., arial.ttf) here.
  - *images/:* Place your logo image (e.g., company_logo.png) here.

- **generated_certificates/:** Save generated certificate backgrounds and variations.
  - *certificate_background.jpg:* Generated certificate base background.
  - *variation_1.jpg, variation_2.jpg, ...:* Generated variations.

- **final_certificates/:** Save the final certificates with added information.
  - *final_certificate.jpg:* Final certificate with information.

- **scripts/:** Keep your Python scripts here.
  - *generate_certificate_background.py:* Generate certificate base background using DALL·E.
  - *generate_certificate_variations.py:* Generate variations of certificate backgrounds.
  - *add_information_to_certificate.py:* Add information dynamically to the certificate.

- **README.md:** Documentation and usage instructions.

## Usage Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/natybkl /AlgoCertify-dApp-NFT.git
   cd certificate-generation/scripts

2. **Generate Certificate Base Background**

    Edit the prompt in generate_certificate_background.py if you want to create a new certificate background.

    Run the script:
    ``````bash
    python generate_certificate_background.py
    ``````
    The generated background will be saved in the generated_certificates/ folder.

3. **Generate Variations**

    Run the script to generate variations of the certificate background:
    ``````bash
    python generate_certificate_variations.py
    ``````
    Multiple variations will be saved in the generated_certificates/ folder.

4. **Add Information to Certificate**

    Run the script to add information dynamically to the certificate:
    ``````bash
    python add_information_to_certificate.py
    ``````
    The script will prompt you to provide names for the certificate. It will then automatically generate the custom certificate and save it in the final_certificates/ folder.

