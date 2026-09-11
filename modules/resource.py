from modules.printing import prettyprint as print
import yaml, json, os

def load_yaml(filename: str):
	file = open(filename, "r")
	data = yaml.load(file, Loader=yaml.FullLoader)
	file.close()
	return data

def write_file(filename: str, text: str):
	file = open(filename, "w")
	file.write(text)
	file.close()
	return text

class Resource:
	def __str__(self):
		return f"Resource {self.name}(\"{self.filename}\")"
	
	def __init__(self, filename: str):
		self.filename = filename
		self.name, ext = os.path.splitext(os.path.basename(filename))

		self.yaml: dict[str, object] = load_yaml(filename)
		self.template = self.yaml["template"]
	
	def writeToDisk(self, resource_path: str, namespace: str, id: str, tags: dict[str, str]):
		self.writeFiles(self.yaml.get("assets"), (resource_path + f"assets/{namespace}/stationapi/"), namespace, id, tags)
		self.writeFiles(self.yaml.get("data"),   (resource_path + f"data/{namespace}/stationapi/"), namespace, id, tags)

	### Writes a collection of resource files to the disk.
	def writeFiles(self, files: dict[str, str], root: str, namespace: str, id: str, tags: dict[str, str]):
		if files is None: return
		for key, value in files.items():
			filename = os.path.join(root + key).replace("$id", id)
			self.writeFile(filename, value, namespace, id, tags)
	
	### Writes a resource file to the disk.
	def writeFile(self, filename: str, text: str, namespace: str, id: str, tags: dict[str, str]):
		if filename.endswith(".json"): text = json.dumps(json.loads(text), indent=4)

		# Replace tags
		for tag, value in tags.items():
			text = text.replace(tag, value)
		
		# Replace keys
		text = text.replace("$gen", self.name)
		text = text.replace("$namespace", namespace)
		text = text.replace("$id", id)

		# Write the file
		print(f"> Writing: \"{filename}\"", color="cyan")
		write_file(filename, text)
