from re import A
import pdftables_api
import os
import tabula

#Asignación de ruta para analziar
pdf_directory = '/Users\Precitrl\Desktop\ANÁLISIS DATOS\SCRIPT'
excel_directory = '/Users\Precitrl\Desktop\ANÁLISIS DATOS\SCRIPT'
#Listar carpetas y archivos del directorio declarado
archivos = os.listdir(pdf_directory)
archivos_convertibles=[]
#file_to_convert=[]
for fichero in archivos:
    #Condicional para verificar que el archivo cumpla con el formato pdf
    if os.path.isfile(os.path.join(pdf_directory,fichero)) and fichero.endswith('.pdf'):
        archivos_convertibles.append(fichero)        
        
        #Uso de API de conversión de PDFTables
        #conversion= pdftables_api.Client('dcrph9trhd53')

        #Asignación de ruta de archivo y nombre del archivo
        #conversion.xlsx_multiple(fichero,fichero.join("_excel"))

#        file_to_convert=tabula.read_pdf(fichero, pages='all',output_format='json')
        #print(help(tabula))
        #exit()
        #print(file_to_convert)
        #file_to_convert.to_excel(fichero+'.xlsx', encoding='utf-8')
        tabula.io.convert_into(pdf_directory+"\\"+fichero,excel_directory+"\\"+fichero[:-3]+"csv", output_format="csv",pages='all')

        #Impresión de mensaje exitoso
        print("Documento -- "+fichero+"-- convertido exitosamente!!")
    else:
        #Impresión de mensaje de archivos no convertibles        
        print("Documento --"+fichero+"-- no convertible")

#Comprobación en consola de archivos escaneados y convertidos
print("Directorios/Ficheros convertidos: ")
print(archivos_convertibles)