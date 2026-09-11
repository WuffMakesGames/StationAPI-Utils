from modules.registry import Registry
from modules.loader import Loader
from modules.app import CLI
import os

directory = os.path.dirname(__file__)

registry = Registry("morebeta")
loader = Loader(registry)
loader.loadPath(directory + "/data/resources")

app = CLI(registry, "D:/Projects/Minecraft Modding/Babric Mods/MoreBetaWorkspace/morebeta/src/main/generated/resources/")
while app.running: app.run()

print("Finished")
