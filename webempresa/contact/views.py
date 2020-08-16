from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    form = ContactForm()
    # print("Tipo de peticion: {}".format(request.method))
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviar mensaje
            emailMessage = EmailMessage(
                "La Caffettiera: Mensaje de contacto",
                "De {} <{}>\n\nEscribio:{}".format(name, email, content),
                "no-contestar@inbox.mailtramp.io",
                ["jesusalbertoramirezlopez.jr@gmail.com"],
                reply_to=[email]
            )
            try:
                emailMessage.send()
                # redireccionar todo bien
                return redirect(reverse('contact')+'?ok=True')
                pass
            except:
                # redireccionar error
                return redirect(reverse('contact')+'?ok=False')
                pass

            
        
                
    return render(request, "contact/contact.html", {'form': form})