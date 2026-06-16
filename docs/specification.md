# Asistente Personal de Estudio con IA

## Objetivo

Crear una aplicación web para gestionar el estudio mediante PDFs, subrayados, anotaciones, calendario académico e inteligencia artificial.

La aplicación debe funcionar en PC y tablet y utilizar IA local mediante Ollama.

---

# Fase 1

## Funcionalidades

- Crear asignaturas.
- Crear temas.
- Subir PDFs.
- Visualizar PDFs.
- Subrayar texto.
- Guardar subrayados.
- Consultar todos los subrayados de un tema.

### Sistema de anotaciones

- Visualizar PDF original o PDF con anotaciones.
- Mantener las anotaciones separadas del documento original.
- Permitir subrayados, notas y escritura a mano mediante lápiz.
- Mostrar u ocultar anotaciones en cualquier momento.
- Exportar una versión limpia o una versión anotada del documento.

---

# Entidades

## Usuario

Campos:

- id
- nombre
- email
- Carrera

## Asignatura

Campos:

- id
- usuario_id
- nombre

Ejemplos:

- Programación
- Bases de Datos
- Matemáticas

## Tema

Campos:

- id
- asignatura_id
- nombre

Ejemplos:

- SQL
- Normalización
- Índices

## PDF

Campos:

- id
- tema_id
- nombre
- ruta_archivo
- fecha_subida

## Subrayado

Campos:

- id
- pdf_id
- pagina
- texto
- fecha

## Nota

Campos:

- id
- subrayado_id
- contenido

---

# Flujo de uso

1. Crear asignatura.
2. Crear tema.
3. Subir PDF.
4. Leer PDF.
5. Subrayar contenido importante.
6. Consultar subrayados posteriormente.

---

# Pantallas

## Inicio

Lista de asignaturas.

## Asignatura

Lista de temas.

## Tema

Lista de PDFs.

## Visor PDF

Visualización y subrayado.

## Subrayados

Listado de todo el contenido marcado por el usuario.

---

# Funciones futuras

## IA

- Chat sobre los apuntes.
- Generación de preguntas.
- Flashcards.
- Explicaciones.

## Calendario

- Clases.
- Exámenes.
- Entregas.

## Seguimiento

- Tiempo de estudio.
- Progreso por tema.
- Preparación para exámenes.

## Sincronización

- PC.
- Tablet.
- Móvil.
