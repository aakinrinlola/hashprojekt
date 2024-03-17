# Klassendefinitionen für StockPriceDay und Stock

class StockPriceDay:
    def __init__(self, date, open_price, high, low, close, volume, adj_close):
        self.date = date
        self.open_price = open_price
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adj_close = adj_close

class Stock:
    def __init__(self, name, wkn, ticker_symbol):
        self.name = name
        self.wkn = wkn
        self.ticker_symbol = ticker_symbol
        self.price_data = []  # Hält StockPriceDay Objekte

    def add_price_data(self, price_data_day):
        if len(self.price_data) >= 30:
            self.price_data.pop(0)  # Entferne den ältesten Eintrag, wenn bereits 30 Tage Daten vorhanden sind
        self.price_data.append(price_data_day)

# Klassendefinition für HashTable

