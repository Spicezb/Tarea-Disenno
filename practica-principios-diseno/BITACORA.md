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

Se encontraron errores graves en las funciones del archivo legado.py que incumplen con los 11 principios de diseño ideales, estos errores de diseño son perjudiciales para la escabilidad y mantenimiento del software. Las violaciones a los principios fueron detalladas en el archivo de diagnóstico.

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

**Sello:**

b2e524911780ffb5

## Etapa 2 — Reducir el acoplamiento

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 3 — Abstracción y reuso

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 5 — Testabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 6 — Diseño defensivo

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

**Conflicto 2:**
