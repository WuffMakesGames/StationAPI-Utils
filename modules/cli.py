from modules.app import App
from modules.resource import Resource
from modules.template import TemplateGroup
from modules.printing import prettyprint as print, clear
from modules.colors import COLORS

class CLI:
	def __init__(self, app: App):
		self.initialized: bool = False
		self.app: App = app

		# Load resources
		app.loadResources()

		# Variables
		self.groups: dict[str, TemplateGroup] = {}
		self.group: TemplateGroup = None
		self.default_group: TemplateGroup = None

		self.previous_resource: Resource = None

		# Get templates
		for key, resource in app.registry.map.items():
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

		# Variables
		app = self.app
		registry = app.registry
		saver = app.saver

		# Get ID
		response_id = input("ID: ")
		default_texture = f"{registry.namespace}:block/{response_id}"
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
		for tex in resource.textures:
			response = input(f"Texture #{tex} (leave empty to use '{default_texture}'): ")
			if response == "": response = default_texture
			if response.count(":") == 0: response = f"{registry.namespace}:block/{response}"
			tags.setdefault(f"$tex_{tex}", response)
		
		# Get custom tags
		for entry in resource.tags:
			response = input(f"Custom Tag #{entry}: ")
			tags.setdefault(f"${entry}", response)

		# Generate colored resources
		if response_id.count("!c"):
			clear()
			for color in COLORS:
				colored_tags = {}
				for key,tag in tags.items(): colored_tags[key] = tag.replace("!c", color)
				saver.save(resource, response_id.replace("!c", color), colored_tags)
			print(f"> Generated 16 colored {resource.name}(s)", color="green")

		# Generate base resources
		else:
			clear()
			saver.save(resource, response_id, tags)
			print(f"> Generated {resource.name}", color="green")
