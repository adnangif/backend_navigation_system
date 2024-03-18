from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .utils import Decoder,read_qr_code,Map,Point

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
found_qrcode = False
not_found_str = "Could not find the given QR Code"

def get_instruction(request):

    return HttpResponse(
        '''@FBBFFBRLFBRL$'''
    )


@csrf_exempt
def evaluate_qr(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        file = request.FILES['file']
        # print(file.read())
        return HttpResponse(f"result is: {Decoder(file.read())}" )


    if request.method == "GET":
        form = UploadFileForm()
        return render(request=request,template_name='base/upload.html',context={"form": form})

class Store:
    result = "@UUUUSSSSSS$"

    def set(self,x:str):
        self.result = x
    def get(self):
        return self.result
        

store = Store()

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        try:
            data = request.body
            with open('uploaded_image.jpg', 'wb') as f:
                f.write(data)
            
            qr_data = read_qr_code('uploaded_image.jpg')

            if(not qr_data):
                print("No valid data")
                qr_data.append('3,5')

            if(qr_data):
                fitem:str = qr_data[0]

                x = int(fitem.split(',')[0])
                y = int(fitem.split(',')[1])

                m = Map(Point(x,y),
                [
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                ])
                m.bfs()

                print(m.path())

                p = (m.transformed_path())
                while len(p) < 10:
                    p += 'S'

                p = '@' + p + '$'
                print(p)
                # result = p
                store.set(p)
                return HttpResponse(p)
            

            return HttpResponse('Not Found')

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif(request.method == "GET"):
        return HttpResponse(store.get())
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)