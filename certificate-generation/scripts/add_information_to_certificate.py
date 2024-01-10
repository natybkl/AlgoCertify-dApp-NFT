import os
import datetime
import cv2

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"

# Get today's date
todays_date = datetime.date.today().strftime("%B %d, %Y")

# Load logo
logo_filename = "../assets/images/10ac.jpg"
logo = cv2.imread(logo_filename)
# Get original dimensions
original_width = logo.shape[1]
original_height = logo.shape[0]

# Calculate half values
new_width = int(original_width / 7)
new_height = int(original_height / 7)

new_width_2 = int(original_width / 14)
new_height_2 = int(original_height / 14)


# Resize using calculated values
resized_logo = cv2.resize(logo, (new_width, new_height))
resized_logo_2 = cv2.resize(logo, (new_width_2, new_height_2))

# Load base template image
base_template_filename = "../generated_certificates/certificate_background.jpg"
base_template_image = cv2.imread(base_template_filename)

# Create a copy of the base template for modification
certificate_image = base_template_image.copy()
achievement_text = f"This certificate is proudly presented to {full_name} in recognition of"
achievement_text_2 = f"their dedication.and perseverance in completing the challenging" 
achievement_text_3 = f"week-long program that concluded on {todays_date}."
# Positions for text and logo (adjust based on your certificate design)
name_position = (285, 750)
logo_position = (450, 710)  # Assuming logo is smaller than name text
date_position = (600, 750)

# Example using a different font for each text
name_font = cv2.FONT_HERSHEY_COMPLEX
date_font = cv2.FONT_HERSHEY_COMPLEX
achievement_font = cv2.FONT_HERSHEY_COMPLEX

print(f"Certificate = (X:{certificate_image.shape[0]}, Y:{certificate_image.shape[1]})")
print(f"Logo = (X:{resized_logo.shape[0]}, Y:{resized_logo.shape[1]})")
# Add text and logo to the certificate image (copy of the base template)

cv2.putText(certificate_image, achievement_text, (290, 440), achievement_font, 0.37, (150, 0, 0), 1, cv2.LINE_AA)
cv2.putText(certificate_image, achievement_text_2, (290, 475), achievement_font, 0.37, (150, 0, 0), 1, cv2.LINE_AA)
cv2.putText(certificate_image, achievement_text_3, (290, 520), achievement_font, 0.37, (150, 0, 0), 1, cv2.LINE_AA)

cv2.putText(certificate_image, full_name, name_position, name_font, 0.58, (0, 0, 0), 1, cv2.LINE_AA)
certificate_image[logo_position[1] : logo_position[1] + resized_logo.shape[0], logo_position[0] : logo_position[0] + resized_logo.shape[1]] = resized_logo
certificate_image[350: 350 + resized_logo_2.shape[0], 480 : 480 + resized_logo_2.shape[1]] = resized_logo_2
cv2.putText(certificate_image, todays_date, date_position, date_font, 0.52, (0, 0, 0), 1 , cv2.LINE_AA)

# Save the final certificate
# Save the final certificate
final_certificate_filename = f"../final_certificates/{full_name}_certificate.jpg"
cv2.imwrite(final_certificate_filename, certificate_image)

print(f"Final certificate generated and saved to: {final_certificate_filename}")
