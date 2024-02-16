import os

folder_path = r'C:\Users\Administrator\Desktop\nox_setup_v7.0.5.9_full_intl\bin\BignoxVMS'

def list_folders(directory):
    try:
        folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
        return folders
    except Exception as e:
        return []

all_folders = list_folders(folder_path)

for folder in all_folders:
    file = open(f"{folder_path}\{folder}\{folder}.vbox","r")
    port = file.read().split('<Forwarding name="port2" proto="1" hostip="127.0.0.1" hostport="')[1].split('"')[0]

    os.system(f"adb connect 127.0.0.1:{port}")
