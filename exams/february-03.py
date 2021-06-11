def stock_availability(l_boxes, action, *args):
    if action == "delivery":
        for box in args:
            l_boxes.append(box)
    elif action == "sell":
        if not args:
            l_boxes = l_boxes[1:]
            return l_boxes
        for box in args:
            if type(box) == int:
                return l_boxes[box:]
            while box in l_boxes:
                l_boxes.remove(box)
    return l_boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
