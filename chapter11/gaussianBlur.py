from PIL import Image, ImageFilter

kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)  # 高斯模糊
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()
