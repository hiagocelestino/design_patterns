from abc import ABC, abstractmethod

class DocumentConverter(ABC):

    def converter_document(self, filename):
        self.load_document(filename)
        self.parse_to_target_format()
        self.convert_to_format()
        self.save_document()

    @abstractmethod
    def load_document(self, filename):
        ...

    @abstractmethod
    def parse_to_target_format(self):
        ...

    @abstractmethod
    def convert_to_format(self):
        ...
    
    @abstractmethod
    def save_document(self):
        ...


class PdfConverter(DocumentConverter):

    def load_document(self, filename):
        print(f'load document {filename}...')

    def parse_to_target_format(self):
        print('parsing content to pdf conversion')

    def convert_to_format(self):
        print('converting content to pdf')
    

    def save_document(self):
        print('save document as pdf')


class DocxConverter(DocumentConverter):

    def load_document(self, filename):
        print(f'load document {filename}...')

    def parse_to_target_format(self):
        print('parsing content to docx conversion')

    def convert_to_format(self):
        print('converting content to docx')
    

    def save_document(self):
        print('save document as docx')


pdf_converter = PdfConverter()
docx_converter = DocxConverter()

pdf_converter.converter_document('file.pdf')
docx_converter.converter_document('file.docx')