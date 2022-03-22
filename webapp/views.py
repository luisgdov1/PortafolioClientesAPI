import datetime
import json
import xlwt
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from clientes.models import Clientes
from django.views import View
from django.views.decorators.csrf import csrf_exempt


from webapp.models import Contacto

class ClientesVistas(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            clientes = list(Clientes.objects.filter(id=id).values())
            if (len(clientes)>0):
                cliente = clientes[0]
                mensaje = {'message':'Success', 'cliente': cliente}
            else:
                mensaje = {'message': 'No encontrado'}
        else:
            clientes = list(Clientes.objects.values())
            if (len(clientes) > 0):
                mensaje = {'message': 'Success', 'clientes': clientes}
            else:
                mensaje = {'message': 'No hay clientes que mostras'}
        return JsonResponse(mensaje)

    def post(self, request):
        #json recibido (jr)
        jr = json.loads(request.body)
        Clientes.objects.create(nombre_Cliente=jr['nombre_Cliente'], direccion_Cliente=jr['direccion_Cliente'], telefono_Cliente=jr['telefono_Cliente'], email_Cliente=jr['email_Cliente'])
        mensaje = {'message': 'Success'}
        return JsonResponse(mensaje)

    def put(self, request, id):
        jr = json.loads(request.body)
        clientes = list(Clientes.objects.filter(id=id).values())
        if (len(clientes) > 0):
            cliente = Clientes.objects.get(id=id)
            cliente.nombre_Cliente= jr['nombre_Cliente']
            cliente.email_Cliente= jr['email_Cliente']
            cliente.telefono_Cliente=jr['telefono_Cliente']
            cliente.direccion_Cliente=jr['direccion_Cliente']
            cliente.save()
            mensaje = {'message': 'Success'}
        else:
            mensaje = {'message': 'No encontrado'}
        return JsonResponse(mensaje)

    def delete(self, request, id):
        clientes = list(Clientes.objects.filter(id=id).values())
        if (len(clientes) > 0):
            Clientes.objects.filter(id=id).delete()
            mensaje = {'message': 'Deleted Cliente: ' + str(id)}
        else:
            mensaje = {'message': "Error al eliminar Cliente: "  + str(id)}
        return JsonResponse(mensaje)

class CrearContacto(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        #json recibido (jr)
        jr = json.loads(request.body)
        #Contacto.objects.create(nombre_Cliente=jr['nombre_Cliente'], direccion_Cliente=jr['direccion_Cliente'], telefono_Cliente=jr['telefono_Cliente'], email_Cliente=jr['email_Cliente'])

        if jr['nombre_Contacto'] == '' or jr['email_Contacto']=='' or jr['mensaje_Contacto']=='':
            mensaje = {"message": 'Error, datos vacios'}
        else:
            Contacto.objects.create(nombre_Contacto=jr['nombre_Contacto'], telefono_Contacto=jr['telefono_Contacto'],email_Contacto=jr['email_Contacto'], mensaje_Contacto=jr['mensaje_Contacto'])
            mensaje = {'message': 'Success'}
        return JsonResponse(mensaje)

    def get(self, request, id=0):
        if (id>0):
            contactos = list(Contacto.objects.filter(id=id).values())
            if (len(contactos)>0):
                contacto = contactos[0]
                mensaje = {'message':'Success', 'cliente': contacto}
            else:
                mensaje = {'message': 'No encontrado'}
        else:
            contactos = list(Contacto.objects.values())
            if (len(contactos) > 0):
                mensaje = {'message': 'Success', 'clientes': contactos}
            else:
                mensaje = {'message': 'No hay contactos que mostras'}
        return JsonResponse(mensaje)


class BusquedaClienteAPI(View):
    def get(self, request, busqueda, id):
        termino = busqueda
        #tipo 1, solo responde JSON, tipo 2 responde con EXCEL
        if (id==1):
            clientes = list(Clientes.objects.filter(nombre_Cliente__icontains=termino).values())
            if (len(clientes)>0):
                mensaje = {'menssage': 'Sucess', 'clientes': clientes}
            else:
                mensaje = {'message': 'Success', 'clientes': 'no hay'}
            return JsonResponse(mensaje)
        elif (id==2):
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename=ReporteBusquedas' + str(
                datetime.datetime.now()) + ".xls"
            rows = Clientes.objects.filter(nombre_Cliente__icontains=termino).values_list("nombre_Cliente",
                                                                                          "direccion_Cliente",
                                                                                          "email_Cliente",
                                                                                          "telefono_Cliente")
            if (len(rows)>0):
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet('Resultados Busqueda')
                row_num = 0
                columnas = ['nombre', 'direccion', 'email', 'telefono']
                font_style = xlwt.XFStyle()
                font_style.font.bold = True

                for col_num in range(len(columnas)):
                    ws.write(row_num, col_num, columnas[col_num], font_style)
                font_style = xlwt.XFStyle()

                for row in rows:
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
                row_num = 0
                wb.save(response)
                return response
            else:
                return HttpResponseBadRequest('This view can not handle method {0}'. \
                                              format(request.method), status=405)
        return HttpResponseBadRequest('This view can not handle method {0}'. \
                                      format(request.method), status=405)




def exportarExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ReporteGeneral' + str(datetime.datetime.now()) + ".xls"
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Clientes')
    ws1 = wb.add_sheet("Contacto")
    row_num = 0
    columnas = ['nombre', 'direccion', 'email', 'telefono']
    columnasC = ['nombre', 'email', 'telefono', 'mensaje']
    font_style = xlwt.XFStyle()
    font_style.font.bold=True

    for col_num in range(len(columnas)):
        ws.write(row_num, col_num, columnas[col_num], font_style)
        ws1.write(row_num, col_num, columnasC[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Clientes.objects.all().values_list("nombre_Cliente", "direccion_Cliente", "email_Cliente",  "telefono_Cliente")
    rows1 = Contacto.objects.all().values_list("nombre_Contacto", "email_Contacto", "telefono_Contacto", "mensaje_Contacto")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    row_num=0
    for row in rows1:
        row_num += 1
        for col_num in range(len(row)):
            ws1.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


