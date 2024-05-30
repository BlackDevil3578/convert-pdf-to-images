import os
import fitz  # PyMuPDF
from PIL import Image


def pdf_to_images(pdf_path):
    # Extract the base name of the PDF file (without extension)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Create the output folder named after the PDF file
    output_folder = f"{base_name}_images"
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_document)):
        # Select the page
        page = pdf_document.load_page(page_num)

        # Render the page to a pixmap (image)
        pix = page.get_pixmap()

        # Convert the pixmap to an image
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        image.save(image_path)

    # Close the PDF file
    pdf_document.close()

    print(f"PDF pages saved as images in '{output_folder}'")


# Example usage
pdf_to_images('SAHIH Al BUKHARI - ARABIC.pdf')
