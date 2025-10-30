import json
import os
from typing import Any


STORAGE_BASE_FOLDER = "./storage_file"

class BaseStrage:
    _file_path: str

    def __init__(self, file_name: str):
        self._file_path = os.path.abspath(os.path.join(STORAGE_BASE_FOLDER, file_name))

    # save to file
    def save_data_to_file(self, data: list[dict[str, Any]]):
        with open(self._file_path, "w") as file:
            json.dump(data, file, indent=4)
        file.close()
    
    # read from file
    def read_data_from_file(self) -> list[dict[str, Any]]:
        with open(self._file_path, "r") as file:
            return json.load(file)

    # check whether the file exist
    def check_file_exist(self):
        if not os.path.exists(self._file_path):
            os.makedirs(os.path.abspath(STORAGE_BASE_FOLDER), exist_ok=True)
            init_data = []
            try:
                with open(self._file_path, "w") as file:
                    json.dump(init_data, file, indent=4)
                file.close()
            except:
                print("failed to create file")