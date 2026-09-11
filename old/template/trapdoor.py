BLOCKSTATE = '''{
	"generated": "trapdoor",
	"variants": {
		"facing=north,top=false,open=false": { "model": "morebeta:block/$id_bottom", "y": 90 },
		"facing=south,top=false,open=false": { "model": "morebeta:block/$id_bottom", "y": 270 },
		"facing=east,top=false,open=false":  { "model": "morebeta:block/$id_bottom", "y": 180 },
		"facing=west,top=false,open=false":  { "model": "morebeta:block/$id_bottom", "y": 0 },

		"facing=north,top=false,open=true": { "model": "morebeta:block/$id_open", "y": 90 },
		"facing=south,top=false,open=true": { "model": "morebeta:block/$id_open", "y": 270 },
		"facing=east,top=false,open=true":  { "model": "morebeta:block/$id_open", "y": 180 },
		"facing=west,top=false,open=true":  { "model": "morebeta:block/$id_open", "y": 0 },

		"facing=north,top=true,open=false":  { "model": "morebeta:block/$id_top", "y": 90 },
		"facing=south,top=true,open=false":  { "model": "morebeta:block/$id_top", "y": 270 },
		"facing=east,top=true,open=false":   { "model": "morebeta:block/$id_top", "y": 180 },
		"facing=west,top=true,open=false":   { "model": "morebeta:block/$id_top", "y": 0 },

		"facing=north,top=true,open=true":  { "model": "morebeta:block/$id_open", "y": 90 },
		"facing=south,top=true,open=true":  { "model": "morebeta:block/$id_open", "y": 270 },
		"facing=east,top=true,open=true":   { "model": "morebeta:block/$id_open", "y": 180 },
		"facing=west,top=true,open=true":   { "model": "morebeta:block/$id_open", "y": 0 }
	}
}
'''
TOP = '''{
	"generated": "trapdoor",
	"parent": "morebeta:base/trapdoor_top",
	"textures": { "texture": "$tex" }
}
'''
BOTTOM = '''{
	"generated": "trapdoor",
	"parent": "morebeta:base/trapdoor_bottom",
	"textures": { "texture": "$tex" }
}
'''
OPEN = '''{
	"generated": "trapdoor",
	"parent": "morebeta:base/trapdoor_open",
	"textures": { "texture": "$tex" }
}
'''