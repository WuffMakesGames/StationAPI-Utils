from modules.registry import Registry
from modules.resource import Resource, ResourceLoader, ResourceSaver
import os

class App:
	def __init__(self, namespace: str, resource_path: str, working_directory: str):
		self.running = True
		
		self.resource_path = resource_path
		self.working_directory = working_directory

		self.registry = Registry(namespace)
		self.loader = ResourceLoader()
		self.saver = ResourceSaver(resource_path, namespace)
	
	def loadResources(self):
		self.registry.clear()
		path = self.working_directory + "/data/resources"

		for root, dirs, files in os.walk(path):
			for file in files:
				filename = root + "/" + file
				
				resource = self.loader.load(filename)
				resource.name = filename[:filename.rfind(".")].removeprefix(root + "/")

				self.registry.put(resource.name, resource)
	
