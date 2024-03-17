import csv
from datetime import datetime
import pickle
from hash_management import HashTable  # Angenommen, die HashTable Klasse ist hier definiert
from stock_management import Stock, StockPriceDay  # Angenommen, diese Klassen sind hier definiert

class DataManager:
    def __init__(self, hash_table):
        self.hash_table = hash_table

    def import_stock_data(self, filename, ticker_symbol):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Überspringen der Kopfzeile, falls vorhanden
            for row in reader:
                if len(row) >= 7:  # Sicherstellen, dass die Zeile genügend Daten enthält
                    date = datetime.strptime(row[0], '%Y-%m-%d')
                    open_price = float(row[1])
                    high = float(row[2])
                    low = float(row[3])
                    close = float(row[4])
                    volume = float(row[5])
                    adj_close = float(row[6])
                    price_data_day = StockPriceDay(date, open_price, high, low, close, volume, adj_close)
                    
                    stock = self.hash_table.find(ticker_symbol)
                    if stock:
                        stock.add_price_data(price_data_day)
                    else:
                        print(f"Stock with ticker symbol '{ticker_symbol}' not found.")

    def save_hash_table(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.hash_table, file)

    def load_hash_table(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.hash_table = pickle.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

# Beispiel für die Verwendung:
# hash_table = HashTable()  # Erstellen Sie eine neue Hashtabelle
# data_manager = DataManager(hash_table)
# data_manager.import_stock_data('stock_data.csv', 'AAPL')
# data_manager.save_hash_table('my_hash_table.pkl')
# data_manager.load_hash_table('my_hash_table.pkl')
