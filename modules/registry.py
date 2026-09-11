from modules.resource import Resource

class Registry:
	def __init__(self, namespace: str):
		self.map: dict[str, Resource] = {}
		self.namespace = namespace

	def put(self, key: str, resource: Resource) -> None:
		self.map.setdefault(key, resource)

	def get(self, key: str) -> Resource:
		return self.map.get(key)
