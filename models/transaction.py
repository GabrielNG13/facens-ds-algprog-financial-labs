# Internal imports
from utils.utils import Utils

class Transaction():
    
    def __init__(self, operation=None, value=None, description=None):
        self.__utils = Utils()
        
        self.__operation = operation
        self.__value = value
        self.__description = description
    
    def save(self):
        self.__utils.write_file(self.__operation, self.__value, self.__description)
    
    def view(self):
        return [ transacion for transacion in self.__utils.read_file() ]