import csv
import numpy as np #Liste von Schlusskursen in ein eigenes NumArray darzustellen 
import gnuplotlib as gp #um daten grafisch anzuzeigen

class HashTable:
    def __init__(self, size=1031):  # Wählen Sie eine geeignete Größe; 1031 ist ein Beispiel.
        self.size = size
        self.table = [None] * size
    
    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size
    
    def quadratic_probe(self, key, i):
        return (self.hash(key) + i**2) % self.size
    
    def add(self, key, value):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Wenn der Schlüssel bereits existiert, aktualisieren Sie den Wert.
                self.table[index] = (key, value)
                return
            i += 1
            index = self.quadratic_probe(key, i)
        self.table[index] = (key, value)
    
    def delete(self, key):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            i += 1
            index = self.quadratic_probe(key, i)
    
    def search(self, key):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Rückgabe des zugehörigen Werts, wenn der Schlüssel gefunden wird
            i += 1
            index = self.quadratic_probe(key, i)
        return None  # Rückgabe von None, wenn der Schlüssel nicht gefunden wird
    

    
    def import_data_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stock_name = row['Name']
                stock_data = (row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Adj Close'])
                self.add(stock_name, stock_data)


    def generate_plot(self, stock_name):
        stock_data = self.search(stock_name)
        if stock_data is None:
            print("Aktie nicht gefunden.")
            return
        
        closes = [float(day[3]) for day in stock_data[-30:]]  # Annahme: Close ist an der vierten Position in den Kursdaten
        graph = np.array(closes)
        gp.plot(graph, _with='line', terminal='dumb 200,20', unset='grid')


def main():
    table_size = 1031  # Wählen Sie eine geeignete Größe; 1031 ist ein Beispiel.
    hash_table = HashTable(size=table_size)

    while True:
        command = input("Enter a command (ADD, DEL, IMPORT, SEARCH, PLOT, SAVE, LOAD, QUIT): ").strip().upper()

        if command == "ADD":
            stock_name = input("Enter the stock name: ")
            # Hier könnten Sie weitere Informationen wie WKN und Kürzel eingeben
            stock_data = input("Enter the stock data (e.g., Open, High, Low, Close, Volume, Adj Close): ")
            hash_table.add(stock_name, stock_data)
            print("Stock added successfully.")

        elif command == "DEL":
            stock_name = input("Enter the stock name to delete: ")
            # Hier könnten Sie zusätzliche Logik implementieren, um Aktien zu löschen
            hash_table.delete(stock_name)
            print("Stock deleted successfully.")

        elif command == "IMPORT":
            filename = input("Enter the filename to import stock data from: ")
            hash_table.import_data_from_csv(filename)
            print("Stock data imported successfully.")

        elif command == "SEARCH":
            stock_name = input("Enter the stock name to search for: ")
            stock_data = hash_table.search(stock_name)
            if stock_data:
                print("Stock found:", stock_data)
            else:
                print("Stock not found.")

        elif command == "PLOT":
            stock_name = input("Enter the stock name to plot: ")
            hash_table.generate_plot(stock_name)

        elif command == "SAVE":
            filename = input("Enter the filename to save hash table to: ")
            # Hier könnten Sie die Hashtabelle in eine Datei speichern
            print("Hash table saved to", filename)

        elif command == "LOAD":
            filename = input("Enter the filename to load hash table from: ")
            # Hier könnten Sie die Hashtabelle aus einer Datei laden
            print("Hash table loaded from", filename)

        elif command == "QUIT":
            print("Exiting the program...")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()


