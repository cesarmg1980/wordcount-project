from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    text_content = request.GET['fulltext']
    content_list = text_content.split()
    word_count = {}
    for word in content_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count.items())
    return render(request, 'count.html', {'text_content':text_content, 
        'count':len(content_list), 
        'wordcount': word_count.items()})

def about(request):
    return render(request, 'about.html')