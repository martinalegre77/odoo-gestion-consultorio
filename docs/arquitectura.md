# 🧱 Arquitectura del Módulo – Psychology Clinic (Odoo)

## 📌 Visión General

El módulo **Psychology Clinic** fue diseñado como una extensión modular y escalable sobre **Odoo 17 Community**, orientado a la gestión clínica y administrativa de consultorios de psicología.

La arquitectura sigue los principios del framework Odoo:

* Dominio bien modelado
* Separación clara de responsabilidades
* Integración nativa con módulos base
* Seguridad y trazabilidad de datos sensibles

---

## 🧩 Arquitectura General

El módulo se estructura en capas claramente definidas, respetando el patrón arquitectónico de Odoo:

```text
┌─────────────────────────────┐
│ Interfaz (XML)              │
│ Form / Tree / Kanban        │
└──────────────▲──────────────┘
               │
┌──────────────┴──────────────┐
│ Lógica de Negocio           │
│ Models (ORM)                │
└──────────────▲──────────────┘
               │
┌──────────────┴──────────────┐
│ Persistencia                │
│ PostgreSQL (Odoo)           │
└─────────────────────────────┘
```

Esta separación permite mantener una arquitectura mantenible, extensible y alineada con las buenas prácticas del ecosistema Odoo.

---

## 🗂️ Estructura del Módulo

```text
psychology_clinic/
├── models/        # Lógica de negocio y entidades del dominio
├── views/         # Definición de vistas XML
├── wizards/       # Asistentes y flujos guiados
├── report/        # Reportes clínicos y administrativos (QWeb)
├── security/      # Control de accesos y permisos
├── data/          # Datos iniciales y configuraciones base
├── static/        # Recursos visuales y UI
└── __manifest__.py
```

---

## 🧠 Modelado del Dominio Clínico

### Entidades principales

* Paciente
* Historia Clínica
* Sesión / Evento Clínico
* Profesional
* Informes Clínicos
* Agenda y Actividades

### Criterios de diseño

El modelado prioriza:

* Trazabilidad temporal de la información clínica
* Relación clara entre sesiones e historia clínica
* Integración fluida con agenda y actividades de Odoo

---

## 🔗 Integraciones Clave

### 📅 Agenda

* Extensión del modelo `calendar.event`
* Asociación directa entre sesiones, pacientes y profesionales
* Gestión de recordatorios y actividades automáticas

### 👥 Contactos

* Integración con `res.partner`
* Unificación de datos administrativos y clínicos
* Evita duplicación de información

### 💰 Facturación (ARCA – Argentina)

* Integración con el sistema fiscal argentino (ARCA)
* Emisión de comprobantes vinculados a sesiones clínicas
* Preparado para cumplir normativas fiscales locales

> La implementación fiscal completa se mantiene fuera del repositorio público por razones comerciales.

---

## 🔐 Seguridad y Privacidad

La arquitectura contempla:

* Control de acceso basado en roles
* Separación entre información clínica y administrativa
* Protección de datos sensibles
* Registro de acciones relevantes para auditoría y trazabilidad

El diseño respeta principios éticos y legales aplicables a la práctica psicológica.

---

## 📈 Escalabilidad y Extensión

El módulo fue diseñado para permitir futuras ampliaciones, tales como:

* Estadísticas clínicas y administrativas
* Integración con obras sociales
* Reportes avanzados
* Soporte multi-profesional y multi-consultorio

---

## 🧭 Decisiones de Diseño

* Uso exclusivo del ORM nativo de Odoo
* Preferencia por herencia y extensión antes que duplicación
* Separación clara entre UI y lógica de negocio
* Código preparado para mantenimiento y evolución a largo plazo

---

## 📌 Nota

Este documento describe la arquitectura general del módulo.

Parte de la lógica específica fue omitida en el repositorio público por tratarse de un producto comercial en uso real.

---
