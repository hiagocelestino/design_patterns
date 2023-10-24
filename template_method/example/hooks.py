from abc import ABC, abstractmethod

class FileHandler(ABC):
    _file = None

    def content_file(self, filename) -> str:
        self.open_file(filename)
        self.before_read()
        content = self.read_file()
        self.after_read()
        self.close_file()

        return content

    @abstractmethod
    def open_file(self):
        ...

    @abstractmethod
    def read_file(self):
        ...

    @abstractmethod
    def close_file(self):
        ...

    def before_read(self):
        ...
    
    def after_read(self):
        ...

class TextFileHandler(FileHandler):

    def open_file(self, filename):
        self._file = open(filename)

    def read_file(self):
        return self._file.read()


    def close_file(self):
        self._file.close()


class BinTextFileHandler(FileHandler):

    def open_file(self, filename):
        self._file = open(filename, 'rb')

    def after_read(self):
        print('returning file pointer to beginning')
        self._file.seek(0)

    def read_file(self):
        return self._file.read()


    def close_file(self):
        self._file.close()


binary = BinTextFileHandler()
print(binary.content_file('test.txt'))

text = TextFileHandler()
print(text.content_file('test.txt'))
