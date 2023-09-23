import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import textwrap
import PIL.ImageFont as ImageFont

def text_to_image(text, filename, font_size=16, font_path='arial.ttf', font_color='black', background_color='white', image_width=800):


    # Create a new image.
    image = Image.new('RGB', (image_width, 500), background_color)

    # Create a drawing context.
    draw = ImageDraw.Draw(image)

    # Load the font file.
    font = ImageFont.truetype(font_path, font_size)

    # Wrap the text to fit within the image width.
    lines = textwrap.wrap(text, width=(image_width // font_size))

    # Calculate the total height of the text.
    total_height = len(lines) * font_size

    # Calculate the vertical centering position.
    y = (image.height - total_height) // 2

    # Draw the text onto the image.
    for line in lines:
        draw.text((0, y), line, font=font, fill=font_color)
        y += font_size

    # Save the image in a compressed format.
    image.save(filename, 'PNG')

# Example usage:

text = """Validated
cf94198dfa0679e7460e5d2a087b710128498fce8c3076d6bfba1307618fbaeb"""

# Convert the text to an image and save it to the file 'text.png'.
text_to_image(text, 'text9.png', font_size=20, image_width=800)
