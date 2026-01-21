# 🔄 Flujos Funcionales – Psychology Clinic (Odoo)

## 📌 Introducción

Este documento describe los principales **flujos funcionales** del módulo **Psychology Clinic**, detallando cómo interactúan los distintos perfiles de usuario con el sistema en los procesos clínicos y administrativos.

Los flujos fueron diseñados para reflejar el funcionamiento real de un consultorio psicológico, garantizando:

* Coherencia clínica
* Trazabilidad de la información
* Control administrativo
* Respeto por la privacidad de los datos

---

## 👤 Flujo de Gestión de Pacientes

**Objetivo:** centralizar la información clínica y administrativa del paciente.

### Pasos principales

1. Alta de paciente desde **Contactos** o desde el módulo clínico
2. Registro de datos personales y administrativos
3. Asociación automática con su historia clínica
4. Disponibilidad inmediata para:

   * Agenda
   * Sesiones
   * Informes clínicos

📌 **El paciente actúa como entidad central del sistema**, vinculando todos los procesos clínicos y administrativos.

---

## 📅 Flujo de Agenda y Sesiones

**Objetivo:** gestionar la planificación y ejecución de sesiones terapéuticas.

### Pasos principales

1. Creación de evento en la agenda profesional
2. Asociación del evento a un paciente
3. Registro de la sesión clínica
4. Generación automática de:
   * Actividades
   * Recordatorios
5. Registro temporal de sesiones realizadas

### Integraciones involucradas

* Agenda de Odoo
* Sesiones clínicas
* Historia clínica

Este flujo garantiza una visión unificada entre planificación y atención clínica.

---

## 🧠 Flujo de Historia Clínica

**Objetivo:** consolidar la información clínica del paciente de forma estructurada y trazable.

### Pasos principales

1. Creación automática de la historia clínica al registrar un paciente
2. Registro de eventos clínicos relevantes
3. Asociación de:
   * Sesiones
   * Informes
   * Observaciones clínicas
4. Acceso restringido según rol profesional

📌 La historia clínica funciona como **repositorio central de la información clínica del paciente**.

---

## 📄 Flujo de Informes Clínicos

**Objetivo:** documentar la evolución clínica y generar respaldo profesional.

### Pasos principales

1. Creación del informe desde el módulo correspondiente
2. Redacción estructurada del contenido clínico
3. Almacenamiento seguro del informe
4. Posibilidad de generación de reporte en formato PDF

Los informes quedan vinculados al paciente y, cuando corresponde, a la sesión clínica asociada.

---

## 💰 Flujo Administrativo y Facturación

**Objetivo:** integrar la gestión clínica con el circuito administrativo y fiscal.

### Pasos principales

1. Registro de sesión facturable
2. Asociación con comprobante administrativo
3. Integración con el sistema fiscal argentino (ARCA)
4. Vinculación del registro administrativo con el paciente

⚠️ **Nota:**
Parte de la lógica fiscal completa se mantiene fuera del repositorio público por tratarse de un módulo comercial.

---

## 🔐 Flujo de Seguridad y Accesos

**Objetivo:** proteger la información clínica y garantizar el acceso correcto según rol.

### Características principales

* Asignación de roles:
  * Profesional
  * Administrativo
* Control de acceso a información clínica sensible
* Restricción de acciones críticas
* Protección de datos confidenciales

El sistema impide accesos no autorizados y respeta principios éticos y legales de la práctica psicológica.

---

## 📈 Flujo de Escalabilidad

El diseño funcional del módulo permite incorporar de forma progresiva:

* Nuevos tipos de sesiones
* Nuevos reportes clínicos y administrativos
* Escenarios multi-profesional y multi-consultorio

La arquitectura y los flujos fueron pensados para acompañar el crecimiento del consultorio.

---

## 📌 Nota Final

Este documento describe los **flujos funcionales principales** del módulo.

Algunos detalles fueron simplificados u omitidos en esta versión pública, ya que el sistema corresponde a un producto comercial en uso real.
