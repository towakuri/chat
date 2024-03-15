#%%
import qrcode

# QRコードにするデータ
data = "https://"

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
