from fastapi import FastAPI

app = FastAPI()

menu = []

@app.get("/menu")
async def get_menu():
    return menu

@app.post("/menu")
async def add_dish(name: str, price: float):
    dish = {"id": len(menu), "name": name, "price": price}
    menu.append(dish)
    return dish

@app.post("/order")
async def order_food(dishes: list):
    order_price = 0
    ordered_dishes = []

    for dish_id in dishes:
        dish = menu[dish_id]
        order_price += dish["price"]
        ordered_dishes.append(dish)

    return {"Zamówienie": ordered_dishes, "Suma zamówienia": order_price}
