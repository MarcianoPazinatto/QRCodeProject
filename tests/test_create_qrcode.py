from create_qrcode import QRCodeCreator
import pytest


class TestQRCodeCreator:

    def test_create_qrcode(self, mocker):
        # Arrange
        mocker_insert_name_file = mocker.patch('create_qrcode.QRCodeCreator.insert_name_file')
        mocker_make = mocker.patch('create_qrcode.qrcode.make')
        a = QRCodeCreator('name', 'name_path')

        # Action
        a.create_qrcode()

        # Assert
        mocker_insert_name_file.assert_called()
        mocker_make.assert_called()

    def test_insert_name_file(self, mocker):
        # Arrange
        mocker_validate_name = mocker.patch('create_qrcode.QRCodeCreator.validate_name')
        a = QRCodeCreator('name', 'name_path')

        # Action
        response = a.insert_name_file()

        # Action
        assert response == 'name.png'

