import Restaurant.Menu 
import Restaurant.Order 
import Discount


if __name__ == '__main__':
    d1 = Restaurant.Menu.Dish('Oliv"e', 'Salad with potatoes, vegetables, eggs, and mayonnaise', 110)
    d2 = Restaurant.Menu.Dish('Dnestr', 'Traditional Moldovan pastry with cheese', 85)
    d3 = Restaurant.Menu.Dish('Grecheskiy', 'Greek salad with feta cheese, olives, and vegetables', 120)
    d4 = Restaurant.Menu.Dish('Steak', 'Grilled chicken meat steak', 200)
    d5 = Restaurant.Menu.Dish('Margherita', 'Classic Italian pizza with tomato, mozzarella, and basil', 300)
    d6 = Restaurant.Menu.Dish('Sushi', 'Assorted sushi rolls with fresh fish and vegetables', 500)
    d7 = Restaurant.Menu.Dish('Tiramisu', 'Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cheese', 150)
    d8 = Restaurant.Menu.Dish('Borsch', 'Traditional Ukrainian beetroot soup', 80)
    d9 = Restaurant.Menu.Dish('Pad Thai', 'Thai stir-fried rice noodles with tofu, shrimp, and peanuts', 145)
    d10 = Restaurant.Menu.Dish('Miso Soup', 'Japanese soup with soybean paste and tofu', 65)

    cat1 = Restaurant.Menu.Category('Salads')
    cat2 = Restaurant.Menu.Category('Soups')

    cat1.add_dish(d1)
    cat1.add_dish(d2)
    cat1.add_dish(d3)
    cat2.add_dish(d8)
    cat2.add_dish(d10)
    menu = Restaurant.Menu.Menu()
    menu.add_category(cat1)
    menu.add_category(cat2)

    order = Restaurant.Order.Order()
    order.add_dish(d1, 1)
    order.add_dish(d4, 2)
    order.add_dish(d8, 1)

    cat1.process()
    cat2.process()
    menu.process()
    order.process()

    for dish in cat1:
        print(dish)

    for dish in menu:
        print(dish)

    print(f'Total {order.total_price(Discount.GoldDiscount())}')

    print(len(cat1))

