import pypandoc as doc
from UTILS.extract_pdf import converter 
import sys
import os


def resource_path(relative_path: str) -> str:
    """Pega o caminho correto mesmo se rodar via PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def to_pdf(tipo, path):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(path))[0]
    output_path = os.path.join(upload_dir, f"{base_name}.pdf")

    if tipo == 'pdf':
        text = converter(path)
        doc.convert_text(
            text,
            to="pdf",
            format="markdown",
            outputfile=output_path,
            extra_args=[
                "--pdf-engine=xelatex",
                "-V", "fontsize=12pt",
                "-V", "geometry:top=2cm,left=1.5cm,right=2cm,bottom=2cm",
                "-H", resource_path("FORMATS/header.tex")
            ]
        )
    else:
        doc.convert_file(
            path,
            to="pdf",
            format=tipo,
            outputfile=output_path,
            extra_args=[
                "--pdf-engine=xelatex",
                "-V", "fontsize=12pt",
                "-V", "geometry:top=2cm,left=1.5cm,right=2cm,bottom=2cm",
                "-H", resource_path("FORMATS/header.tex")
            ]
        )

    return f"Conversão de Arquivo Completa! Arquivo gerado em: {os.path.abspath(output_path)}"


def to_txt(tipo, path):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(path))[0]
    output_path = os.path.join(upload_dir, f"{base_name}.txt")

    if tipo == 'pdf':
        text = converter(path)
        doc.convert_text(text, to="markdown", format="markdown", outputfile=output_path)
    else:
        doc.convert_file(path, to="markdown", format=tipo, outputfile=output_path)

    return f"Conversão de Arquivo Completa! Arquivo gerado em: {os.path.abspath(output_path)}"


def to_docx(tipo, path):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(path))[0]
    output_path = os.path.join(upload_dir, f"{base_name}.docx")

    if tipo == 'pdf':
        text = converter(path)
        doc.convert_text(
            text,
            to="docx",
            format="markdown",
            outputfile=output_path,
            extra_args=["--reference-doc=" + resource_path("FORMATS/modelo.docx")]
        )
    else:
        doc.convert_file(
            path,
            to="docx",
            format=tipo,
            outputfile=output_path,
            extra_args=["--reference-doc=" + resource_path("FORMATS/modelo.docx")]
        )

    return f"Conversão de Arquivo Completa! Arquivo gerado em: {os.path.abspath(output_path)}"


def to_pptx(tipo, path):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(path))[0]
    output_path = os.path.join(upload_dir, f"{base_name}.pptx")

    if tipo == 'pdf':
        text = converter(path)
        doc.convert_text(
            text,
            to="pptx",
            format="markdown",
            outputfile=output_path,
            extra_args=["--reference-doc=" + resource_path("FORMATS/format.pptx")]
        )
    else:
        doc.convert_file(
            path,
            to="pptx",
            format=tipo,
            outputfile=output_path,
            extra_args=["--reference-doc=" + resource_path("FORMATS/format.pptx")]
        )

    return f"Conversão de Arquivo Completa! Arquivo gerado em: {os.path.abspath(output_path)}"


def iniciar(x, tipo, path):
    if x == '1':
        return to_pdf(tipo, path)
    elif x == '2':
        return to_txt(tipo, path)
    elif x == '3':
        return to_docx(tipo, path)
    elif x == '4':
        return to_pptx(tipo, path)
    else:
        return "Opção inválida! Use: 1=pdf | 2=txt | 3=docx | 4=pptx"


if __name__ == "__main__":
    try:
        print(iniciar(sys.argv[1], sys.argv[2], sys.argv[3]))
    except Exception as e:
        print("Erro ao Converter o Arquivo:", e)
