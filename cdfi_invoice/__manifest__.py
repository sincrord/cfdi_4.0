# -*- coding: utf-8 -*-
##############################################################################
#                 @author IT Admin
#
##############################################################################

{
    'name': 'Ventas Factura Electronica Mexico CFDI',
    'version': '14.10',
    'description': ''' Factura Electronica módulo de ventas para Mexico (CFDI 4.0)
    ''',
    'category': 'Accounting',
    'author': 'IT Admin',
    'website': 'www.itadmin.com.mx',
    'depends': [
        'sale','account','purchase'
    ],
    'data': [
        'data/catalogo.unidad.medida.csv',
        'security/ir.model.access.csv',
        'wizard/import_account_payment_view.xml',
        'wizard/reason_cancelation_sat_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/product_view.xml',
        'views/account_invoice_view.xml',
        'views/account_payment_view.xml',
        'views/account_tax_view.xml',
        'views/sale_view.xml',
        'views/account_payment_term_view.xml',
        'views/purchase_view.xml',
        'views/account_journal_view.xml',
        'views/res_currency.xml',
        'report/invoice_report_custom.xml',
        'report/payment_report.xml',
        'data/mail_template_data.xml',
        'data/cron.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'application': False,
    'installable': True,
    'price': 0.00,
    'currency': 'USD',
    'license': 'OPL-1',
}
