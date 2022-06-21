import sys

import pytest

from read_qrcode import ReadQRCode


class TestQRCodeRead:

    def test_create_qrcode(self):
        # Arrange
        if len(sys.argv) == 2:
            qr_code = ReadQRCode('../tests/file_test/first.png')
        else:
            qr_code = ReadQRCode('tests/file_test/first.png')

        # Action
        response = qr_code.decode_qr_code()

        # Assert
        assert response == 'Testing'

    def test_create_qrcode_error(self):
        # Arrange

        qr_code = ReadQRCode('')
        qr_code.path_file = ''
        # Action

        response = qr_code.decode_qr_code()

        assert response is None
