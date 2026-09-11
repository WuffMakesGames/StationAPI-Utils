import registry, template
from utils import *
from paths import *

# TODO: gate, pane, bed, button, door, ladder, path, pressure_plate, sign, torch, vine

### BLOCK ============================================
def generate_block(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.base.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}.json", template.cube.BLOCK_MODEL_ALL.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.ITEM.replace("$id", id))
registry.add_block("block", generate_block, None)

### STAIRS ===========================================
def generate_stairs(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.stair.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}.json", template.stair.MODEL.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.ITEM.replace("$id", id))
registry.add_block("stair", generate_stairs, None)

### TRAPDOOR =========================================
def generate_trapdoor(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.trapdoor.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}_top.json", template.trapdoor.TOP.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_bottom.json", template.trapdoor.BOTTOM.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_open.json", template.trapdoor.OPEN.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.ITEM.replace("$id", id + "_bottom"))
registry.add_block("trapdoor", generate_trapdoor, None)

### FENCE ============================================
def generate_fence(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.fence.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}_post.json", template.fence.POST.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_side.json", template.fence.SIDE.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.fence.ITEM.replace("$id", id).replace("$tex", tex))

def remove_fence(id):
	removefile(f"{PATH_BLOCKSTATE}/{id}.json")
	removefile(f"{PATH_MODELS}/block/{id}_post.json")
	removefile(f"{PATH_MODELS}/block/{id}_side.json")
	removefile(f"{PATH_MODELS}/item/{id}.json")
	
registry.add_block("fence", generate_fence, remove_fence)

### FENCE ============================================
def generate_detailed_fence(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.detailed_fence.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}_post.json", template.detailed_fence.POST.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_side.json", template.detailed_fence.SIDE.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.detailed_fence.ITEM.replace("$id", id).replace("$tex", tex))

def remove_detailed_fence(id):
	removefile(f"{PATH_BLOCKSTATE}/{id}.json")
	removefile(f"{PATH_MODELS}/block/{id}_post.json")
	removefile(f"{PATH_MODELS}/block/{id}_side.json")
	removefile(f"{PATH_MODELS}/item/{id}.json")
	
registry.add_block("fence_ext", generate_detailed_fence, remove_detailed_fence)

### SLAB =============================================
def generate_slab(id, tex):
	full = input(f"Full block model (leave empty to use '{tex}'): ")
	# if full.startswith("?"):
	# 	writefile(f"{PATH_MODELS}/block/{full[1::]}", template.cube.BLOCK_MODEL_ALL.replace("$tex", tex))
	# 	full = f"{PATH_MODELS}/block/{full[1::]}"
	# 	?black_wool
		
	if full == "": full = tex
	if full.count(":") == 0: full = tex

	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.slab.BLOCKSTATE.replace("$full", full).replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}.json", template.slab.MODEL.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.ITEM.replace("$id", id))
registry.add_block("slab", generate_slab, None)

### CROSS ============================================
def generate_cross(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.base.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}.json", template.cross.MODEL.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.GENERATED_ITEM.replace("$tex", tex))
registry.add_block("cross", generate_cross, None)

### WALL =============================================
def generate_wall(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.wall.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}_post.json", template.wall.POST.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_side.json", template.wall.SIDE.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_full.json", template.wall.FULL.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.wall.ITEM.replace("$id", id).replace("$tex", tex))
registry.add_block("wall", generate_wall, None)

### CARPET ===========================================
def generate_carpet(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.base.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}.json", template.carpet.MODEL.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.ITEM.replace("$id", id))
registry.add_block("carpet", generate_carpet, None)

### FURNACE ===========================================
def generate_furnace(id, tex):
	writefile(f"{PATH_BLOCKSTATE}/{id}.json", 	template.furnace.BLOCKSTATE.replace("$id", id))
	writefile(f"{PATH_MODELS}/block/{id}.json", template.furnace.UNLIT.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/block/{id}_lit.json", template.furnace.LIT.replace("$tex", tex))
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.ITEM.replace("$id", id))
registry.add_block("furnace", generate_furnace, None)
