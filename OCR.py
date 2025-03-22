# 一个OCR文字识别
import cv2
import pytesseract

# 读取图片
img = cv2.imread(r'imgs/img.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 识别文字
text = pytesseract.image_to_string(binary)

print(text)