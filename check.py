#!/usr/bin/env python3

# Copyright (c) 2012-2019 Juan Francisco Cantero Hurtado <iam@juanfra.info>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import json
import urllib.request
import HCGB
import argparse

##########################################################
def estado_sorteo():
    url_elpais = "https://api.elpais.com/ws/LoteriaNavidadPremiados?s=1"
    respuesta = urllib.request.urlopen(url_elpais)
    contenido = respuesta.read()
    datos = json.loads(contenido.decode("utf8").replace("info=", ""))
    
    status = datos["status"]
    estado = None
    if status == 0:
        estado = "El sorteo no ha comenzado."
    elif status == 1:
        estado = "El sorteo ha empezado. Lista de premios parcial."
    elif status == 2:
        estado = "Sorteo terminado. Lista de premios provisional."
    elif status == 3:
        estado = "Sorteo terminado. Lista de premios semioficial."
    elif status == 4:
        estado = "Sorteo terminado. Lista de premios oficial."
    print("\n=====>", estado, "\n\n")


##########################################################
def consultar(n):
    url_elpais = "https://api.elpais.com/ws/LoteriaNavidadPremiados?n=" + n
    respuesta = urllib.request.urlopen(url_elpais)
    contenido = respuesta.read()
    datos = json.loads(contenido.decode("utf8").replace("busqueda=", ""))
    
    premio = float(datos["premio"])
    return premio

##########################################################
def sorteo(dictionary_numeros):
    
    total_ganado = 0.0
    total_jugado = 0.0
    for num in dictionary_numeros.keys():
        info_num = dictionary_numeros[num].split("-")
        jugado=info_num[0]
        ident = info_num[1]
        
        ganado_decimo = consultar(str(int(num)))
        he_ganado = max(float(jugado) * ganado_decimo / 20, 0)
        total_ganado += he_ganado
        total_jugado += float(jugado)
        HCGB.functions.aesthetics_functions.print_sepLine("*", 50, "yellow")
        print(
            "Número: " + num + "\n",
            "  Jugado: " + str(jugado) + " euros" + "\n",
            "  Ganado: " + str(he_ganado) + " euros" + "\n",
            "  Ident: " + ident + "\n",
        )
        
    print("\n=============================")
    print("Total Jugado = " + "{0:10.2f}".format(total_jugado), "euros")
    print("Total Ganado = " + "{0:10.2f}".format(total_ganado), "euros")
    print("Saldo        = " + "{0:10.2f}".format(total_ganado - total_jugado), "euros")

    print()
    print()

#########################################
def main():
    ## this code runs when call as a single script
    parser=argparse.ArgumentParser(description='''Comrpueba los boletos de Loteria de Navidad''');
    
    parser.add_argument('--input', '-i', help='Input numeros. Formato= Numero:Participación-Identificación')
    parser.add_argument('--batch', '-b', action="store_true", help='Input es un fichero')
    parser.add_argument('--status', '-s', action="store_true", help='Comprueba estado del sorteo')
    args=parser.parse_args();
    
    numeros={}
    
    if args.status:
        estado_sorteo()
    
    if args.batch:
        if args.input:
            numeros=HCGB.functions.main_functions.file2dictionary(args.input, ":")
    elif args.input:
        input_info=args.input.split(":")
        numeros[input_info[0]] = input_info[1] 
    
    if numeros:
        sorteo(numeros)
    
    return ()


######
if __name__== "__main__":
    main()
