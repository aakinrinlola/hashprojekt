from hash_management import HashTable
from data_management import DataManager
from stock_management import Stock, StockPriceDay
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys


# Erstellen einer neuen Hashtabelle
hash_table = HashTable()

# Erstellen einer neuen DataManager Instanz mit der Hashtabelle
data_manager = DataManager(hash_table)

def display_menu():
    print("\nAktienverwaltungssystem")
    print("1. Aktie hinzufügen")
    print("2. Aktie löschen")
    print("3. Kursdaten importieren")
    print("4. Aktie suchen")
    print("5. Schlusskurse plotten")
    print("6. Hashtabelle speichern")
    print("7. Hashtabelle laden")
    print("8. Beenden")
    choice = input("Wählen Sie eine Option: ")
    return choice

def add_stock(hash_table):
    name = input("Name der Aktie: ")
    wkn = input("WKN der Aktie: ")
    ticker_symbol = input("Kürzel der Aktie: ")
    stock = Stock(name, wkn, ticker_symbol)  # Erstellen eines neuen Stock-Objekts
    hash_table.insert(stock)  # Hinzufügen des Stock-Objekts zur Hashtabelle
    print(f"Aktie {name} wurde hinzugefügt.")

def delete_stock(hash_table):
    ticker_symbol = input("Kürzel der zu löschenden Aktie: ")
    success = hash_table.delete(ticker_symbol)  # Versuch, die Aktie zu löschen
    if success:
        print(f"Aktie mit dem Kürzel {ticker_symbol} wurde gelöscht.")
    else:
        print(f"Aktie mit dem Kürzel {ticker_symbol} konnte nicht gefunden werden.")

def plot_stock_prices(stock):
    # Überprüfen, ob die Aktie Kursdaten hat
    if not stock.price_data:
        print("Keine Kursdaten für diese Aktie vorhanden.")
        return

    dates = [price_data_day.date for price_data_day in stock.price_data]
    closes = [price_data_day.close for price_data_day in stock.price_data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, closes, marker='o', linestyle='-')
    
    plt.title(f"Schlusskurse der letzten {len(dates)} Tage: {stock.name}")
    plt.xlabel("Datum")
    plt.ylabel("Schlusskurs")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
    plt.tight_layout()
    plt.show()

def main():
    while True:
        choice = display_menu()

        if choice == '1':
            add_stock(hash_table)
        
        elif choice == '2':
            delete_stock(hash_table)
        
        elif choice == '3':
            filename = input("Dateiname der CSV-Datei: ")
            ticker_symbol = input("Kürzel der Aktie: ")
            data_manager.import_stock_data(filename, ticker_symbol)
        
        elif choice == '4':
            ticker_symbol = input("Kürzel der zu suchenden Aktie: ")
            stock = hash_table.find(ticker_symbol)
            if stock:
                print(f"Aktie gefunden: {stock.name}")
            else:
                print("Aktie nicht gefunden.")
        
        elif choice == '5':
            ticker_symbol = input("Kürzel der Aktie für den Plot: ")
            stock = hash_table.find(ticker_symbol)
            if stock:
                plot_stock_prices(stock)
            else:
                print("Aktie nicht gefunden.")
        
        elif choice == '6':
            filename = input("Speicherdateiname: ")
            data_manager.save_hash_table(filename)
        
        elif choice == '7':
            filename = input("Dateiname zum Laden: ")
            data_manager.load_hash_table(filename)
        
        elif choice == '8':
            print("Programm wird beendet.")
            sys.exit()
        
        else:
            print("Ungültige Eingabe, bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
