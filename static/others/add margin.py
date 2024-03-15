from PIL import Image

def add_margin(pil_img, top, right, bottom, left, color=(0, 0, 0, 0)):
    """
    Add transparent margins to a PIL image.
    
    Args:
        pil_img (PIL.Image): The input PIL image.
        top (int): Size of the top margin (in pixels).
        right (int): Size of the right margin (in pixels).
        bottom (int): Size of the bottom margin (in pixels).
        left (int): Size of the left margin (in pixels).
        color (tuple): Color of the margins in RGBA format (default is transparent).
    
    Returns:
        PIL.Image: The PIL image with transparent margins added.
    """
    width, height = pil_img.size
    new_width = width + left + right
    new_height = height + top + bottom
    new_img = Image.new("RGBA", (new_width, new_height), color)
    new_img.paste(pil_img, (left, top))
    return new_img

# Load the PNG image
input_image_path = "C:/Users/TRETEC/Desktop/Repos/ch7almachyaREACT/ch7almachya/static/others/page_icon_150.png"
output_image_path = "C:/Users/TRETEC/Desktop/Repos/ch7almachyaREACT/ch7almachya/static/others/page_icon_150.png"
img = Image.open(input_image_path)

# Add transparent margins of 20 pixels on all sides
margins = (30, 30, 30, 30)
new_img = add_margin(img, *margins)

# Save the image with transparent margins
new_img.save(output_image_path)