import PyPDF2 as pdf

def converter(path):
    with open(path, 'rb') as arquivo:
        leitor = pdf.PdfReader(arquivo)
        all_text = ""

        for i in leitor.pages:
            texto = i.extract_text()
            if texto:
                all_text += texto + "\n"
        
        return all_text