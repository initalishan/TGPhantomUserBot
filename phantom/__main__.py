from phantom.core.clients import phantom
from os import listdir
import importlib
from asyncio import get_event_loop

async def main():
    import_plugins()
    print("Phantom UserBot started.")
    await phantom.run_until_disconnected()

def import_plugins():
    path = "phantom/plugins"
    for file in listdir(path):
        if file.endswith(".py") and not file.startswith("__"):
            importlib.import_module(f"phantom.plugins.{file[:-3]}")
            print(f"{file[:-3]} plugin loaded succesfully.")

get_event_loop().run_until_complete(main())