import sys
from Extentions import Extentions

class Main:
    """
    The main class
    """

    def __init__(self):
        """
        Get filenames
        """

        self.files = sys.argv[1:]
    
    def recognizeExtention(name:str) -> Extentions:
        ext = name.split('.')
        match ext[-1]:
            case 'c':
                return Extentions.C
            case _:
                return Extentions.TXT