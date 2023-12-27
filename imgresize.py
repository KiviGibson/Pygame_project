from PIL import Image
import PIL
name = "./Images/Animations/green/idle/0.png"
img = Image.open(name)
new_img = img.resize((img.width*2, img.height*2), resample=Image.NEAREST)
new_img.save(name)
