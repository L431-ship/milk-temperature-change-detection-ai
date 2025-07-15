
def get_required_temperature(product, external_temp):
    # Placeholder logic for demo purposes
    product_temp_map = {
        'Milk': (1, 4),
        'Curd': (2, 6),
        'Ice-cream': (-18, -12),
        'Cheese': (1, 7),
        'Flavored Milk': (2, 8)
    }
    if product in product_temp_map:
        min_temp, max_temp = product_temp_map[product]
        return round((min_temp + max_temp) / 2, 1)
    return None
