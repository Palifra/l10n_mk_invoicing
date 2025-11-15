# Macedonian Translations for Odoo 18 Invoicing Module
# Македонски преводи за Odoo 18 Invoicing модул

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-875A7B.svg)](https://www.odoo.com/)
[![Language](https://img.shields.io/badge/Language-Macedonian-red.svg)](https://en.wikipedia.org/wiki/Macedonian_language)

## 📋 Overview / Преглед

This module provides **Macedonian (mk_MK)** translations for the Odoo 18 Invoicing/Accounting module.

Овој модул обезбедува **македонски (mk_MK)** преводи за Odoo 18 Invoicing/Accounting модулот.

## 📊 Translation Statistics / Статистика на преводот

- **Total entries:** 3,312
- **Translated:** 2,837 (85.7%)
- **Quality:** 100% (all placeholders and HTML preserved)
- **Characters:** 315,000+

### Coverage / Покриеност

- ✅ Invoice / Фактура
- ✅ Payment / Плаќање
- ✅ Account / Конто
- ✅ Journal / Дневник
- ✅ Tax / Данок
- ✅ Report / Извештај
- ✅ Partner / Партнер
- ✅ Currency / Валута
- ✅ Credit Note / Кредитно одобрение
- ✅ Reconciliation / Порамнување

## 🚀 Installation / Инсталација

### Method 1: Manual Installation

1. Download this module:
```bash
cd /path/to/odoo/addons
git clone https://github.com/Palifra/l10n_mk_invoicing.git
```

2. Restart Odoo:
```bash
sudo systemctl restart odoo
# or
docker-compose restart odoo
```

3. Install the module:
   - Go to **Apps**
   - Remove the **Apps** filter
   - Search for **"North Macedonia - Invoicing"**
   - Click **Install**

4. Activate Macedonian language:
   - Go to **Settings → Users → Preferences**
   - Select **Language → Macedonian / македонски јазик**
   - Click **Save**
   - Refresh the page (F5)

### Method 2: Docker

Add to your `docker-compose.yml`:
```yaml
volumes:
  - ./l10n_mk_invoicing:/mnt/extra-addons/l10n_mk_invoicing
```

## 📦 Dependencies / Зависности

- `account` (Odoo Invoicing/Accounting module)

## 🔧 Technical Details / Технички детали

### Module Structure / Структура на модулот

```
l10n_mk_invoicing/
├── __init__.py
├── __manifest__.py
├── i18n/
│   └── mk_MK.po          # 2,837 translated terms
└── README.md
```

### Translation Quality / Квалитет на преводот

- ✅ **0 placeholder errors** - All `%(variable)s` placeholders preserved
- ✅ **0 HTML errors** - All HTML tags and attributes preserved
- ✅ **100% accuracy** - Verified with automated quality scanner

### Key Terminology / Клучна терминологија

| English | Македонски |
|---------|-----------|
| Invoice | Фактура |
| Credit Note | Кредитно одобрение |
| Debit Note | Дебитно одобрение |
| Payment | Плаќање |
| Customer | Купувач |
| Vendor | Добавувач |
| Account | Конто |
| Journal | Дневник |
| Tax | Данок |
| Report | Извештај |
| Reconcile | Порамнување |
| Currency | Валута |

## 🌍 About Macedonian Language / За македонскиот јазик

Macedonian (македонски јазик) is a South Slavic language spoken primarily in North Macedonia. This translation follows official terminology used in business and accounting contexts.

Македонскиот јазик е јужнословенски јазик што се зборува главно во Северна Македонија. Овој превод ја следи официјалната терминологија што се користи во деловен и сметководствен контекст.

## 🤝 Contributing / Придонес

Contributions are welcome! If you find translation errors or have suggestions:

1. Open an issue on GitHub
2. Submit a pull request
3. Contact: info@eskon.mk

## 📄 License / Лиценца

This module is licensed under **LGPL-3.0** - same as Odoo.

## 👥 Credits / Заслуги

**Author / Автор:** ЕСКОН-ИНЖЕНЕРИНГ ДООЕЛ Струмица

**Translation Method / Метод на превод:**
- DeepL API (Beta Macedonian language)
- Manual quality control and corrections
- Automated placeholder/HTML preservation

**Tools Used / Користени алатки:**
- DeepL API for translation
- polib for PO file manipulation
- Custom quality scanner for validation

## 📧 Contact / Контакт

- **Organization:** ЕСКОН-ИНЖЕНЕРИНГ ДООЕЛ Струмица
- **Email:** info@eskon.mk
- **Website:** https://eskon.mk
- **GitHub:** https://github.com/Palifra

## 🔗 Related Modules / Поврзани модули

- [l10n_mk_inventory](https://github.com/Palifra/l10n_mk_inventory) - Inventory/Stock translations
- [l10n_mk](https://github.com/OCA/l10n-macedonia) - Chart of Accounts for North Macedonia

---

**Supported Odoo Version:** 18.0
**Language:** Macedonian (mk_MK)
**Last Updated:** 2025-11-15

**Среќно со македонскиот Odoo! 🇲🇰**
