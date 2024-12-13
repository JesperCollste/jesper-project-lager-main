"""
__author__  = "Jesper Collste"
__version__ = "3.12.1"
__email__   = "Jesper.Collste@elev.ga.ntig.se"
"""
import csv

cars = [
    {
        "id": 0,
        "name": "Toyota Corolla",
        "desc": "En paver och branslesnal kompaktbil",
        "price": 220000,
        "quantity": 5
    },
    {
        "id": 1,
        "name": "Ford Mustang",
        "desc": "En klassisk amerikansk sportbil med V8-motor",
        "price": 600000,
        "quantity": 3
    },
    {
        "id": 2,
        "name": "Audi A4",
        "desc": "En lyxig sedan med avancerad teknik och komfortåäö",
        "price": 450000,
        "quantity": 4
    },
    {
        "id": 3,
        "name": "Volvo XC90",
        "desc": "En saker och rymlig SUV perfekt for familjer",
        "price": 650000,
        "quantity": 2
    },
    {
        "id": 4,
        "name": "Mercedes-Benz C-Class",
        "desc": "En elegant och stilren bil med en kraftfull motor",
        "price": 550000,
        "quantity": 6
    },
    {
        "id": 5,
        "name": "BMW 320i",
        "desc": "En sportig och hogpresterande bil med bra hantering",
        "price": 500000,
        "quantity": 4
    },
    {
        "id": 6,
        "name": "Volkswagen Golf",
        "desc": "En praktisk och mangsidig hatchback",
        "price": 250000,
        "quantity": 7
    },
    {
        "id": 7,
        "name": "Chevrolet Bolt",
        "desc": "En elbil med lang rackvidd och miljovanliga funktioner",
        "price": 350000,
        "quantity": 3
    },
    {
        "id": 8,
        "name": "Honda Civic",
        "desc": "En popular och bransleeffektiv bil",
        "price": 230000,
        "quantity": 5
    },
    {
        "id": 9,
        "name": "Porsche 911",
        "desc": "En ikonisk sportbil med enastende prestanda",
        "price": 1200000,
        "quantity": 1
    },
    {
        "id": 10,
        "name": "Nissan Leaf",
        "desc": "En budgetvanlig elbil med enkel teknik och bra rackvidd",
        "price": 300000,
        "quantity": 6
    },
    {
        "id": 11,
        "name": "Ferrar F40",
        "desc": "Ferrarin som de mäktigaste människorna i världen äger",
        "price": 16400000,
        "quantity": 1
    }
]




# Define the CSV file path
csv_file_path = "db_cars.csv"

# Write the cars data to a CSV file
with open(csv_file_path, mode='w',encoding='UTF-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
    writer.writeheader()  # Write the header row
    writer.writerows(cars)  # Write the product data

print(f"Data successfully saved to {csv_file_path}")

def save_data(filename, cars):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
        writer.writeheader() 
        writer.writerows(cars)  

    print(f"Data successfully saved to {filename}")