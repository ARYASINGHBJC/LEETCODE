class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        # Parking limit for each type of car
        self.big_limit = big
        self.medium_limit = medium
        self.small_limit = small

        # Create an Array to store parked cars
        self.parking_array = [None] * (big + medium + small)

    def addCar(self, carType: int) -> bool:

        # Depending on carType, store the limit for the type of car
        if carType == 1:
            limit = self.big_limit
        elif carType == 2:
            limit = self.medium_limit
        else:
            limit = self.small_limit

        # Traverse linearly through the array from the left
        count = 0
        for i in range(len(self.parking_array)):

            # Count the number of cars parked in the system of that type
            if self.parking_array[i] == carType:
                count += 1

            # Stop if the count becomes equal to the limit
            if count == limit:
                return False

            # If the count is less than the limit, then add the car
            # to the first available empty slot from the left
            if self.parking_array[i] is None:
                self.parking_array[i] = carType
                return True

        # If no empty slot is found, then return False.
        # However, this line will never be executed if count < limit
        # because slot will be found before count becomes equal to limit
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)