# Catalog ids
catalog_id = ["doc-product_groups", "doc-option_groups", "doc-manufacturers", "doc-suppliers", "doc-delivery_statuses",
              "doc-sold_out_statuses", "doc-quantity_units", "doc-csv"]

# Customers ids
customers_id = ["doc-csv", "doc-newsletter"]

# Modules ids
modules_id = ["doc-customer", "doc-shipping", "doc-payment", "doc-order_total", "doc-order_success", "doc-order_action"]

# Reports ids
reports_id = ["doc-monthly_sales", "doc-most_sold_products", "doc-most_shopping_customers"]

# Settings ids
settings_id = ["doc-store_info", "doc-defaults", "doc-general", "doc-listings", "doc-images", "doc-checkout",
               "doc-advanced", "doc-security"]

# Translations ids
translations_id = ["doc-scan", "doc-csv"]

# Titles ids
titles = ['Appearence', 'Catalog', 'Countries', 'Currencies', 'Customers', 'Geo Zones', 'Languages', 'Modules',
          'Orders', 'Pages', 'Reports', 'Settings', 'Slides', 'Tax', 'Translations', 'Users', 'vQmods']

# Matching titles and id
titles_ids = {
    'Appearance': "doc-logotype",
    'Catalog': catalog_id,
    'Customers': customers_id,
    'Languages': "doc-storage_encoding",
    'Modules': modules_id,
    'Orders': "doc-order_statuses",
    'Reports': reports_id,
    'Settings': settings_id,
    'Tax': "doc-tax_rates",
    'Translations': translations_id,
}
