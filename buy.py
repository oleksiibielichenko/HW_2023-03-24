def buy (customer , manager) :
    manager_bag = manager['bag']
    customer_money = customer['money']
    manager_money = manager['money']

    product = input(f"""
        if you want to buy something there pick a)
        Otherwise pick q) - to exit
        :
        """)

    if product != "a" : raise SystemError("Goodbye!")

    for i,item in enumerate(manager_bag) :
        print(i)
        print(item)

    user_choose = int(input("Enter the number of product that you wanna buy!"))

    users_product = manager_bag[user_choose]
    product_price = manager_bag[user_choose]['price']

    if customer_money >= product_price :
        customer['money'] -= product_price
        manager['money'] += product_price

        customer['bag'].append(users_product)
        manager['bag'].pop(user_choose)

        print(customer)
        print(manager)

