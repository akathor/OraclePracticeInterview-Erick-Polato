from Classes.Box import Box


def package_into_boxes(fruits, max_box_weight, package_fee):
    boxes = [Box(max_box_weight, package_fee)]
    current_box = 0
    for f in fruits:
        if boxes[current_box].get_box_weight() + f.get_weight() > boxes[current_box].get_box_max_weight():
            boxes[current_box].close_box()
            current_box += 1
            boxes.append(Box(max_box_weight, package_fee))
        boxes[current_box].insert_fruit(f)
    boxes[current_box].close_box()
    return boxes


def print_boxes(boxes):
    current_box = 1
    for b in boxes:
        print("BOX #{}".format(current_box))
        print('_____________________________')
        print('Box Weight: {}'.format(b.get_box_weight()))
        print('Box fruits price: {} €'.format(b.get_box_price_no_fee()))
        print('Box price + fee: {} €'.format(b.get_box_price()))
        print('_____________________________')
        print('List of fruits:')
        for f in b.fruits:
            print(f)
        current_box += 1
        print('_____________________________')
        print('\n')
    return
