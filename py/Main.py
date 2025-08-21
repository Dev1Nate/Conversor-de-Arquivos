import pypandoc as doc


#doc.convert_file
for i in doc.get_pandoc_formats()[1]:
    print(i)