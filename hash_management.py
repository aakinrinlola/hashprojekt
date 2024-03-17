class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, stock):
        index = self.hash_function(stock.ticker_symbol)
        self.buckets[index].append(stock)

    def find(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for stock in bucket:
            if stock.name == key or stock.ticker_symbol == key:
                return stock
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, stock in enumerate(bucket):
            if stock.name == key or stock.ticker_symbol == key:
                del bucket[i]
                return True
        return False
