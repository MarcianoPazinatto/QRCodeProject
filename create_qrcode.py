import qrcode
import os


class QRCodeCreator:

    def __init__(self, name_file, phrase):
        self.name_file = name_file
        self.phrase = phrase

    def create_qrcode(self) -> None:
        self.insert_name_file()
        img = qrcode.make(self.phrase)
        img.save(self.name_file)

    def insert_name_file(self) -> str:
        self.name_file: str = self.name_file + ".png"
        self.validate_name(self.name_file)
        return self.name_file

    def validate_name(self, file: str) -> str:
        count = 0
        while os.path.isfile(file):
            file: str = self.name_file
            count += 1
            file: str = self.assign_new_values_to_the_file(count, file)
            self.name_file = file
        return self.name_file

    @staticmethod
    def assign_new_values_to_the_file(count: int, file: str) -> str:
        if ")" in file[-5]:
            return file.split('.')[0][0:-3] + f"({count})" + "." + file.split('.')[1]
        return file.split('.')[0] + f"({count})" + "." + file.split('.')[1]
