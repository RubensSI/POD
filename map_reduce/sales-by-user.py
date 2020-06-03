from mrjob.job import MRJob

class SalesByUser(MRJob):
    def mapper(self, _, line):
        (userID, _, amount) = line.split(',')
        
        yield userID, float(amount)

    def reducer(self, key, values):
        items = list(values)

        total = sum(items)

        yield key, (min(items), max(items), total, total / len(items))
        
if __name__ == "__main__":
    SalesByUser.run()