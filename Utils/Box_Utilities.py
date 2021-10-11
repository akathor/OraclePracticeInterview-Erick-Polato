from Classes.Box import Box


def package_into_boxes(fruits):
    boxes = [Box()]
    i = 0
    for f in fruits:
        if boxes[i].get_box_weight() + f.get_weight() > 1000:
            i += 1
            boxes.append(Box())
        boxes[i].insert_fruit(f)
    return boxes

def print_boxes(boxes, packaging_fee):
    i = 1
    for b in boxes:
        print("BOX #{}".format(i))
        print('_____________________________')
        print('Box Weight: {}'.format(b.get_box_weight()))
        print('Box fruits price: {} €'.format(b.get_box_price()))
        b.add_fee(packaging_fee)
        print('Box price + fee: {} €'.format(b.get_box_price()))
        print('_____________________________')
        print('List of fruits:')
        for f in b.fruits:
            print(f)
        i += 1
        print('_____________________________')
        print('\n')
    return
