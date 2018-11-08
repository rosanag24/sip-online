# SIP
Este documento pretende dar una idea general del proyecto desde el punto de vista del programador.

## Base de datos

Cada entidad de la base de datos cuenta con diversos métodos para permitir su gestión.
Todas las clases tienen un método __str__ para definir su impresión.

| Entidades     | Atributos                           | Métodos                             |
| ------------- |:-----------------------------------:|-----------------------------------:|
| Departamento  | nombre,código,jefe | Tiene jefe, jefe_coherente, __str__ |
| Profesor      | nombre, apellido, cedula, disponibilidad,departamentos,email,asignaturas|   codigo_completo,__str__ |
| Asignatura    | nombre,código,departamento          | __str__                             |

