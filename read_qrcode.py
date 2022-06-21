from typing import NoReturn

import cv2
from pyzbar.pyzbar import decode


class ReadQRCode:
    def __init__(self, path_file):
        self.path_file = path_file

    def decode_qr_code(self) -> str:
        try:
            img = cv2.imread(self.path_file)

            for code in decode(img):
                print(code.type)
                print(code.data)
                print(code.data.decode("utf-8"))
                return code.data.decode("utf-8")
        except TypeError as ex:
            print(str(ex))
