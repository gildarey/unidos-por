from django.shortcuts import render
from .models import Evento, Emprendimiento
from .form import EventoForm
from django.http import JsonResponse
from django.conf import settings
from decimal import Decimal, DecimalException
from django.core import serializers
from django.http import HttpResponse
from django.utils.html import escape
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import BadHeaderError, send_mail
from datetime import datetime, timedelta, time
import re
import traceback

def inicio(request):
    try:
        today = datetime.now().date()
        eventos = Evento.objects.filter(categoria='otros',fecha__gt=today).order_by('fecha')[:3]
        emprendimientos = Emprendimiento.objects.filter(categoria='emprendimiento')[:1]
        context = {'eventos': eventos, 'current_page': "home", 'emprendimientos': emprendimientos}
        return render(request, 'index.html', context)
    except Exception as e:
        print(traceback.format_exc())
        eventos = Evento.objects.all()
        context = {'records': None, 'current_page': "home"}
        return render(request, 'index.html', context)

def about(request):
    context = {'current_page': "about"}
    return render(request, 'about.html', context)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    return render(request, '404.html', status=500)


def getEventos(request):
    if request.is_ajax and request.method == "GET":
        ciudad = request.GET.get("ciudad", None)
        if Evento.objects.filter(ciudad = ciudad).exists():
            eventos = Evento.objects.filter(ciudad=ciudad)[:5]
            data = serializers.serialize('json', list(eventos))
            #  fields=('id','evento','organizador','fecha','telefono','email','meta','costo','direccion','ciudad','descripcion','latitud','longitud')
            return JsonResponse(data, status = 200, safe=False)
        else:
            return JsonResponse({"found": False}, status = 200, safe=False)

    return JsonResponse({}, status = 400)
    

def eventos(request):
    categoria = request.GET.get('categoria')
    page = request.GET.get('page', 1)
    try:
        if categoria is None:
            # eventos = Evento.objects.all()[:4]
            evento_list = Evento.objects.all()[:1000]
            paginator = Paginator(evento_list, 4)
            validate = validatePagination(page, paginator.num_pages)

            if validate:
                eventos_page = paginator.page(page)
            else:
                eventos_page = paginator.page(1)

            context = {'google_api': settings.GOOGLE_MAPS_API_KEY, 'current_page': 'events', 'records': evento_list}
            return render(request, 'eventos.html', context)
        else:
            if Evento.objects.filter(categoria = categoria).exists():
                evento_list = Evento.objects.filter(categoria=categoria)
                paginator = Paginator(evento_list, 4)
                validate = validatePagination(page, paginator.num_pages)
                if validate:
                    eventos_page = paginator.page(page)
                else:
                    eventos_page = paginator.page(1)

                context = {'google_api': settings.GOOGLE_MAPS_API_KEY, 'current_page': 'events', 'records': eventos_page}
                return render(request, 'eventos.html', context)
            else:
                eventos = Evento.objects.all()[:4]
                context = {'google_api': settings.GOOGLE_MAPS_API_KEY, 'current_page': 'events', 'records': eventos}
                return render(request, 'eventos.html', context)

    except Exception as e:
        print(traceback.format_exc())
        eventos = Evento.objects.all()[:4]
        context = {'records': None, 'current_page': "home"}
        return render(request, 'index.html', context)

def crearEvento(request):
    form = EventoForm()
    response_data = {}

    if request.method == 'POST':

        lastId = 1
        try:
            lastId = int(Evento.objects.latest('id').pk) + 1
        except Evento.DoesNotExist:
            lastId = 1

        try:
            evento = request.POST.get('evento')
            organizador = request.POST.get('organizador')
            fecha = request.POST.get('fecha')
            categoria = request.POST.get('categoria')
            image = request.FILES.get('images')
            # testing = request.FILES.get('images').name

            telefono = request.POST.get('telefono')
            beneficiario = request.POST.get('beneficiario')
            benef = re.sub('[^a-zA-Z0-9 \n\.]', '', str(beneficiario)).lower()

            medios = request.POST.get('medios')
            meta = request.POST.get('meta')
            costo = request.POST.get('costo')
            direccion = request.POST.get('direccion')
            ciudad = request.POST.get('ciudad')
            descripcion = request.POST.get('descripcion')
            url = benef.replace(" ", "-") + "-" + str(lastId)    

            lng = Decimal(request.POST.get('long'))
            lat = Decimal(request.POST.get('lat'))

            newEvento = Evento.objects.create(
             evento = evento,
             beneficiario = beneficiario,
             categoria = categoria,
             url = url,
             image=image,
             organizador = organizador,
             fecha = fecha,
             telefono = telefono,
             medios = medios,
             meta = meta,
             costo = costo,
             direccion = direccion,
             ciudad = ciudad,
             descripcion = descripcion,
             latitud = lat,
             longitud = lng
             )
            response_data['url'] = url
            return JsonResponse(response_data)

        except Exception as e:
            print(traceback.format_exc())
            response_data['error'] = traceback.format_exc()
            return JsonResponse(response_data)

        response_data['error'] = 'Unexpected error ocurred, please check all data.'
        return JsonResponse(response_data)

    context = {'google_api': settings.GOOGLE_MAPS_API_KEY, 'form': form, 'current_page': 'form'}
    return render(request, 'form.html', context)

def evento_detail(request, id):
    evento  = Evento.objects.get(url=id)
    context = {'detalle': evento, 'current_page': 'evento_detalle'}
    return render(request, 'evento_detalle.html', context)

def reportar(request):
    form = EventoForm()
    response_data = {}

    if request.method == 'POST':

        try:
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            descripcion = request.POST.get('descripcion')
            asunto = request.POST.get('asunto')
            telefono = request.POST.get('telefono')
            body = 'Nombre: ' + nombre + '. Telefono: ' + telefono + '. Descripcion: ' + descripcion

            if asunto and descripcion and email:
                send_mail(asunto, body, email, ['admin@gildarey.dev'], fail_silently=False,)
                response_data['msg'] = 'Se envio correctamete el mail.'
                return JsonResponse(response_data)
            else:
                response_data['msg'] = 'Hubo un error.'
                return JsonResponse(response_data)

        except Exception as e:
            print(traceback.format_exc())
            response_data['error'] = traceback.format_exc()
            return JsonResponse(response_data)

        response_data['error'] = 'Unexpected error ocurred, please check all data.'
        return JsonResponse(response_data)

    context = {'form': form, 'current_page': 'reportar'}
    return render(request, 'reportar.html', context)

def validatePagination(page, numbers_of_page):
    try:
        if page is None:
            return False
        else:
            new_number = int(numbers_of_page) + 1
            new_page = int(page)
            return new_page < new_number
    except:
        return False