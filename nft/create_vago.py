from parts import PARTS
from PIL import Image
from test import foo
from random_from_events import rand_to_nft

id=22
genes = foo(rand_to_nft(id))


# SIZE
old = (895, 1569)
# NEW SIZE
new = (1600,2000)
# MAIN BODY
im0 = Image.open(PARTS["cuerpo"]["img"][0])
# WORKING BODY
border = Image.new("RGBA",new,color=PARTS["bg"][genes[0]%5])
body = im0.copy()
eyes = Image.open(PARTS["eyes"]["img"][genes[1]%5])
cyb = Image.open(PARTS["cyb"]["img"][genes[2]%7])
bocas = Image.open(PARTS["bocas"]["img"][genes[3]%5])
inferior = Image.open(PARTS["inferior"]["img"][genes[4]%4])
superior = Image.open(PARTS["superior"]["img"][genes[5]%5])
manod = Image.open(PARTS["manod"]["img"][genes[6]%5])
manoi = Image.open(PARTS["manoi"]["img"][genes[7]%5])
# (2560, 170)
#print(manoi.size)
#superiorr = superior.resize((240,240))
#superiorr.save("./vago_parts/superior/1.png")
# ASSEMBLY
border.paste(body,box=PARTS["cuerpo"]["loc"][0],mask=body)
border.paste(eyes,box=PARTS["eyes"]["loc"][genes[1]%5] ,mask=eyes)
border.paste(superior,box=PARTS["superior"]["loc"][genes[5]%5],mask=superior)
border.paste(inferior,box=PARTS["inferior"]["loc"][genes[4]%4],mask=inferior)

border.paste(manod,box=PARTS["manod"]["loc"][genes[6]%5],mask=manod)
border.paste(cyb,box=PARTS["cyb"]["loc"][genes[2]%7],mask=cyb)
border.paste(bocas,box=PARTS["bocas"]["loc"][genes[3]%5],mask=bocas)
border.paste(manoi,box=PARTS["manoi"]["loc"][genes[7]%5],mask=manoi)

border.show()

# SAVE VAGOS V2
#border.save("./nft/metadata/{}.png".format(id))



