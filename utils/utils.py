# Default imports
from datetime import datetime

# Internal imports
from configurations.configuration import Configuration

class Utils():
    
    def __init__(self):
        self.__configuration = Configuration()

    def read_file(self):
        with open(self.__configuration.file_output, 'r') as file:
            return list(map(lambda l: l.replace('\n', ''), file.readlines()))
    
    def write_file(self, operation, value, description):
        with open(self.__configuration.file_output, 'a+') as file:
            file.write(
                f'{datetime.today()} - {operation} - {value} - {description}\n'
            )