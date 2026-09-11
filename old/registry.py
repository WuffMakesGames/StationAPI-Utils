__registry = {}
__list_cache = None

def get_list_formatted() -> str: return ", ".join(get_list())
def get_list() -> list:
	global __list_cache
	if __list_cache is None: __list_cache = list(__registry.keys())
	return __list_cache

def add_block(key: str, create: callable, remove: callable):
	add(key, (create, remove), "morebeta:block/%s")

def add_item(key: str, create: callable, remove: callable):
	add(key, (create, remove), "morebeta:item/%s")

def get(key: str) -> dict:
	return __registry.get(key)

def add(key: str, methods: tuple[callable, callable], texture_root: str):
	__registry.setdefault(key, {
		"generate": methods[0],
		"remove": methods[1],
		"texture_root": texture_root
	})
