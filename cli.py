from modules.registry import Registry
from modules.loader import Loader
from modules.app import CLI
import os

directory = os.path.dirname(__file__)
namespace = "morebeta"
resources_path = "D:/Projects/Minecraft Modding/Babric Mods/MoreBetaWorkspace/morebeta/src/main/generated/resources/"

registry = Registry(namespace)
loader = Loader(registry)
loader.loadPath(directory + "/data/resources")

app = CLI(registry, resources_path)
while app.running: app.run()

print("Finished")
