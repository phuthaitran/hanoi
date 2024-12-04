def find_district(n):
    match n:
        case 1:
            print("Ba Dinh")
        case 2: 
            print("Hoan Kiem")
        case 3:
            print("Tay Ho")
        case 4:
            print("Long Bien")
        case 5:
            print("Cau Giay")
        case 6:
            print("Dong Da")
        case 7:
            print("Hai Ba Trung")
        case 8:
            print("Hoang Mai")
        case 9:
            print("Thanh Xuan")
        case 10:
            print("Ha Dong")
        case 11:
            print("Bac Tu Liem")
        case 12:
            print("Nam Tu Liem")
        case _:
            print("You want to go to the countryside?")

find_district(5)
