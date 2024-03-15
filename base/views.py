from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .utils import Decoder

# Create your views here.

@csrf_exempt
def get_instruction(request):
    return HttpResponse(
        '''@FBBFFBRLFBRL$'''
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