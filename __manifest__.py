# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'North Macedonia - Invoicing Translations',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations',
    'description': """
Macedonian Translations for Invoicing/Accounting Module
========================================================

This module provides complete Macedonian (mk_MK) translations for:
- Invoicing module (Customer Invoices, Vendor Bills)
- Accounting module (Journal Entries, Payments, Reconciliation)
- Financial Reports
- All accounting-related terminology

Македонски преводи за модулот Фактурирање/Сметководство
=======================================================

Овој модул обезбедува комплетни македонски (mk_MK) преводи за:
- Модул за фактурирање (Излезни фактури, Влезни фактури)
- Модул за сметководство (Книжења, Плаќања, Затворање)
- Финансиски извештаи
- Сета сметководствена терминологија
    """,
    'author': 'ЕСКОН-ИНЖЕНЕРИНГ ДООЕЛ Струмица',
    'website': 'https://github.com/eskon/odoo',
    'maintainer': 'ЕСКОН-ИНЖЕНЕРИНГ Development Team',
    'depends': [
        'account',  # Invoicing/Accounting module
        'l10n_mk',  # Macedonian Chart of Accounts
    ],
    'data': [],
    'demo': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
