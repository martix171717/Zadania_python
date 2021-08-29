import logging
logging.basicConfig(level=logging.DEBUG)
def calculator(operation, number1, number2):
    if operation == 1:
        addition = (number1 + number2)
        logging.info("Dodaję: %d i %d" % (number1, number2))
        return (f"Wynik to: {addition}")
    
    elif operation == 2:
        subtraction = number1 - number2
        logging.info("Od %d odejmuję %d" % (number1, number2))
        return f"Wynik to: {subtraction}"
    elif operation == 3:
        multiplication = number1 * number2
        logging.info("Mnożę %d i %d" % (number1, number2))
        return f"Wynik to: {multiplication}"
    elif operation == 4:
        division = number1 / number2
        logging.info("Dzielę %d na %d" % (number1, number2))
        return f"Wynik to: {division}"
    else:
        return "Nie ma takiego działania do wyboru"
        exit(1)
if __name__ == "__main__":
    logging.info("To kalkulator, który przyjmuje tylko dwie liczby. Potrafi dodawać, odejmować, mnożyć i dzielić.")
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    number1 = int(input("podaj składnik 1."))
    number2 = int(input("podaj składnik 2."))
    print(calculator(operation, number1, number2))
