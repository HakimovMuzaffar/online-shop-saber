CATEGORIES = {
    'Erkaklar uchun': 'category/47/',
    'bolalar uchun': 'category/49/',
    'aksessuarlar': 'category/96/',
}

def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v
