import os

def create_folder(path: str) -> tuple:
    os.makedirs(path, exist_ok=True)
    folder_path_root = os.path.abspath(path)
    
    folder_name_data = "data"
    folder_path_data = os.path.join(folder_path_root, folder_name_data)
    os.makedirs(folder_path_data, exist_ok=True)

    folder_name_META = "META"
    folder_path_META = os.path.join(folder_path_root, folder_name_META)
    os.makedirs(folder_path_META, exist_ok=True)

    return folder_path_data, folder_path_META
