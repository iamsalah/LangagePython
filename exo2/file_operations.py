class FileHandler:
    @staticmethod
    def read_file(filename):
        with open(filename, "r") as file:
            content = file.read()
        return content

    @staticmethod
    def write_file(filename, content):
        with open(filename, "w") as file:
            file.write(content)

