{
    'name': 'JILINSIGHTS CUSTOM INVOICE MODULE',
    'summary': 'A module to revamp the look and feel of the JilInsights Invoice',
    'author': 'JilInsights (U) LTD',
    'web': 'jilinsights.net',
    'category': 'Documentation',
    'version': '1.0',
    'depends': ['base','sale','account_accountant'],
    'data': ['reports/custom_header.xml',
              'reports/jil_custom_invoice.xml',
              'reports/jil_custom_quote.xml','views/tax_invoice.xml'],
    'application': True,
}