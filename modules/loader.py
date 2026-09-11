from modules.registry import Registry
from modules.resource import Resource
import os

class Loader:
	def __init__(self, registry: Registry):
		self.registry = registry

	def loadPath(self, path: str) -> None:
		for root, dirs, files in os.walk(path):
			for file in files:
				filename = root + "/" + file
				key, ext = os.path.splitext(filename.removeprefix(path))
				self.loadResource(key, filename)
	
	def loadResource(self, key: str, filename: str) -> None:
		resource = Resource(filename)
		self.registry.put(filename, resource)
