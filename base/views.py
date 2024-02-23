from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .utils import Decoder

# Create your views here.


def get_instruction(request):
    return HttpResponse(
        '''
        <html>
            <h1>This was generated in the laptop </h1>
        </html>
        '''
    )



def evaluate_qr(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        file = request.FILES['file']
        # print(file.read())
        return HttpResponse(f"result is: {Decoder(file.read())}" )


    if request.method == "GET":
        form = UploadFileForm()
        return render(request=request,template_name='base/upload.html',context={"form": form})