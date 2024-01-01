import pyqrcode


def gen_qr_code(data, file_name):
    qr = pyqrcode.create(data)
    qr.png(path+file_name, scale=6)
    print("QR Generation success!")


path = "C:\\Users\\Palli Chandra Sekhar\\Desktop\\TTS\\QR\\"
name = "LoveCode.png"
msg = "I Love You Kumari"
gen_qr_code(msg, name)
