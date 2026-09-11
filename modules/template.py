from modules.resource import Resource

class TemplateGroup:
	def __init__(self, name):
		self.resources: list[Resource] = []
		self.name = name

	def append(self, resource: Resource):
		self.resources.append(resource)
	
	def getByName(self, name: str):
		for resource in self.resources:
			if resource.name == name: return resource
		return None

	def get(self, index: int):
		return self.resources[index]
	
	def toString(self):
		return ", ".join([res.name for res in self.resources])
	
