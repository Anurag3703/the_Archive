import shutil
import os

def upload_data(file_path, destination= "data/raw"):
    if not os.path.exists(file_path):
        print("File doesn't exist")
        return
    if not file_path.endswith(".csv", 'json'):
        print("Only csv and json files are supported")
        return
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.move(file_path,os.path.join(destination,os.path.basename(file_path)))
    print(f"File {os.path.basename(file_path)} successfully uploaded to {destination}.")



