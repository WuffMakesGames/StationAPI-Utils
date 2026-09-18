import argparse
from modules.app import App
from modules.cli import CLI
import os

# Arguments
parser = argparse.ArgumentParser("stationapi_utils")
parser.add_argument("-namespace", help="Define the mod namespace", type=str, required=False)
args = parser.parse_args()

# User directory
namespace = "morebeta"
resources_path = "D:/Projects/Minecraft Modding/Babric Mods/MoreBetaWorkspace/morebeta/src/main/generated/resources/"
resources_path = "test/"

# App directory
directory = os.path.dirname(__file__)
if directory == "": directory = os.getcwd()

# Application
app = App(namespace, resources_path, directory)
cli = CLI(app)
while app.running: cli.run()

# Exit
print("Finished")
