import sys #Access command line arguments
from PIL import Image #Treat files as images

images =[] #acumulate images

#iterate through images and add it to the list images
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
#python3 gifPIL.py costume1.gif costume2.gif