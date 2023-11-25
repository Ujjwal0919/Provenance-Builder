from PIL import Image, ImageDraw, ImageFont


def print_alert(message):
    # ANSI escape code for red color
    red_color = "\033[91m"

    # ANSI escape code to reset text formatting
    reset_color = "\033[0m"

    # Print the message with red color and a red flag
    print(f"{red_color}🚩 ALERT: {message}{reset_color}")


def print_success(message):
    # ANSI escape code for green color
    green_color = "\033[92m"

    # ANSI escape code to reset text formatting
    reset_color = "\033[0m"

    # Print the message with green color and a green flag
    print(f"{green_color}🚩 SUCCESS: {message}{reset_color}")


def display_images_with_captions(image1_path, image2_path, caption1, caption2):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Ensure both images have the same width
    min_width = max(image1.width, image2.width)
    image1 = image1.crop((0, 0, min_width, image1.height))
    image2 = image2.crop((0, 0, min_width, image2.height))

    # Create a new image to display both images with captions
    combined_width = min_width
    combined_height = image1.height + image2.height + 40  # Add space for captions
    combined_image = Image.new('RGB', (combined_width, combined_height))

    # Paste the first image on top
    combined_image.paste(image1, (0, 0))

    # Paste the second image below with separation
    combined_image.paste(image2, (0, image1.height + 40))

    # Add captions above each image
    draw = ImageDraw.Draw(combined_image)
    font = ImageFont.load_default()  # You can customize the font and size

    caption1_position = (10, image1.height - 30)
    caption2_position = (10, image1.height + 10)

    draw.text(caption1_position, caption1, fill='white', font=font)
    draw.text(caption2_position, caption2, fill='white', font=font)

    # Display the combined image
    combined_image.show()
