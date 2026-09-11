BLOCKSTATE = '''{
	"generated": "furnace",
	"variants": {
		"facing=north,lit=false": { "model": "morebeta:block/$id", "y": 0 },
		"facing=south,lit=false": { "model": "morebeta:block/$id", "y": 180 },
		"facing=east,lit=false":  { "model": "morebeta:block/$id", "y": 90 },
		"facing=west,lit=false":  { "model": "morebeta:block/$id", "y": 270 },
		"facing=north,lit=true":  { "model": "morebeta:block/$id_lit", "y": 0 },
		"facing=south,lit=true":  { "model": "morebeta:block/$id_lit", "y": 180 },
		"facing=east,lit=true":   { "model": "morebeta:block/$id_lit", "y": 90 },
		"facing=west,lit=true":   { "model": "morebeta:block/$id_lit", "y": 270 }
	}
}
'''
UNLIT = '''{
	"parent": "block/cube",
	"textures": {
		"particle": "#east",
		"north": "$tex_side",
		"south": "$tex_side",
		"east": "$tex_front",
		"west": "$tex_side",
		"up": "$tex_top",
		"down": "$tex_bottom"
	}
}
'''
LIT = '''{
	"parent": "block/cube",
	"textures": {
		"particle": "#east",
		"north": "$tex_side",
		"south": "$tex_side",
		"east": "$tex_front_lit",
		"west": "$tex_side",
		"up": "$tex_top",
		"down": "$tex_bottom"
	}
}
'''