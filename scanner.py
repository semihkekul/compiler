class Scanner:
    def load_code_file(self, file_path):
        f = open(file_path, "r")
        print(f.read())
