from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=12)

with open("analysis_summary.txt", "r") as file:

    for line in file:

        pdf.cell(200, 10, txt=line, ln=True)

pdf.output("Asset_Report.pdf")

print("PDF Generated")