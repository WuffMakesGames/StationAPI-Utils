from utils import *
import block, item, registry, os

# Inputs
def input_type(default):
	print(f"Types: {registry.get_list_formatted()}")
	type = input(f"Type (leave empty to use '{default}'): ")
	return default if type == "" else type

def input_tex(default):
	tex = input(f"Texture (leave empty to use '{default}'): ")
	if tex == "": tex = default
	if tex.count(":") == 0: tex = f"morebeta:block/{tex}"
	return tex

# App
type = "block"
colors = "black,gray,light_gray,white,brown,red,orange,yellow,lime,green,cyan,light_blue,blue,purple,magenta,pink".split(",")
os.system("cls")

while True:
	id = input("ID: ")
	if id == "": continue
	if id == "exit": break

	# Remove item
	removing = False
	if id.startswith("-"):
		removing = True
		id = id[1::]

	# Get Type
	type = input_type(type)

	# Type doesn't exist
	entry = registry.get(type)
	if entry is None:
		os.system("cls")
		print(f"Invalid type {type}")
		continue
	
	# Removing
	if removing:
		print(entry)
		if entry["remove"] is None:
			print("Failed to remove %s" % id)
		else:
			entry["remove"](id)
			print("Removed %s" % id)
		continue

	# Register block with colors
	tex = input_tex(entry["texture_root"] % id)
	if id.count("!c"):
		for col in colors:
			entry["generate"](id.replace("!c", col), tex.replace("!c", col))
		os.system("cls")
		print("Generated 16 blocks")

	# Register block
	else:
		entry["generate"](id, tex)
		os.system("cls")
		print("Generated %s" % id)

