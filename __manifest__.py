# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Odoo/OpenERP Hospital Management",
    "version" : "10.0.0.1",
    "summary": "Hospital Management",
    "category": "Industries",
    "description": """
BrowseInfo developed a new odoo/OpenERP module apps.
This module is used to manage Hospital Mangement.
    Also use for manage the healthcare management, Clinic management, Medical Management.Doctor's Clinic. Clinic software, oehealth.
    
    Health Center Management
    Hospital Buildings Management
    Apothecary
    Domiciliary Units
    Patient - OutPatient Admissions
    Patient - InPatient Admissions
    Vaccines
    Call Logs
    Physicians & Appointments
    Physicians Management
    Appointments
    Prescriptions
    Evaluations
    Pediatrics
    Newborns
    Surgeries
    Insurances
    Laboratory
    Lab Tests
    Imaging
    Imaging Tests
    Configuration
    Physicians
    Specialties
    Degrees
    Laboratory
    Pathology
    Diseases
    Disease Categories
    Health & Products
    Medicines
""" ,
    "depends" : ["base", "sale", "stock", "account"],
    "data": [
            'security/hospital_groups.xml',
            'data/ir_sequence_data.xml',
            'views/assets.xml',
            'views/login_page.xml',
            'views/main_menu_file.xml',
            'wizard/medical_appointments_invoice_wizard.xml',
            'views/medical_appointment.xml',
            'wizard/appointment_start_end_wizard.xml',
            'wizard/create_prescription_invoice_wizard.xml',
            'wizard/create_prescription_shipment_wizard.xml',
            'wizard/medical_bed_transfer_wizard.xml',
            'wizard/medical_health_services_invoice_wizard.xml',
            'wizard/multiple_test_request_wizard.xml',
            'views/medical_ambulatory_care_procedure.xml',
            'views/medical_directions.xml',
            'views/medical_family_code.xml',
            'wizard/medical_lab_test_create_wizard.xml',
            'views/medical_speciality.xml',
            'views/medical_dose_unit.xml',
            'views/medical_medicament.xml',
            'views/medical_drug_form.xml',
            'views/medical_drug_route.xml',
            'views/medical_drugs_recreational.xml',
            'views/medical_ethnicity.xml',
            'views/medical_family_disease.xml',
            'views/medical_genetic_risk.xml',
            'views/medical_health_service_line.xml',
            'views/medical_health_service.xml',
            'views/medical_hospital_bed.xml',
            'views/medical_hospital_building.xml',
            'views/medical_hospital_oprating_room.xml',
            'views/medical_hospital_unit.xml',
            'views/medical_hospital_ward.xml',
            'views/medical_inpatient_registration.xml',
            'views/medical_inpatient_icu.xml',
            'views/medical_icu_apache2_.xml',
            'views/medical_icu_ecg.xml',
            'views/medical_icu_glasgow.xml',
            'views/medical_inpatient_medication.xml',
            'views/medical_insurance_plan.xml',
            'views/medical_insurance.xml',
            'wizard/medical_lab_test_invoice_wizard.xml',
            'views/medical_lab_test_units.xml',
            'views/medical_patient_lab_test.xml',
            'views/medical_lab.xml',
            'views/medical_neomatal_apgar.xml',
            'views/medical_newborn.xml',
            'views/medical_occupation.xml',
            'views/medical_operational_area.xml',
            'views/medical_operational_sector.xml',
            'views/medical_pathology_category.xml',
            'views/medical_pathology_group.xml',
            'views/medical_pathology.xml',
            'views/medical_patient_ambulatory_care.xml',
            'views/medical_patient_disease.xml',
            'views/medical_patient_evaluation.xml',
            'views/medical_patient_medication.xml',
            'views/medical_patient_medication1.xml',
            'views/medical_patient_pregnancy.xml',
            'views/medical_patient_prental_evolution.xml',
            'views/medical_patient_psc.xml',
            'views/medical_patient.xml',
            'views/medical_physician.xml',
            'views/medical_preinatal.xml',
            'views/medical_prescription_line.xml',
            'views/medical_prescription_order.xml',
            'views/medical_procedure.xml',
            'views/medical_puerperium_monitor.xml',
            'views/medical_rcri.xml',
            'views/medical_rounding_procedure.xml',
            'views/medical_surgey.xml',
            'views/medical_test_critearea.xml',
            'views/medical_test_type.xml',
            'views/medical_vaccination.xml',
            'views/medicament_category.xml',
            'views/res_partner.xml',
            'report/report_view.xml',
            'report/appointment_recipts_report_template.xml',
            'report/medical_view_report_document_lab.xml',
            'report/medical_view_report_lab_result_demo_report.xml',
            'report/newborn_card_report.xml',
            'report/patient_card_report.xml',
            'report/patient_diseases_document_report.xml',
            'report/patient_medications_document_report.xml',
            'report/patient_vaccinations_document_report.xml',
            'report/prescription_demo_report.xml',
            'security/ir.model.access.csv',
	     ],
    "author": "BrowseInfo",
    "website": "http://www.browseinfo.in",
    "price": 129,
    "currency": "EUR",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images":["static/description/Banner.png"],

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
