from django.shortcuts import render, redirect
from contact.forms import UserForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        frm = UserForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect(send)
    else:
        frm = UserForm()
    return render(request, 'index.html', {'ff':frm})
        

def send(request):
    return render(request, 'success.html')
        