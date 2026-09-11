import registry, template
from utils import *
from paths import *

# Music discs
def item(id, tex):
	writefile(f"{PATH_MODELS}/item/{id}.json", 	template.base.GENERATED_ITEM.replace("$tex", tex))
# registry.add_item("item", item)

