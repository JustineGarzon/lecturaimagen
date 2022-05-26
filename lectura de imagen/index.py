#Librería
import cv2
from cv2 import imshow
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="cafe"
#Lectura de imagen
img=cv2.imread(imgText+'.png')
imshow('Imagen Original',img)
img=cv2.imread(imgText+".png", cv2.IMREAD_GRAYSCALE)
imshow ("Imagen Escala De Grises", img)


 




cv2.waitKey(0)
cv2.destroyAllWindows()