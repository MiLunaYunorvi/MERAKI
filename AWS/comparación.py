from logging import root
import boto3
from botocore.exceptions import ClientError
from tkinter import *
from tkinter import filedialog

def image_a_byte(ruta_imagen):
    with open(ruta_imagen,'rb') as imagen:
        return imagen.read()

def comparar_rostros(ruta_imagen1,ruta_imagen2):
    bytes_1=image_a_byte(ruta_imagen1)
    bytes_2=image_a_byte(ruta_imagen2)
    cliente = boto3.client('rekognition')

    try:
        respuesta= cliente.compare_faces(SourceImage={'Bytes': bytes_1},
                                     TargetImage={'Bytes': bytes_2})
        if respuesta and respuesta['ResponseMetadata']['HTTPStatusCode'] == 200:
            for i in respuesta['UnmatchedFaces']:
                print(i)
            
            for i in respuesta['FaceMatches']:
                print('Similarity: '+str(i['Similarity']))

    except ClientError as error:
        print('Problemas al llamar al servicio: ')

if __name__=="__main__":
    root=Tk()
    ruta_imagen1 = filedialog.askopenfilename(title="imagen",initialdir='C:',filetypes=(("Imagenes PNG",".png"),("Imágenes JPEG",".jpeg"),('todos','.*')))
    ruta_imagen2 = filedialog.askopenfilename(title="imagen",initialdir='C:',filetypes=(("Imagenes PNG",".png"),("Imágenes JPEG",".jpeg")))
    comparar_rostros(ruta_imagen1,ruta_imagen2)
    root.mainloop()
