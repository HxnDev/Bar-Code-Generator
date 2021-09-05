from barcode import EAN13   # Install using "pip install python-barcode" and "pip install pillow"
from barcode.writer import ImageWriter

num = input("Enter the number whose barcode you want to generate = ")
code = EAN13(num, writer=ImageWriter())     # Generating barcode
code.save("barcode")    # Saving as png image
