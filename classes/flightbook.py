
class Flight:
    """A Flight with a particular passenger Aircraft"""


    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')
        if not number[:2].isupper():
            raise ValueError(f'Invalid value error "{number}"')
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError (f'Invalid route "{number}"')         
        self._number = number
        self._aircraft = aircraft
        rows,seats = self._aircraft.seat_planning()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model()
    
    def allocate_seat(self,seat,passenger):
        """Allocate a seat to a passenger
        
        Arg:
            seat:A seat designator is such as 12C or 21F.
            passesnger: The passenger Name
            
        raises:
            ValueError : If the seat is unavailable
        """
        row,seat_letters = self._aircraft.seat_planning()

        letter = sear[-1]
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat Row {row_text}')
        if row not in rows:
            raise ValueError(f'Invalid row number {row}')
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already filled")
        self._seating[row][letter] = passenger

    


class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seat_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration
    def model(self):
        return self._model
    def seat_planning(self):
        return (range(1,self._num_rows +1), 'ABCDEFGHIJ'[:self._num_seat_per_row]  ) 
    

f = Flight("BA758",Aircraft("EUB-T","Airbus A319",num_rows=22,num_seats_per_row=6))
# print(f.aircraft_model())

print(f._seating)

from pprint import pprint as pp

print(pp(f._seating))
    