from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Check checkbox values
    removepun = request.POST.get('removepuncuation', 'off')
    uppercase = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremove', 'off')
    numberremover = request.POST.get('removenumber', 'off')

    # check which checkbox is on
    if removepun == "on":
        punctuations = '''""’'()[]{}<>:,‒―…!.«»-‐?‘’“”;/⁄␠·&@*\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|¦⁂☞∴‽※'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'Analyzed_text': analyzed}
        djtext = analyzed
    
    if(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase','Analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line' , 'Analyzed_text':analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not ( djtext[index] == " " and djtext[index+1] == " " ):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces' , 'Analyzed_text':analyzed}
        djtext = analyzed

    if(numberremover == "on"):
        numbers= '0123456789'
        analyzed = ""
        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        params = {'purpose': 'Remove the Numbers','Analyzed_text': analyzed}
        djtext = analyzed
    
    if (removepun != "on" and uppercase !="on" and newlineremover !="on" and extraspaceremover != "on" and numberremover != "on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request, 'analyze.html', params)
