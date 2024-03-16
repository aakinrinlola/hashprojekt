import csv
from datetime import datetime

class FileHandler:
    @staticmethod
    def read_stock_data_from_csv(filename):
        stock_data = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = datetime.strptime(row['Date'], '%Y-%m-%d')  # Annahme: Datum im Format 'YYYY-MM-DD'
                open_price = float(row['Open'])
                close_price = float(row['Close'])
                high_price = float(row['High'])
                low_price = float(row['Low'])
                volume = int(row['Volume'])
                adj_close = float(row['Adj Close'])
                stock_course = StockCourse(date, open_price, close_price, high_price, low_price, volume, adj_close)
                stock_data.append(stock_course)
        return stock_data

class StockCourse:
    # Hier kommt Ihre StockCourse-Implementierung hin (wie bereits gezeigt)
    pass

# Verwendung:
filename = 'stock_data.csv'  # Annahme: CSV-Datei mit Kursdaten
stock_data = FileHandler.read_stock_data_from_csv(filename)
