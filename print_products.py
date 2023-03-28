def print_products(products):
    user_category = input(
        f"What do you wanna pick from {products.keys()}? Enter category name: ")
    for category, list_of_products in products.items():
        if user_category == category:
            return print(f"""
    {user_category}: """, list_of_products)
        else:
            return print(f"""
    There are no {user_category} category!""")
