from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess as sp
from subprocess import Popen, PIPE, STDOUT

# Create your views here.

def ceditor(request):

    return render(request,"ceditor.html")

@csrf_exempt
def save_data(request):
   

    if request.method == "POST":
        
        # print(request.POST['code'])
        f = open("codec.c", "w")
        f.write(request.POST['code'])
        f.close()
        print(request.POST['stdin'])
        # output = sp.getoutput('gcc codec.c -o codec && "/home/abhay/Desktop/terminal-webpage/terminal/"codec')
        output = sp.Popen('gcc codec.c -o codec && "/home/abhay/Desktop/terminal-webpage/terminal/"codec',shell=True,stdout=PIPE, stdin=PIPE, stderr=STDOUT)
#         lst=[2,3,2,4]
# string=""
# for i in lst:
#     string+=str(i)+"\\n"

# print(string)
        output.stdin.write( bytes(request.POST['stdin'], 'utf-8')) 
        grep_stdout = output.communicate()[0]
        print(grep_stdout.decode())

 
 

        # print(output)
        

        return JsonResponse({'status': grep_stdout.decode()})
    else:
        return JsonResponse({"status": 'fail'})
