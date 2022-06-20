from create_qrcode import QRCodeCreator
from read_qrcode import ReadQRCode

if __name__ == '__main__':
    qrcode = QRCodeCreator("first", "Testing")
    qrcode.create_qrcode()
    read_qrcode = ReadQRCode('first.png')
    read_qrcode.decode_qr_code()
