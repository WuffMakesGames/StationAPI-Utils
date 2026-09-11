ITEM = '''{
	"generated": "detailed_fence",
	"parent": "morebeta:base/detailed_fence_inventory",
	"textures": { "texture": "$tex" }
}
'''
BLOCKSTATE = '''{
	"generated": "detailed_fence",
	"multipart": [
		{ "apply": { "model": "morebeta:block/$id_post" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": false }, "when": { "east": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": false, "y": 180 }, "when": { "west": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": false, "y": 90 }, "when": { "north": "true" } },
		{ "apply": { "model": "morebeta:block/$id_side", "uvlock": false, "y": 270 }, "when": { "south": "true" } }
	]
}
'''
POST = '''{
	"generated": "detailed_fence",
	"parent": "morebeta:base/detailed_fence_post",
	"textures": { "texture": "$tex" }
}'''
SIDE = '''{
	"generated": "detailed_fence",
	"parent": "morebeta:base/detailed_fence_side",
	"textures": { "texture": "$tex" }
}'''