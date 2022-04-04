import qrcode

data = 'Hello world'

img = qrcode.make(data)
img.save()