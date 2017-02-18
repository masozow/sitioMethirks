from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder #para decofificar todos los datos de MySql
from django.core.mail import send_mail #Falta configurar los settings

def index(request):
    return render(request, 'pagina/index.html', {})


def correo_electronico(request):
    if request.method=='POST':
        form_contacto=Form_Contacto(request.POST) #se obtiene el formulario que vino con el request
        if form_contacto.is_valid(): #se comprueba que el formulario sea válido, es decir, que cumpla con las restricciones descritas en el model
            datos_contacto=form_contacto.cleaned_data
            from_email=settings.EMAIL_HOST_USER
            to_list=[from_email]
            send_mail(datos_contacto['asunto_contacto'],'De: '+datos_contacto['nombre_contacto']+' <'+datos_contacto['correo_contacto']+'>'+'\n\n' +datos_contacto['mensaje_contacto'],from_email,to_list,fail_silently=False)
            #guardar=form_contacto.save()
            form_contacto=Form_Contacto() #se obtiene un formulario limpio
    else:
        form_contacto=Form_Contacto() #se obtiene el formulario que vino con el request
    return render(request, 'kadoshapp/WEBcontacto.html', {'form_contacto':form_contacto})
