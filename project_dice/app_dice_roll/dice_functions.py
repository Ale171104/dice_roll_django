import random


class Dice:


    def __init__(self, sides):
        self.sides = sides
        self.increment = 0
        self.result = 0
        


        match sides:
            case 4:
                self.increment = 1081080000

            case 6:
                self.increment = 772200000

            case 8:
                self.increment = 600600000

            case 10:
                self.increment = 491400000

            case 12:
                self.increment = 415800000  

            case 20:
                self.increment = 257400000              



    def roll(self):
        random_value = random.randint(1, 5405400000)
        divisor = 0
        


        for side in range(1, self.sides + 1):
            divisor = divisor + self.increment

            if random_value <= divisor:
                self.result = int(side)                             
                
                
        return self.result

    def get_result_previosly_rolled(self):
        return self.result
            


    
        