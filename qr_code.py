#%%
import qrcode

# QRコードにするデータ
data = "file:///Users/az299/Desktop/towa_practice/webchat/templates/index.html"

# QRコードの生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# QRコードを画像として保存
img = qr.make_image(fill_color="black", back_color="white")
img.save("example_qrcode.png")

# %%
