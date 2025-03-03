from PIL import Image

# Open your 10 image files (adjust the paths as needed)
images = [Image.open(f"tile{i}.png") for i in range(1, 11)]  # tile1.png, tile2.png, ..., tile10.png

# Create a blank canvas for the grid (5 tiles per row, 2 rows)
grid_width = images[0].width * 5  # 5 tiles per row
grid_height = images[0].height * 2  # 2 rows of tiles
grid_image = Image.new("RGB", (grid_width, grid_height))

# Paste images into the grid
for i, img in enumerate(images):
    x_offset = (i % 5) * images[0].width
    y_offset = (i // 5) * images[0].height
    grid_image.paste(img, (x_offset, y_offset))

# Save the final grid image
grid_image.save("output_grid.png")
