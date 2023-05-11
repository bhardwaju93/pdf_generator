from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics (1).csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=40)
    pdf.set_text_color(100, 40, 60)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    pdf.line(10, 21, 200, 21)

    # Setting the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(100, 40, 60)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(100, 40, 60)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")


pdf.output("output.pdf")
