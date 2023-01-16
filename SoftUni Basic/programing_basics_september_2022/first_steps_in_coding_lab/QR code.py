import pyqrcode
# import png
# from pyqrcode import QRCode

address = "https://www.cars.bg/offer/631b55a314b357daae0d6982"
url = pyqrcode.create(address)
url.png('exampleQR.png', scale=10)

