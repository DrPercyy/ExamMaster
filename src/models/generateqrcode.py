import qrcode

class QrCode:
    def __init__(self, data):
        self.data = data

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img