from modules.printing import prettyprint as print
from typing import Literal
import yaml, json, os

ASSET_TYPE = Literal["assets", "data"]

### Resource =============================================================
class Resource:
	def __init__(self, filename: str):
		self.filename = filename
		self.name = filename

		self.template: str = "blockmodel"
		self.textures: list = []
		self.tags: list = []

		self.assets: dict[str, str] = {}
		self.data: dict[str, str] = {}

	def __str__(self): return f"Resource {self.name}(\"{self.filename}\")"
	
### Resource =============================================================
class ResourceFile:
	def __init__(self, filename: str, contents: str):
		self.filename = filename
		self.contents = contents

### Loader ===============================================================
class ResourceLoader:
	def load(self, filename: str) -> Resource:
		resource: Resource = Resource(filename)
		with open(filename, "r") as f:
			data: dict[str, object] = yaml.load(f, Loader=yaml.FullLoader)

		# Load elements from yaml
		resource.template = data.get("template", "blockmodel")
		resource.textures = data.get("textures", [])
		resource.tags = data.get("tags", [])

		resource.assets = data.get("assets", {})
		resource.data = data.get("data", {})

		# Return resource
		return resource

### Saver ================================================================
class ResourceSaver:
	def __init__(self, path: str, namespace: str):
		self.path = path
		self.namespace = namespace

	def save(self, resource: Resource, id: str, tags: dict[str, str]):
		self.__saveFiles(resource, "assets", id, tags)
		self.__saveFiles(resource, "data", id, tags)

	def __saveFiles(self, resource: Resource, type: ASSET_TYPE, id: str, tags: dict[str, str]):
		root: str = f"{self.path}/{type}/{self.namespace}/stationapi/"

		# Get file list from resource
		files: dict[str, str] = None
		if type == "assets": files = resource.assets
		elif type == "data": files = resource.data

		# Save each file
		for file, contents in files.items():
			filename = (root + file).replace("$id", id)
			self.__saveFile(resource, ResourceFile(filename, contents), id, tags)
	
	def __saveFile(self, resource: Resource, file: ResourceFile, id: str, tags: dict[str, str]):
		filename = file.filename
		contents = file.contents

		# Prettify json contents
		if filename.endswith(".json"): contents = json.dumps(json.loads(contents), indent=4)
		
		# Replace tags
		for tag, value in tags.items(): contents = contents.replace(tag, value)

		# Replace keys
		contents = contents.replace("$gen", resource.name)
		contents = contents.replace("$namespace", self.namespace)
		contents = contents.replace("$id", id)

		# Write the file
		print(f"> Writing \"{filename}\"", color="cyan")
		if not os.path.exists(os.path.dirname(filename)):
			os.makedirs(os.path.dirname(filename))
		with open(filename, "w") as f: f.write(contents)
