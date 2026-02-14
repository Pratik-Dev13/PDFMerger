from django.shortcuts import render
from django.http import HttpResponse ,FileResponse
from pypdf import PdfWriter
from pdfmerger import settings
import os


def merger(request):
    if request.method=="POST":
        merger = PdfWriter()
        try:
            for pdf in request.FILES.getlist('pdfs'):
                merger.append(pdf)

            output_path=os.path.join(settings.MEDIA_ROOT,"merged.pdf")

            with open(output_path , "wb") as file:


                merger.write(file)
            file.close()
        except:
            pass
        return FileResponse(open(output_path,"rb"),as_attachment=True , filename="mergedfile.pdf")
    
    

    return render(request,'merger/pdf_merger.html')
 

 
    