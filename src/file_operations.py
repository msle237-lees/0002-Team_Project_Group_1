import re

class FileOperations:
    def __init__(self):
        pass

    def open_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.file_content = file.readlines()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def search_file(self, search_string, case_sensitive, n_th):
        results = []

        if not hasattr(self, 'file_content'):
            print("Error: File not opened or loaded. Please use open_file method first.")
            return results

        if not case_sensitive:
            search_string = search_string.lower()

        for line in self.file_content:
            if not case_sensitive:
                line = line.lower()

            words = line.split()
            occurrences = [index for index, word in enumerate(words) if word == search_string]

            for index in occurrences:
                if index + n_th < len(words):
                    results.append(words[index + n_th])

        return results


    def save_data_to_file(self, file_name, results):
        try:
            with open(file_name, 'w') as savefile:
                for result in results:
                    savefile.write(result)
                    savefile.write('\n')
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

def main():
    # Initialize the FileOperations class
    file_operations = FileOperations()

    # Test the open_file method
    file_name = "src/txt/President Washinton Inaugural Speech.txt"
    if file_operations.open_file(file_name):
        print(f"File {file_name} opened successfully.")
    else:
        print(f"Failed to open file {file_name}")

    # Test the search_file method
    search_string = "the"
    case_sensitive = False
    n_th = 1
    results = file_operations.search_file(search_string, case_sensitive, n_th)
    print(f"Search results for '{search_string}':\n{results}")

    # Test the save_data_to_file method
    output_file = "src/out/output.txt"
    if file_operations.save_data_to_file(output_file, results):
        print(f"Search results saved to {output_file}")
    else:
        print(f"Failed to save search results to {output_file}")


if __name__ == "__main__":
    main()
