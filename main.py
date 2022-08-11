import os

for path, files in os.walk(
        "/Volumes/E:\01 - Current Projects\Verdiverkstedet\Kort Fortalt Season 02"):
    for file in files:
        # if file.startswith("VV_KF2"):
            print(os.path.join(path, file))
