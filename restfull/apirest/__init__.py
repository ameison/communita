# -*- coding: utf-8 -*-
import logging
import json
 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from persistence.models import * 
from util import JSONResponse 
from util import *

import json
logger = logging.getLogger(__name__)

 
@api_view(['GET'])
def lista_items_donaciones(request):
    try: 
        lista_items = Item.objects.all()
        data = []

        logger.info(" *** lista_items_donaciones *** ")
        for it in lista_items:
			data.append({
				"id": it.id,
				"nombre": it.nombre
				})        	

        return JSONResponse({"data":data})
    except Exception as e:
        logger.info("exc : "+str(e))
        return JSONResponse(None)


@api_view(['GET'])
def lista_lugares(request):
    try: 
        lista_lugares = Lugar.objects.all()

        data = []

        logger.info(" *** lista_lugares *** ")
        for lu in lista_lugares:
            data.append({
                "id": lu.id,
                "nombre": lu.nombre,
                "direccion": lu.direccion
                })          

        return JSONResponse({"data": data})
    except Exception as e:
        logger.info("exc : "+str(e))
        return JSONResponse(None)


@api_view(['POST'])
def registrar_donacion(request):
    try: 

        direccion = request.data.get('direccion')
        geo_ubicacion = request.data.get('geo_ubicacion')
        usuario_id = 1
        lugar_id = 1

        items = request.data.get('detalle_donativo')

        logger.info("direccion " + str(direccion))
        logger.info("geo_ubicacion " + str(geo_ubicacion))
        logger.info("detalle_donativo " + str(items))

        donativo = Donativo.objects.create(
            direccion=direccion, 
            geo_ubicacion=geo_ubicacion, 
            usuario_id=usuario_id, 
            lugar_id=lugar_id)

        for item in items.split('-'):
            datos = item.split(',')

            item_id = datos[0]
            cantidad = datos[1]

            dd = DonativoDetalle()
            dd.item_id = item_id
            dd.cantidad = cantidad
            dd.donativo_id = donativo.id
            dd.save()

        logger.info("Se guardo")
        return JSONResponse({"result": True})

        return JSONResponse(data)
    except Exception as e:
        logger.info("exc : "+str(e))
        return JSONResponse({"result": False})