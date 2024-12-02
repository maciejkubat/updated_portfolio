from PIL import Image, ImageDraw
rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

def turtle_in_color(color):
    # Create a new image with a transparent background
    image = Image.new("RGBA", (50, 50), (255, 0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Draw a simple turtle shape (circle for the body and smaller circles for the legs and head)
    draw.ellipse((10, 10, 40, 40), fill=color)  # Body
    draw.ellipse((5, 5, 15, 15), fill=color)    # Head
    draw.ellipse((5, 35, 15, 45), fill=color)   # Leg 1
    draw.ellipse((35, 5, 45, 15), fill=color)   # Leg 2
    draw.ellipse((35, 35, 45, 45), fill=color)  # Leg 3
    draw.ellipse((5, 35, 15, 45), fill=color)   # Leg 4

    # Save the image as a PNG file
    image.save(f"{color}_turtle.png")

for color in rainbow_colors:
    color = color.lower()
    turtle_in_color(color)