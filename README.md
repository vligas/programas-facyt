# Programas FACYT
----------------------------
### Informacion General:
#### Modelos:

* Usuario (persona que administra):
  Sera el **por defecto** de Django, con el extra de que habra grupo de usuario con diferentes permisologias
  
* Solicitud:
  Cuando un estudiante lleva sus documentos y pide los programas se genera una solicitud, dicha solicitud tendra la siguiente informacion:
  * Nombre
  * Cedula
  * Telefono
  * Solvencia (si debe algo como el tomo de la tesis por ejemplo)
  * Archivo adjunto (reporte de notas suministrado por el estudiante)
  * Usuario que creo la solicitud
  * Usuario que proceso la solicitud
  * Fecha de creacion de solicitud
  * Fecha de procesamiento de solicitud
  * Fecha de firma de solicitud
  * Envio correo de que se recibio (logico)
  * Envio correo de que ya se proceso (logico)
  * estatus actual de la solicitud (son opciones limitadas)

* Programas:
  Informacion programatica para una materia en un año en especifico contendra la siguiente informacion:
  * Codigo de materia
  * Año y periodo
  * Archivo (un archivo puede ser valido para muchos años)
 
##### Aclaraciones:
* Los usuarios en este caso son las personas que administran el sitio y estan dividios en 3 grupos:
  * Recibe - Entrega: encargado de recibir las solicitudes de los estudiantes y cargarlas en el sistema, posteriormente tambien pueden entregar los programas a los estudiantes una vez culminado el proceso.
  * Procesa: Procesa dichas solicitudes (tambien puede recibirlas)
  * Admin: Firma las solicitudes (tambien puede procesarlas y recibirlas) **El admin es el unico usuario que puede entrar al admin panel**

------------------------------------------

### Explicacion de el problema:
![Alt text](flujo.png?raw=true "Flujo")

------------------------------------------

# *! Pasos para configurar un ambiente de desarrollo correctamente !*
1. Instalar virtuelenv `pip install virtualenv`
2. Clonar el repositorio
3. Iniciar un entorno virtual dentro del repositorio (root ó raiz)
```
cd programas-facyt

virtualenv -p python venv // en mi caso es python3
```
4. Activar el virtualenv
```
source venv/bin/activate

// deberia aparecer algo como (venv) en el terminal
```
5. instalar requerimientos `pip install -r requirements.txt`
6. cada vez que se quiera instalar algo o correr el servidor activar el entorno virtual antes
