from django.shortcuts import render
from django.http import HttpResponse

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
                print(self.result)
                break


    def get_result_previosly_rolled(self):
        return self.result



d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)







def home(request):
    return render(request, 'dices/home.html')


def result(request):

    if request.method == 'POST':
        option = request.POST.get('dice')
        dice_type = "d-1"
        dice_image = 'images/d-1_image.png'
        result = -1

        if option == 'd4':
           dice_type = "d4"
           dice_image = 'images/d4_image.png'
           while True:
                d4.roll()
                result = d4.result
                if result != 0:
                    break

        elif option == 'd6':
           dice_type = "d6"
           dice_image = 'images/d6_image.png'
           while True:
                d6.roll()
                result = d6.result
                if result != 0:
                    break

        elif option == 'd8':
           dice_type = "d8"
           dice_image = 'images/d8_image.png'
           while True:
                d8.roll()
                result = d8.result
                if result != 0:
                    break   

        elif option == 'd10':
           dice_type = "d10"
           dice_image = 'images/d10_image.png'
           while True:
                d10.roll()
                result = d10.result
                if result != 0:
                    break   

        elif option == 'd12':
           dice_type = "d12"
           dice_image = 'images/d12_image.png'
           while True:
                d12.roll()
                result = d12.result
                if result != 0:
                    break   

        elif option == 'd20':
           dice_type = "d20"
           dice_image = 'images/d20_image.png'
           while True:
                d20.roll()
                result = d20.result
                if result != 0:
                    break                                            




    
   
    dices = {
            'result': result,
            'dice_type': dice_type,
            'dice_image': dice_image
        }    

    return render(request, 'dices/dice_result.html', dices)    

       


