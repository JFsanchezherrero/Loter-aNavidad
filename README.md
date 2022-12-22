# Comprobador de Loteria Navidad
Este es un pequeño script de python que se conecta via API a la web del pais y revisa los números premiados para comprobar si tienes algún acierto en tu lista de números.


# Instalación

Para ejecutar el script hacen falta una serie de requisitos, paquetes de python incluidos en el fichero: `requirements.txt`

Para instalarlo, recomiendo utilizar un entorno pip.

Pasos:

```
## clone repo
git clone https://github.com/JFsanchezherrero/LoteriaNavidad.git

## create environment
python3 -m venv LotNavidad
source LotNavidad/bin/activate

# install requirements
pip install -r requirements.txt
```

## Ejecución

Para ejecutar, puedes ejecutarlo de varias formas
```
$ python check.py -h

usage: check.py [-h] [--input INPUT] [--batch] [--status]

Comrpueba los boletos de Loteria de Navidad

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input numeros. Formato= Numero:Participación-Identificación
  --batch, -b           Input es un fichero
  --status, -s          Comprueba estado del sorteo

```

Un único número, con la cantidad de euros jugados y un identificador, separado por ":" y "_" respectivamente.
```
python check.py -i 04074:20-test
```

Un conjunto de números incluidos en un fichero:
```
$ cat numeros_test.txt 
  04074:20-ejemplo
  12345:20-ejemplo2


$ python check.py -i numeros_test.txt --batch
```

También existe una forma de comprobar cada 5 minutos de forma automática los números con el fichero `checker.sh`
```
$ cat checker.sh 
  #!/bin/sh  
  while true  
  do  
    python check.py -b -i $1
    sleep 300  
  done
```

Por ejemplo:
```
$ sh checker.sh numeros_test.txt 
```

# Resultado
```
$ sh checker.sh numeros_test.txt 
**************************************************
Número: 04074
   Jugado: 20 euros
   Ganado: 125000.0 euros
   Ident: ejemplo

**************************************************
Número: 12345
   Jugado: 20 euros
   Ganado: 0.0 euros
   Ident: ejemplo2


=============================
Total Jugado =      40.00 euros
Total Ganado =  125000.00 euros
Saldo        =  124960.00 euros
```


# Copyright

Copyright (c) 2012-2019 Juan Francisco Cantero Hurtado <iam@juanfra.info>

Modified by Jose F. Sanchez Herrero in 2021-2022.

