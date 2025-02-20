import json
import os


class DataManager:
    
    def __init__(self, file_path):
        
        self.file_path = file_path
        
        
    def get_data(self) -> dict:
        with open(self.file_path) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                return {}
        return {int(k): v for k, v in data.items()}
    
    
    def update_data(self, key, value):
        data = self.get_data()
        data[str(key)] = value
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)