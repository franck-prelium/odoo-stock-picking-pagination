# Odoo Stock Picking Pagination

Addon Odoo 19+ permettant de configurer le nombre de lignes affichées par page dans l'onglet **Opérations** des bons de livraison et transferts.

## Fonctionnement

Par défaut Odoo affiche 40 lignes par page. Ce module permet de modifier cette limite depuis les Réglages.

**Configuration :**
> Réglages → Inventaire → Affichage des transferts → Lignes par page

La valeur est appliquée dynamiquement à chaque ouverture d'un bon de livraison, sans redémarrage du serveur.

## Installation

1. Copier le dossier `stock_picking_pagination` dans votre répertoire d'addons
2. Mettre à jour la liste des apps (`-u base`)
3. Installer le module depuis **Apps**

## Compatibilité

- Odoo 19.0
- Dépendance : `stock`


