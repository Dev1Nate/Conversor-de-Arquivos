import pypandoc as doc
import os
from util.extract_pdf import converter 

#NAO DA PRA CONVERTER SLIDE PRA PDF(mas da para fazer se estiver em um linux)

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


#================

def to_txt(tipo,path):
    if tipo == 'pdf':
        text = converter(path)
        x = doc.convert_text( text,
                         to="markdown",
                         format="markdown",outputfile="teste.txt"
                         )
        
    else:
        x = doc.convert_file( path,
                         to="markdown",
                         format=tipo,outputfile="teste.txt"
                         )
    print(x)


#to_txt("markdown","teste/text_example.txt" )
#to_txt("pdf","teste/Modules.pdf")
#to_txt("docx","teste/world.docx")


#================

def to_docx(tipo,path):
    if tipo == 'pdf':
        text = converter(path)
        x = doc.convert_text( text,
                         to="docx",
                         format="markdown",outputfile="teste.docx",extra_args=[
        "--reference-doc=format/modelo.docx"
    ]
                         )
        
    else:
        x = doc.convert_file( path,
                         to="docx",
                         format=tipo,outputfile="teste.docx",extra_args=[
        "--reference-doc=format/modelo.docx"
    ] 
                         )
    print(x)


#to_docx("markdown","teste/text_example.txt" )
#to_docx("pdf","teste/Modules.pdf")
#to_docx("docx","teste/world.docx")


#================

def to_pptx(tipo,path):
    if tipo == 'pdf':
        text = converter(path)
        x = doc.convert_text( text,
                         to="pptx",
                         format="markdown",outputfile="teste.pptx", extra_args=[
        "--reference-doc=format/format.pptx"
    ]
                         )
        
    else:
        x = doc.convert_file( path,
                         to="pptx",
                         format=tipo,outputfile="teste.pptx", extra_args=[
        "--reference-doc=format/format.pptx"
    ]
                         )
    print(x)


to_pptx("markdown","teste/text_example.txt" )
#to_pptx("pdf","teste/Modules.pdf")  #fica bugado devido aos tamanhos
#to_pptx("docx","teste/world.docx")
