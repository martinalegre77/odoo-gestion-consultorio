# -*- coding: utf-8 -*-
# psychology_clinic/__manifest__.py

{
    'name': "Consultorio de Psicología",
    'version': '1.0',
    'summary': "Gestión clínica y administrativa para psicólogos",
    'description': """
        Módulo para Odoo 17 Community que integra pacientes, sesiones, informes y cobros.
    """,
    'author': "Martín Alegre",
    'website': "https://martinalegre77.github.io/",
    'category': 'Healthcare',
    'depends': [
        'base', 
        'contacts',   
        'account',    
        'calendar',   
        'mail',
        'web',

    ],
    'data': [
        # Seguridad primero
        'security/psychology_security.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',

        # Datos iniciales
        'data/patient_sequence.xml',
        'data/paperformat.xml',
        'data/cron.xml',

        # Reportes/ Informes
        'report/report_template.xml',
        #'report/assets_template.xml',
        'report/clinical_history_template.xml',
        'report/mail_template.xml',

        # Vistas
        'views/patient_views.xml',
        'views/session_views.xml',
        'views/session_payment_confirm_wizard_views.xml',
        'views/res_partner_views.xml',
        'views/report_views.xml',
        'views/clinical_history_views.xml',
        'views/clinical_history_event_views.xml',
        'views/pivot_views.xml',
        'views/search_views.xml',
        
        # Actions
        'views/actions_patient.xml',
        'views/actions_session.xml',
        'views/actions_session_payment_confirm.xml',
        'views/actions_report.xml',
        'views/actions_calendar.xml',
        'views/actions_clinical_history.xml',
        'views/actions_session_pivot.xml', 

        # Menús
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'psychology_clinic/static/src/css/styles.css',
            'psychology_clinic/static/src/js/calendar_default_check.js',
            ],
    },
    'installable': True,
    'application': True,   
    'auto_install': False,
    'license': 'LGPL-3',
}