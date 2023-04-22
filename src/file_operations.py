class FileOperations:
    OperatingFile = None
    # Flags whether file is ready for IO
    # flag=bool(True)
    def __init__(self):
        pass

    def open_file(self, file_name):
        # Tries to open file provided and returns whether successful
        try:
            OperatingFile = open(file_name, 'r')
            return bool(True)
        except:
            return bool(False)

    def search_file(self, search_string, caseSensitive):
        if caseSensitive:
            pass
        else:
            pass

    def save_file(self, file_name):
        pass

    def save_data_to_file(self, file_name, data):
        pass    