#!/usr/bin/env python3
"""
练习2: 购物车系统
练习字典、列表和类的使用
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - ¥{self.price:.2f}"


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ¥{self.subtotal:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity=1):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return True
        self.items.append(CartItem(product, quantity))
        return True
    
    def remove_item(self, product_id):
        for i, item in enumerate(self.items):
            if item.product.product_id == product_id:
                self.items.pop(i)
                return True
        return False
    
    def update_quantity(self, product_id, quantity):
        if quantity <= 0:
            return self.remove_item(product_id)
        
        for item in self.items:
            if item.product.product_id == product_id:
                item.quantity = quantity
                return True
        return False
    
    def get_total(self):
        return sum(item.subtotal for item in self.items)
    
    def clear(self):
        self.items.clear()
    
    def __str__(self):
        if not self.items:
            return "购物车是空的"
        
        result = ["=" * 40]
        for item in self.items:
            result.append(str(item))
        result.append("=" * 40)
        result.append(f"总计: ¥{self.get_total():.2f}")
        return "\n".join(result)


class Store:
    def __init__(self):
        self.products = {}
        self.carts = {}
    
    def add_product(self, product):
        self.products[product.product_id] = product
    
    def list_products(self):
        print("\n可用商品:")
        for p in self.products.values():
            print(f"  {p.product_id}: {p}")
    
    def get_cart(self, customer_id):
        if customer_id not in self.carts:
            self.carts[customer_id] = ShoppingCart()
        return self.carts[customer_id]


def main():
    store = Store()
    
    store.add_product(Product("P001", "iPhone 15", 6999))
    store.add_product(Product("P002", "MacBook Pro", 12999))
    store.add_product(Product("P003", "AirPods Pro", 1899))
    store.add_product(Product("P004", "iPad Air", 4599))
    
    store.list_products()
    
    cart = store.get_cart("customer001")
    
    cart.add_item(store.products["P001"])
    cart.add_item(store.products["P002"])
    cart.add_item(store.products["P003"], 2)
    
    print("\n购物车内容:")
    print(cart)
    
    cart.update_quantity("P003", 1)
    print("\n更新数量后:")
    print(cart)
    
    cart.remove_item("P002")
    print("\n删除MacBook后:")
    print(cart)


if __name__ == "__main__":
    main()
