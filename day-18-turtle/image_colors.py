import colorgram

# Duplicate a Hirst painting
# Used to extract colors
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g,color.rgb.b))

print(rgb_colors)