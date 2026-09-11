ITEM = '''{
	"generated": "fence",
	"parent": "morebeta:base/fence_inventory",
	"textures": { "texture": "$tex" }
}
'''
BLOCKSTATE = '''{
	"generated": "fence",
	"multipart": [
		{ "apply": { "model": "morebeta:block/$id_post" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true }, "when": { "east": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 180 }, "when": { "west": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 90 }, "when": { "north": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": true, "y": 270 }, "when": { "south": "true" } }
	]
}
'''
POST = '''{
	"generated": "fence",
	"parent": "morebeta:base/fence_post",
	"textures": { "texture": "$tex" }
}'''
SIDE = '''{
	"generated": "fence",
	"parent": "morebeta:base/fence_side",
	"textures": { "texture": "$tex" }
}'''