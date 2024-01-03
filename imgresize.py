from PIL import Image

name = "./Images/Animations/green/damage/2"
format=".png"

img = Image.open(name+format)
new_img = img.resize((img.width*2, img.height*2), resample=Image.NEAREST)

new_img.save(name+format)
img.save(name+".old"+format)
