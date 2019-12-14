import cv2


def zh_ch(string):
    return string.decode().encode("gbk")


img = cv2.imread("source.jpg")

cv2.

# cv2.imshow(u"测试窗口", img)
# cv2.waitKey(10000)
