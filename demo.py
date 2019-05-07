#!/usr/bin/env python
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas

c = canvas.Canvas('rldemo3.pdf', pagesize=letter)
width, height = letter
c.drawString(inch, height - inch, '1 inch')
c.drawString(inch, height - 2 * inch, '2 inches')
c.drawString(cm, cm, '1 cm')
c.drawString(cm, 2 * cm, '2 cm')
c.showPage()
c.save()