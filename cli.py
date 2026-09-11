import argparse
from modules.registry import Registry
from modules.loader import Loader
from modules.app import CLI
import os

parser = argparse.ArgumentParser("stationapi_utils")
parser.add_argument("-namespace", help="Define the mod namespace", type=str, required=False)
args = parser.parse_args()

namespace = "morebeta"
resources_path = "D:/Projects/Minecraft Modding/Babric Mods/MoreBetaWorkspace/morebeta/src/main/generated/resources/"

directory = os.path.dirname(__file__)
if directory == "": directory = os.getcwd()

registry = Registry(namespace)
loader = Loader(registry)
loader.loadPath(directory + "/data/resources")

app = CLI(registry, resources_path)
while app.running: app.run()

print("Finished")
