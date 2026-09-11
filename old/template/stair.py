BLOCKSTATE = '''{
	"generated": "stair",
	"variants": {
		"facing=north,top=false": { "uvlock": true, "model": "morebeta:block/$id", "y": 0,	"x": 0 },
		"facing=south,top=false": { "uvlock": true, "model": "morebeta:block/$id", "y": 180,  "x": 0 },
		"facing=east,top=false":  { "uvlock": true, "model": "morebeta:block/$id", "y": 90,	"x": 0 },
		"facing=west,top=false":  { "uvlock": true, "model": "morebeta:block/$id", "y": 270,  "x": 0 },
		"facing=north,top=true":  { "uvlock": true, "model": "morebeta:block/$id", "y": 0, 	"x": 180 },
		"facing=south,top=true":  { "uvlock": true, "model": "morebeta:block/$id", "y": 180,  "x": 180 },
		"facing=east,top=true":   { "uvlock": true, "model": "morebeta:block/$id", "y": 90,	"x": 180 },
		"facing=west,top=true":   { "uvlock": true, "model": "morebeta:block/$id", "y": 270,  "x": 180 }
	}
}
'''
MODEL = '''{
	"generated": "stair",
	"parent": "morebeta:base/stairs_all",
	"textures": { "all": "$tex" }
}
'''