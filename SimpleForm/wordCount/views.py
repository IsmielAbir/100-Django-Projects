from django.shortcuts import render

def countWord(request):
    if request.method == 'POST':
        txt = request.POST.get('text', '')  # Use get() method to retrieve the value from the textarea
        amount = len(txt.split())
        return render(request, 'word.html', {'amount': amount})
    else:
        return render(request, 'word.html')
