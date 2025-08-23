import pypandoc as doc
import os
from util.extract_pdf import converter 

#NAO DA PRA CONVERTER SLIDE PRA PDF

def to_pdf(tipo,path): 
    if tipo == 'pdf':
        text = converter(path)
        x = doc.convert_text( text,
                         to="pdf",
                         format="markdown",outputfile="teste.pdf",
                         extra_args=[
        "--pdf-engine=xelatex",
        "-V", "fontsize=12pt",
        "-V", "geometry:top=2cm,left=1.5cm,right=2cm,bottom=2cm",
        "-H", "format/header.tex" 
    ])
        
    else:
        x = doc.convert_file( path,
                         to="pdf",
                         format=tipo,outputfile="teste.pdf",
                         extra_args=[
        "--pdf-engine=xelatex",
        "-V", "fontsize=12pt",
        "-V", "geometry:top=2cm,left=1.5cm,right=2cm,bottom=2cm",
        "-H", "format/header.tex" 
    ])
    print(x)

#to_pdf("markdown","teste/text_example.txt" ) # txt - pdf FEITO 
#to_pdf("pdf","teste/Modules.pdf") # pdf - pdf FEITO (inutil,mas feito)
#to_pdf("docx","teste/world.docx") # docx - pdf FEITO




