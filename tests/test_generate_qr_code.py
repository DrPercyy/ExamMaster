import sys
sys.path.append('.')
import unittest, qrcode
from unittest.mock import patch

from src.models.generateqrcode import QrCode

class QrCodeTests(unittest.TestCase):
    def test_generate_qrcode(self):
        data = "Hello, World!"
        qr_code = QrCode(data)
        expected_img = "mocked_image"

        with patch("qrcode.QRCode") as mock_qrcode:
            mock_qrcode.return_value.make_image.return_value = expected_img

            result = qr_code.generate_qrcode()

            mock_qrcode.assert_called_once_with(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            mock_qrcode.return_value.add_data.assert_called_once_with(data)
            mock_qrcode.return_value.make.assert_called_once_with(fit=True)
            mock_qrcode.return_value.make_image.assert_called_once_with(
                fill_color="black", back_color="white"
            )

        self.assertEqual(result, expected_img)


if __name__ == "__main__":
    unittest.main()