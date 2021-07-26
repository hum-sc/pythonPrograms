class Room:
    pass


class Hotel:
    def __init__(self, capacity : int, parking_places : int ):
        self.capacity = capacity
        self.parking_places = parking_places
        self.guest = 0
    

    def add_guest (self, number_guest : int) -> None:
        self.guest += number_guest

    
    def remove_guest (self, number_guest : int) -> None:
        self.guest -= number_guest
    

    def show_guest_number (self) -> int :
        return self.guest


def run():
    hotel = Hotel(10,5)
    hotel.add_guest(17)
    hotel.remove_guest(5)
    print(hotel.show_guest_number())


if __name__ == '__main__':
    run()