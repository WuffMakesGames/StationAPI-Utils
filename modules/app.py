from modules.registry import Registry
from modules.resource import Resource
from modules.template import TemplateGroup
from modules.printing import prettyprint as print, clear

class CLI:
	def __init__(self, registry: Registry, resource_path: str):
		self.running = True
		self.initialized = False

		self.namespace = registry.namespace
		self.resource_path = resource_path

		# Variables
		self.groups: dict[str, TemplateGroup] = {}
		self.group: TemplateGroup = None

		self.default_group = None
		self.previous_resource: Resource = None

		# Get templates
		for key, resource in registry.map.items():
			if self.groups.get(resource.template) is None: self.groups[resource.template] = TemplateGroup(resource.template)
			if self.default_group == None: self.default_group = self.groups[resource.template]
			self.groups[resource.template].append(resource)

		# Clear CLI
		clear()
	
	def initialize(self):
		if len(self.groups) == 1:
			self.group = self.default_group
			self.initialized = True
			return

		# Get template
		response = input(f"Template ({ ", ".join(self.groups.keys()) }): ")
		self.group = self.groups.get(response)
		
		# Check template validity
		if self.group is None:
			clear(f"Invalid template: {response}", color="red")

		else: 
			clear()
			self.initialized = True

	def run(self):
		if not self.initialized: self.initialize()
		else: self.input()

	def input(self):
		print(f"Generating {self.group.name}...", color="cyan")

		# Get ID
		response_id = input("ID: ")
		default_texture = f"{self.namespace}:block/{response_id}"
		tags = {}

		# Get template
		print(f"Templates: ({self.group.toString()})", color="cyan")
		if self.previous_resource is None: response_template = input(f"Template: ")
		else: response_template = input(f"Template (leave empty to use {self.previous_resource.name}): ")
		if response_template == "": response_template = self.previous_resource.name

		resource = self.group.getByName(response_template)
		if resource is None: return clear(f"Invalid template: {response_template}", color="red")
		self.previous_resource = resource

		# Get textures
		for tex in resource.yaml.get("textures", []):
			response = input(f"Texture #{tex} (leave empty to use '{default_texture}'): ")
			if response == "": response = default_texture
			if response.count(":") == 0: response = f"{self.namespace}:block/{response}"
			tags.setdefault(f"$tex_{tex}", response)
		
		# Get custom values
		for entry in resource.yaml.get("tags", []):
			response = input(f"Custom Tag #{entry}: ")
			tags.setdefault(f"${entry}", response)

		# Generate mod files
		clear()
		resource.writeToDisk(
			resource_path=self.resource_path,
			namespace=self.namespace,
			id=response_id,
			tags=tags
		)

		# Finished with no errors
		print(f"> Generated {resource.name}", color="green")
