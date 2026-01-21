Psychology Clinic
=================

Módulo personalizado para Odoo 17 Community orientado a la gestión clínica y administrativa de consultorios de psicología.

El sistema permite centralizar pacientes, sesiones, historias clínicas, agenda profesional e informes clínicos, integrándose de forma nativa con los módulos base de Odoo y respetando criterios de seguridad, trazabilidad y confidencialidad de la información.

Características principales
----------------------------

- Gestión de pacientes
- Historia clínica centralizada
- Registro de sesiones clínicas
- Integración con agenda (calendar.event)
- Generación de informes clínicos 
- Control de accesos por roles
- Preparado para integración fiscal (ARCA – Argentina)

Estructura del módulo
---------------------

- ``models``: Modelos ORM y lógica de negocio
- ``views``: Vistas XML (Form, Tree, Kanban)
- ``wizards``: Asistentes y flujos guiados
- ``report``: Reportes QWeb (PDF)
- ``security``: Reglas de acceso y permisos
- ``data``: Datos iniciales y configuraciones base
- ``static``: Recursos visuales y UI

Dependencias
------------

- Odoo 17 Community
- Módulos base de Odoo:
  - base
  - contacts
  - calendar
  - mail
  - account    

Instalación
-----------

1. Copiar el módulo en el directorio ``addons`` de Odoo
2. Actualizar la lista de aplicaciones
3. Instalar el módulo desde Apps

Notas
-----

Este repositorio contiene una versión **demostrativa** del módulo.
Parte de la lógica funcional y de integración fiscal fue omitida intencionalmente por tratarse de un **producto comercial en uso real**.
