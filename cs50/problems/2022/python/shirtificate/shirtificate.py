#wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png
#pip install fpdf2

from fpdf import FPDF
from PIL import Image
from fpdf import Align

shirt = Image.open("shirtificate.png")

pdf = FPDF(orientation = "portrait", format = "A4")
pdf.add_page()

pdf.image(shirt, w = pdf.eph*.7, x=Align.C, y=70)

pdf.set_font("helvetica", "", 50)
pdf.cell( w = 0 , h = 50, txt = "CS50 Shirtificate", align = 'C', new_x = "LMARGIN" )

pdf.set_font("helvetica", "", 24)
pdf.set_text_color(r = 255, g=255, b=255)
pdf.cell( w = 0 , h = 250, txt = "Gabriel Martinez took CS50", align = "C", new_y = "NEXT" )

pdf.output("shirtificate.pdf")