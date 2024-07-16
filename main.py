import os
import magic


all_files = os.listdir("INSERT_PATH/Downloads")
folders = ["Images", "Folders"]

for file in all_files:
    try:
        name = magic.from_file(f"INSERT_PATH/Downloads/{file}", mime=True)
        if name.split()[0].title() == "Cannot":
            if not os.path.exists(f"INSERT_PATH/Downloads/Misc"):
                os.makedirs(f"INSERT_PATH/Downloads/Misc")
                folders.append("Misc")
            os.rename(f"INSERT_PATH/Downloads/{file}",
                      f"INSERT_PATH/Downloads/Misc/{file}")
        else:
            if not os.path.exists(f"INSERT_PATH/Downloads/{name.split()[0].title()}"):
                os.makedirs(f"INSERT_PATH/Downloads/{name.split()[0].title()}")
                folders.append(name.split()[0].title())
            os.rename(f"INSERT_PATH/Downloads/{file}", f"INSERT_PATH/Downloads/{name.split()[0].title()}/{file}")
    except PermissionError:
        if file not in folders:
            if not os.path.exists("INSERT_PATH/Downloads/Folders"):
                os.makedirs("INSERT_PATH/Downloads/Folders")
            os.rename(f"INSERT_PATH/Downloads/{file}", f"INSERT_PATH/Downloads/Folders/{file}")


