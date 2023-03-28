# 1) Store
# 2) Into store you might :
#    a) Category ( [] )
#    b) Show All products
#    c) Admin mode
#    q) Quit
# if a) -> a) TV , b) Smartphone , c) Mp3 , d) DvD
#       a -> show all TV []
#       b -> show all Sm []
#       c -> show all Mp3 []
# products are dictionaries :
# { "label" : "..." , "price" : "..." , desc : ""... }
# 3) User might buy product if user has money (
#                   {
#                   "name" : "..." ,
#                   "money" : ... ,
#                   "bag" : []
#                   }
# )
# 4) Admin mode yields ->
#   1) add product to category ,
#   2) Delete product
#   3) Change name of product

from Category.tv import tv
from Category.smartphone import smartphone
from Category.mp3 import mp3
from Category.dvd import dvd
from print_products import print_products

products = {
    "TV": tv,
    "Smartphone": smartphone,
    "MP3": mp3,
    "DVD": dvd
}

while True:
    user_pick = int(input(
        f"""
1) Show products
2) Show Category
3) Admin mode
4) Quit
    Make your choice: """
    ))
    if user_pick == 1:
        print_products(products)
    elif user_pick == 3:
        while True:
            admin_pick = int(input(
                f"""
1) Add product
2) Delete product
3) Change name of product
4) Quit
    Make your choice: """
            ))
            if admin_pick == 1:
                print("----Add product")
            elif admin_pick == 2:
                print("----Del prod")
            elif admin_pick == 3:
                print("----Change name")
            elif admin_pick == 4:
                exit()
    elif user_pick == 4:
        exit()
