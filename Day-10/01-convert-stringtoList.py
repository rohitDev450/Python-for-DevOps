import os

floder_paths = input("Enter the folder path sperate by spaces : ").split()
for floder in floder_paths:
    
    try:
        files = os.listdir(floder)
        print("========Listed files in Give Floder :", floder)
        print(files)
    except FileNotFoundError:
        print("Floder Not found plz valid folder: ",floder)
    
        