import json
import os
from time import sleep

# defining variables
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "goods.json"), encoding="UTF-8") as inf:
    goods = json.load(inf)

allowed = list(goods.keys())
start = 0


def choose_good(good_order: str) -> tuple:
    """
    to choose a good by giving its order.

    Args:
        good_order (str): the order of the good

    Returns:
        tuple[str, list[str, float]]: the order and the price of the good
    """
    try:
        li = goods[good_order]
        return li[0], round(li[1], 2)
    except KeyError:
        return "?", 0.0


while True:
    print("可供选择的商品如下: ")
    for key in goods:
        tup = choose_good(key)
        print(f"[{key}] {tup[0]}, {tup[1]}元.")

    order = input("\n请输入需要购买的商品编号: ")
    if order == "0":
        print(f"请支付总价 {start} 元.")
        break
    elif order in allowed:
        name, price = choose_good(order)
        start += price
        print(f"你选购的第{order}件商品是 '{name}', 价值 {price} 元.\n当前共需支付 {start} 元.")
    else:
        print("没有此商品!")

    sleep(1.5)
    os.system("cls")

input("Finished. Press 'Enter' to exit.")
