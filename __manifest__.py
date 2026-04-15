{
    'name': 'Stock Picking - Pagination configurable',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Configuration',
    'summary': 'Paramètre pour définir le nombre de lignes par page dans les bons de livraison.',
    'description': """
Stock Picking Pagination
========================

Ce module ajoute un paramètre dans les Réglages généraux pour contrôler
le nombre de lignes affichées par page dans l'onglet Opérations
des bons de livraison (et transferts en général).

Fonctionnement :
- Dans Configuration > Réglages > Inventaire, définissez la taille de page souhaitée
- La valeur est appliquée à la vue liste des mouvements de stock dans les transferts
- Valeur par défaut : 80 lignes
    """,
    'author': 'Prelium',
    'depends': ['stock'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
