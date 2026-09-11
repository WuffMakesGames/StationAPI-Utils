BLOCKSTATE = '''{
	"generated": "slab",
	"variants": {
		"face=up,double=false": 	{ "model": "morebeta:block/$id", "uvlock": true },
		"face=down,double=false": 	{ "model": "morebeta:block/$id", "uvlock": true, "x": 180 },
		"face=north,double=false": 	{ "model": "morebeta:block/$id", "uvlock": true, "x": 90, "y": 270 },
		"face=south,double=false": 	{ "model": "morebeta:block/$id", "uvlock": true, "x": 90, "y": 90 },
		"face=east,double=false": 	{ "model": "morebeta:block/$id", "uvlock": true, "x": 90, "y": 0 },
		"face=west,double=false": 	{ "model": "morebeta:block/$id", "uvlock": true, "x": 90, "y": 180 },
		"face=up,double=true": 		{ "model": "$full" },
		"face=down,double=true": 	{ "model": "$full" },
		"face=north,double=true": 	{ "model": "$full" },
		"face=south,double=true": 	{ "model": "$full" },
		"face=east,double=true": 	{ "model": "$full" },
		"face=west,double=true": 	{ "model": "$full" }
	}
}
'''
MODEL = '''{
	"generated": "slab",
	"parent": "morebeta:base/slab_all",
	"textures": { "all": "$tex" }
}
'''	