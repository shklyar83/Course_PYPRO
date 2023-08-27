import Supermarket.Products as modprod
import Supermarket.Cart as Cart

if __name__ == '__main__':
    pr1 = modprod.Product('apple', 50)
    pr2 = modprod.Product('apple lux', 1200)
    pr3 = modprod.Product('banana', 400)
    pr4 = modprod.Product('orange', 500)
    pr4 = modprod.Product('chocolate', 1000)

    cart = Cart.Cart()
    cart.add_product(pr1, 6)
    cart.add_product(pr4, 40)
    cart.add_product(pr3, 3)

    cart.process()
    print(cart)


