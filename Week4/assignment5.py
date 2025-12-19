class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        """Generator that lazily processes data one item at a time."""
        for item in self.data:
            processed_item = item * 2  
            yield processed_item

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

processor = DataProcessor(data)

gen = processor.process_data()

print(next(gen))  
print(next(gen)) 

print(next(gen))  
print(next(gen))  
