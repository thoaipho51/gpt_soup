import streamlit as st
import time
import cv2
from imutils.video import VideoStream
from pyzbar.pyzbar import decode


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)


# img = cv2.imread('img/qrcode_test.png')
# barcode_demo = cv2.imread('img/barcode_demo.png')

f_with = 640
f_height = 480

video = VideoStream(src=0, width=f_with, height=f_height).start()

camera = True
list_code = []
list_product = []


def write_f(list_product):
    # Mở một tệp txt để ghi dữ liệu
    with open("products.txt", "a", encoding='utf-8') as file:
        for product in list_product:
            # Ghi từng dòng vào tệp txt
            file.write(f"{product['code']} - {product['name']} - {product['price']}\n")


def write_f(product):
    # Mở một tệp txt để ghi dữ liệu
    with open("products.txt", "a", encoding='utf-8') as file:
        # Ghi từng dòng vào tệp txt
        file.write(f"{product['code']} - {product['name']} - {product['price']}\n")


# Vòng white
while camera:

    with open("products.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            barcode = line.split(' - ')[0]
            if barcode not in list_code:
                list_code.append(barcode)

    print(list_code)
    frame = video.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in list_code:
            name = input('Nhập tên sản phẩm:')
            price = input('Giá:')
            product = {
                'code': code.data.decode('utf-8'),
                'name': name,
                'price': price
            }
            print(f'Nhập code : {code.data.decode("utf-8")} Thành Công ! - {name}')
            write_f(product)
            time.sleep(3)

        else:
            with open("products.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    barcode = line.split(' - ')[0]
                    name = line.split(' - ')[1]
                    price = line.split(' - ')[2]
                    if barcode == code.data.decode('utf-8'):
                        print(f"Tên: {name} Giá: {price}")

            time.sleep(3)

    cv2.imshow('Testing_scan_code', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
video.stop()