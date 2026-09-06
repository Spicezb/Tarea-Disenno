# Bitácora de la práctica

Estudiante: Xavier Céspedes Alvarado
Carné: 2025102887

> Cómo se llena cada entrada, en este orden y sin saltarse pasos:
>
> 1. **Predicción** — escríbala ANTES de correr nada. Qué cree que va a
>    pasar y por qué. Equivocarse aquí y entender después vale más que
>    acertar; no vuelva a corregirla.
> 2. **Observación** — corra el experimento de la etapa y pegue la salida.
> 3. **Explicación** — por qué pasó lo que pasó, en sus palabras, citando
>    **su** archivo y **su** línea (`servicio.py:24`).
> 4. **Sello** — corra `python herramientas/marcador.py` al cerrar la
>    etapa y pegue el sello que imprime.

## Etapa 0 — Diagnóstico

**Predicción:**

Mi predicción es que en el archivo de legado.py se van a ver violentados los 11 principios, porque el objetivo principal de esta tarea está enfocado en identificar esas violaciones de los principios y aprender a cómo se deben implementar estos de manera correcta dentro del diseño.

**Observación:**

```
Se observa gran cantidad de violaciones a los principios, en efecto los 11 se encuentran violentados, algunos inclusive en múltiples partes del código.
```

**Explicación:**

Se encontraron errores graves en las funciones del archivo (legado.py:66,69,169,150,151) que incumplen con los 11 principios de diseño ideales, estos errores de diseño son perjudiciales para la escabilidad y mantenimiento del software. Las violaciones a los principios fueron detalladas en el archivo de diagnóstico.

**Sello:**

c83bab6960a5d8f6

## Etapa 1 — Dividir y conquistar, cohesión

**Predicción:**

Por lo observado, ServicioRecetas tiene 6 funcionalidades distintas, yo considero que se podrían requerir al menos 5 archivos más.

**Observación:**

```
ServicioCitas incluye las responsabilidades de validar, escribir en la base de datos, comunicarse, calcular con las reglas de negocio, exportar datos y generar las recetas, para un total de 6 responsabilidades.
```

**Explicación:**

El principio de divide y venceras es violado en la función de emitir (legado.py:57), puesto que realiza varias responsabilidades internas que podrían ser separadas en módulos propios.

El principio de alta cohesión se ve violentado en la clase ServicioRecetas (legado.py:44), pues esta clase se encarga de todo lo que hace el sistema.

Estos problemas fueron resueltos con la separación modular del programa, esto se ve evidenciado en el archivo modelos.py y errores.py dentro de la carpeta de dominio. 

Comparando con la predicción, esta fue de 5 archivos, y en realidad de momento fueron tres, no son números tan lejanos e igual es probable que se ocupen más archivos en las siguientes etapas.

**Sello:**

b2e524911780ffb5

## Etapa 2 — Reducir el acoplamiento

**Predicción:**

Mi predicción es que al cambiar los días de vigencia va a cambiar el comportamiento en alrededor de 2 partes del archivo, esto sería en el cálculo de la fecha de vencimiento y la emisión de la receta.

**Observación:**

```
>>> from clinicasegura.legado import CONFIG
>>> CONFIG["vigencia_dias"] = 1            
>>> print(CONFIG["vigencia_dias"])         
1
```

**Explicación:**

En realidad el cambio solamente cambia el comportamiento en el cálculo de la fecha de vencimiento de la receta. (legado.py:66)

Implementé la regla de negocio en el archivo reglas.py dentro del dominio, en la carpeta de configuración creé la clase de Configuracion para poder ser utilizada como argumento en lugar de variable global que significaba un acoplamiento común(configuracion.py:4), ahora la función de emitir (servicio.py:11) ya no recibe un diccionario como parámetro, sino que recibe una Receta.

**Sello:**

6735d185db9aec2f

## Etapa 3 — Abstracción y reuso

**Predicción:**

Al correr el experimento se encuentran dos coincidencias, mi predicción es que este dato va a bajar a 0.

**Observación:**

```
clinicasegura\legado.py:150:            paciente["data"]["attributes"]["full_name"],
clinicasegura\legado.py:151:            paciente["data"]["attributes"]["risk_lvl"],
```

**Explicación:**

Originalmente en (legado.py:150,151) se violenta el principio de abstracción, pues la función de reporte debe conocer la estructura en la que se guardan los datos del paciente, en emitir (legado.py:57) se debe conocer la información explícita de cada cadena, esto hace que emitir no sea reutilizable para otras cadenas, y en (legado.py:154) se valida la cédula a mano en lugar de utilizar la librería re.

Esto se solucionó aplicando los principios 4, 5 y 6, en este caso se crearon puertos que permiten una mejor abstracción (puestos.py), se crea un código más reutilizable al devolver un despacho a la hora de emitir(servivio.py:17) y se utiliza lo que ya existe con la librería de re en (borde.py:4) para validar la cédula.

Al volver a correr el grep solo se muestran los errores que habían en el legado, lo que quiere decir que fueron solucionados con las nuevas mejoras de diseño.

**Sello:**

1fd8bc21d40b43b0

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**

Mi predicción en esta etapa es que al agregar la nueva cadena el legado va a fallar puesto que utiliza ifs para construir la respuesta de cada cadena, en cambio, después de realizar las modificaciones de la etapa, este fallo no sucedería.

**Observación:**

```
No se puede correr directamente el código de legado en windows porque usa rutas imcompatibles con el entorno (legado.py:50), pero siguiendo el código de emitir, fallaría, pues utiliza condicionales que comparan explícitamente con los nombre de las farmacias.
```

**Explicación:**

Al final del test se pasan todas las pruebas, por lo que ahora se pueden agregar cadenas sin problema y sin tener que modificar el código del servicio.

Antes en la función de emitir se utilizaban los datos directos de las farmacias (legado.py:79), ahora hay flexibilidad porque se pueden agregar nuevas cadenas fácilmente y el servicio no depende de cadenas específicas como lo hacía anteriormente.

Antes se utilizaban dependencias pero no se sabía nada en específico sobre estas, ni ningún plan en caso de que fallaran, ahora en el archivo (DEPENDENCIAS.md) se encuentran detalladas para procurar un mejor mantenimiento del código en caso de que alguna falle.

Anteriormente las rutas que utilizaba el sistema se encontraban directamente en el servicio, lo que imposibilitaba la portabilidad (legado.py:169,50), ahora el servicio ya no depende de estas, sino que funciona de manera general y no está ligado a un solo ambiente.

**Sello:**

025f11d9d2a2ea7b

## Etapa 5 — Testabilidad

**Predicción:**

Mi predicción es que en el legado no se van a poder realizar correctamente las pruebas, ya que depende de varias cosas reales como el reloj del sistema, la base de datos, la red, etc. Esto hace que el software no se pueda probar adecuadamente.

**Observación:**

```
>>> from clinicasegura.legado import ServicioRecetas
>>> servicio = ServicioRecetas()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Xavier\OneDrive\Desktop\TEC\IIS2026\Diseño\Tarea-Disenno\practica-principios-diseno\clinicasegura\legado.py", line 50, in __init__
    self.db = sqlite3.connect(os.path.join("/tmp", "clinicasegura.db"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: unable to open database file

La prueba falla porque el servicio depende internamente de la base de datos.

En el código además se puede observar como el servicio depende de la base de datos, la aleatoriedad, el reloj real, la red y de variables globales.
```

**Explicación:**

Antes en la función de emitir (legado.py:66,69,) se dependía de cosas reales como el reloj, la base de datos, la aleatoriedad y demás, esto hacía difícil aplicar pruebas, en el nuevo diseño las pruebas sobre el servicio se pueden aplicar fácilmente con casos específicos que no dependen de las condiciones de la red o el reloj en tiempo real (servicio.py:14,20).

**Sello:**

c87808d0689c12e8

## Etapa 6 — Diseño defensivo

**Predicción:**

Mi predicción es que en la segunda ejecución con -O no se van a validar los asserts, por lo que los errores van a persistir.

**Observación:**

```
>>> from clinicasegura.legado import ServicioRecetas
>>> 
>>> servicio = ServicioRecetas()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Xavier\OneDrive\Desktop\TEC\IIS2026\Diseño\Tarea-Disenno\practica-principios-diseno\clinicasegura\legado.py", line 50, in __init__
    self.db = sqlite3.connect(os.path.join("/tmp", "clinicasegura.db"))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: unable to open database file
>>> 
>>> datos = {
...     "cedula": "1-1234-5678",
...     "dias": 0,
...     "dosis_mg": 500,
... }
>>> 
>>> servicio.emitir(datos, "farmauno")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'servicio' is not defined

Me vuelve a salir lo mismo porque (legado.py:50) no me permite abrir la base de datos.

Lo que pasaría es que al usar -O no se aplican los asserts y se mantienen los errores.
```

**Explicación:**

Antes el servicio hacía validaciones internas que mezclaban dos partes que en realidad no deberían mezclarse (legado.py:62), ahora las validaciones se hacen en la capa de borde (borde.py:11,30).

Anteriormente los errores podían viajar directamente, eso se soluciona ahora con errores propios del dominio(servicio.py:31)

**Sello:**

faf0f43390bb0fc4

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

Principios 3 y 11: Se buscaba que el sistema no dependiera directamente de los datos externos, pero también había que validarlos antes de usarlos. Se resolvió poniendo la validación en (borde.py) y convirtiendo los datos válidos en una Receta.

**Conflicto 2:**

Principios 7 y 11: Es necesario poder agregar nuevas farmacias sin cambiar el servicio, pero también es necesario manejar los errores de las farmacias correctamente. Se resolvió usando las pasarelas y haciendo que los errores de conexión se conviertan en FarmaciaNoDisponible y se registren en la bitácora, esto se puede ver en el archivo (servicio.py).