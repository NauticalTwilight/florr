import os

# Function to process the name of the file
def processName(name):
    processedName = '_'.join(file.lower().split(' '))
    # Process exceptions
    if processedName == "shiny_ladybug.png":
        return "ladybug_shiny.png"
    elif processedName == "dark_ladybug.png":
        return "ladybug_dark.png"
    elif processedName == "hel_beetle.png":
        return "beetle_hel.png"
    elif processedName == "evil_centipede.png":
        return "centipede_evil.png"
    elif processedName == "desert_centipede.png":
        return "centipede_desert.png"
    else:
        return processedName

# Recurse through every image file in the folder ./batch/ (. being where the Python file is ran from)
for file in os.listdir("./batch/"):
    if file.endswith(".png"):
        print(f"INFO: Renaming file: {file}")
        os.rename(f"./batch/{file}", f"./batch/{processName(file)}")