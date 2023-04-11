#Extract Text from PDF using python
#pip install PyPDF2
import PyPDF2

with open("mypdf.pdf", "rb") as pdf_file:
    
    pdf_reader=PyPDF2.PdfReader(pdf_file)   #se crea un PDF reader object
    num_pages =len(pdf_reader.pages)        #obtiene el arreglo de paginas con la propiedad 'pages'
    text=''
    for page in range(num_pages):           #se recorre cada pagina del archivo
        page_obj= pdf_reader.pages[page]    #con la propiedad 'pages' se obtiene cada pagina
        text +=page_obj.extract_text()      #se extrae el texto y se concatena a la variable 'text'
    
    print(text)
    

#DEPRECTED METHODS
#pdf_file= open("mypdf.pdf","rb")
#PDF_Reader=PyPDF2.PdfFileReader(pdf_file)
#texts = PDF_Reader.getPage(0).extractText()

#print(texts)
