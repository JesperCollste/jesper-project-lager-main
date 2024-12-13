"""
__author__  = "Jesper Collste"
__version__ = "3.12.1"
__email__   = "Jesper.Collste@elev.ga.ntig.se
"""


import csv
import os
import locale
from time import sleep

# Laddar datan från csv filen
def load_data(filename):
    cars = []

    with open(filename, 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])

            cars.append(  # list
                {  # dictionary
                    "id": id,
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return cars



def save_data(filename, cars): #funktion för att spara till databasen
    with open(filename, mode='w', newline='', encoding='UTF-8') as file: 
        writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
        writer.writeheader() 
        writer.writerows(cars)  

    print(f"Data successfully saved to {filename}")



# Remove a car by ID
def remove_car(cars, id):
    temp_car = None

    for car in cars:
        if car["id"] == id:
            temp_car = car
            break  # avslutar loopen när bilen har hittats

    if temp_car:
        cars.remove(temp_car)
        return f"car: {id} {temp_car['name']} was removed"
    else:
        return f"car with id {id} not found"


# Visar en specifik bil beroende på id som du angivit
def view_car(cars, id):
    for car in cars:
        if car["id"] == id:
            return f"Visar bilen: {car['name']} {car['desc']}"
    return "bilenen hittas inte"


# 
def get_car(cars, id):
    for car in cars:
        if car['id'] == id:
            return car


# Edit a car's details
def edit_car(cars, car, name, price, desc, quantity, id):
    car['name'] = name
    car['desc'] = desc
    car['price'] = price
    car['quantity'] = quantity

    return f"Ändrade bilen med id #{car['id']}"

def trim_text(text, length=25): #Funktion för att göra så ifall beskrivningen är för lång byts det mot ...
        return text if len(text) <= length else text[:length] + "..." 


def view_inventory(cars, sort_by_price=False): 
    def get_price(car):  # Hjälpfunktion för att få priset
        return car['price']

    if sort_by_price:
        cars = sorted(cars, key=get_price)

    # Skapa tabellens header
    header = f"{'ID':<5} {'NAMN':<30} {'BESKRIVNING':<25} {'PRIS':<15} {'KVANTITET':<15}"
    separator = "-" * 95  # Skapa en linje för separation

    # Rader för varje bil
    rows = []

    for car in cars:
        car_id = car['id']  # Använd det faktiska ID:t från listan
        name = car['name']
        desc = trim_text(car['desc'])  # Trimma beskrivningar som är för långa
        price = locale.currency(car['price'], grouping=True)
        quantity = car['quantity']

        row = f"{car_id:<5} {name:<30} {desc:<25} {price:<15} {quantity:<15}"
        rows.append(row)

    inventory_table = "\n".join([header, separator] + rows)

    return inventory_table




def add_car(cars, name, desc, price, quantity):
    # Hitta det högsta befintliga ID:t
    max_id = max((car['id'] for car in cars), default=0)
    new_id = max_id + 1  # Skapa ett nytt unikt ID

    # Lägg till bilen med det nya ID:t
    cars.append(
        {
            "id": new_id,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        }
    )
    return f"Lade till bilen: {new_id}"




locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

#FIlsökvägen till databsen
csv_file_path = "db_cars.csv"

# Load data from the CSV file
cars = load_data(csv_file_path)

#Håller koll ifall sort list är true eller false
is_sorted = False

while True: #Huvudkod
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        #Printar listan vanligt ifall is sorted fortfarande är false och printar den sorterade listan ifall den är true
        print(view_inventory(cars, sort_by_price=is_sorted))

        choice = input( #input för att fråga vilket val du vill göra
                         "Vill du:\n"
                         "(L) Lägg till en bil?\n"
                         "(V) Visa Namn och beskrivning på en bil?\n"
                         "(T) Ta bort en bil?\n"
                         "(Ä) Ändra Namn, Beskrivning, Pris och kvantitet på en bil?\n"
                         "(S) Visa listan sorterad efter pris (lägst till högst)?\n"
                         "Ditt val: "
                        ).strip().upper()

        if choice == "L": #Lägga till en bil i listan
            name = input("namn på bilen: ")
            desc = input("Beskrivning på bilen: ")
            price = float(input("pris: "))
            quantity = int(input("antal av bilener: "))
            print(add_car(cars, name, desc, price, quantity))
            save_data(csv_file_path, cars)  #Kallar på spara data funktionen

        elif choice == "S":  # När användaren trycker på S, sätt is_sorted till True
            is_sorted = True  # Lista blir sorterad
            print(view_inventory(cars, sort_by_price=True))  # Visa sorterad lista
            input("Press Enter to continue...")

        elif choice in ["V", "T", "Ä"]: #Lägger alla val som behöver specifik id i samma elif för att slippa fråga om vilket id flera gånger.
            index = int(input("Enter car ID: "))

            if choice == "Ä": #Ändrar en bil
                selected_car = get_car(cars, index)
                if selected_car:
                    print(f"ÄNDRA bilen MED ID {selected_car['name']}")
                    name = input(f"Förra namnet var: {selected_car['name']}, Ange det nya namnet:  ")
                    desc = input(f"Förra beskrivningen var: {selected_car['desc']}, Ange den nya beskrivningen: ")
                    price = float(input(f"Förra priset var: {selected_car['price']}, Ange det nya priset: "))
                    quantity = int(input(f"Förra mängden var: {selected_car['quantity']}, Ange den nya mängden: "))
                    print(edit_car(cars, selected_car, name, price, desc, quantity, index))
                    save_data(csv_file_path, cars)  #Kallar på spara data funktionen

            elif choice == "V": #Visar en bil
                selected_car = get_car(cars, index)
                if selected_car:
                    print(view_car(cars, index,))
                    input("Press Enter to continue...")

            elif choice == "T": #Tar bort en bil
                selected_car = get_car(cars, index)
                if selected_car:
                    print(remove_car(cars, index))
                    save_data(csv_file_path, cars)  #Kallar på spara data funktionen

    except ValueError: 
        print("Välj en bil med siffror")
        sleep(0.5)

     
