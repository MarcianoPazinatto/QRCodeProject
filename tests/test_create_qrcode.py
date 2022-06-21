from create_qrcode import QRCodeCreator
import pytest


class TestQRCodeCreator:

    def test_create_qrcode(self, mocker):
        # Arrange
        mocker_insert_name_file = mocker.patch('create_qrcode.QRCodeCreator.insert_name_file')
        mocker_make = mocker.patch('create_qrcode.qrcode.make')
        qr_code = QRCodeCreator('name', 'name_path')

        # Action
        qr_code.create_qrcode()

        # Assert
        mocker_insert_name_file.assert_called()
        mocker_make.assert_called()

    def test_insert_name_file(self, mocker):
        # Arrange
        mocker_validate_name = mocker.patch('create_qrcode.QRCodeCreator.validate_name')
        qr_code = QRCodeCreator('name', 'name_path')

        # Action
        response = qr_code.insert_name_file()

        # Action
        assert response == 'name.png'

    def test_validate_name(self, mocker):
        # Arrange
        mocker_validate_name = mocker.patch('create_qrcode.os.path.isfile', return_value=False)
        mocker_validate_name2 = mocker.patch('create_qrcode.QRCodeCreator.assign_new_values_to_the_file')
        qr_code = QRCodeCreator('name', 'name_path')

        # Action
        response = qr_code.validate_name("name")

        # Action
        assert response == 'name'
        mocker_validate_name2.assert_not_called()

    def test_assign_new_values_to_the_file_renaming_the_file_more_than_once(self):
        # Arrange
        qr_code = QRCodeCreator('name', 'name_path')

        # Action
        response = qr_code.assign_new_values_to_the_file(2, "name.png")

        # Action
        assert response == 'name(2).png'

    def test_assign_new_values_to_the_file(self, mocker):
        # Arrange
        qr_code = QRCodeCreator('name', 'name_path')

        # Action
        response = qr_code.assign_new_values_to_the_file(1, "name.png")

        # Action
        assert response == 'name(1).png'
