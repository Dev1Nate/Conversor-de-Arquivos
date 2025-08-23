import pypandoc as doc
import os


#NAO DA PRA CONVERTER SLIDE PRA PDF
# docx - pdf FEITO
# txt - pdf FEITO
def to_pdf(tipo): 
    x = doc.convert_file( "processo de pdf",
                         to="pdf",
                         format=tipo,outputfile="teste.pdf",
                         extra_args=[
        "--pdf-engine=xelatex",
        "-V", "fontsize=12pt",
        "-V", "geometry:top=2cm,left=1.5cm,right=2cm,bottom=2cm",
        "-H", "format/header.tex" 
    ])
    print(x)

to_pdf("pdf")





