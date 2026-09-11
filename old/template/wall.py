ITEM = '''{
	"generated": "wall",
	"parent": "morebeta:base/wall_inventory",
	"textures": { "texture": "$tex" }
}
'''
BLOCKSTATE = '''{
	"generated": "wall",
	"multipart": [
		{ "apply": { "model": "morebeta:block/$id_post" }, "when": { "post": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 0 }, "when": { "east": "short" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 180 }, "when": { "west": "short" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 90 }, "when": { "north": "short" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 270 }, "when": { "south": "short" } },
		{ "apply": { "model": "morebeta:block/$id_full", "uvlock": true, "y": 0 }, "when": { "east": "tall" } },
		{ "apply": { "model": "morebeta:block/$id_full", "uvlock": true, "y": 180 }, "when": { "west": "tall" } },
		{ "apply": { "model": "morebeta:block/$id_full", "uvlock": true, "y": 90 }, "when": { "north": "tall" } },
		{ "apply": { "model": "morebeta:block/$id_full", "uvlock": true, "y": 270 }, "when": { "south": "tall" } }
	]
}
'''
POST = '''{
	"generated": "wall",
	"parent": "morebeta:base/wall_post",
	"textures": { "texture": "$tex" }
}'''
SIDE = '''{
	"generated": "wall",
	"parent": "morebeta:base/wall_side",
	"textures": { "texture": "$tex" }
}'''
FULL = '''{
	"generated": "wall",
	"parent": "morebeta:base/wall_full",
	"textures": { "texture": "$tex" }
}'''