from mrjob.job import MRJob

class SalesByUser(MRJob):

    def mapper(self, _, line):
        (userID, _, amount) = line.split(',')
        yield userID, float(amount)

    def reducer(self, key, values):
        items = list(values)
        soma = sum(items)
        maxValue = max(items)
        minValue = min(items)
        yield key, (max(items), min(items), soma, soma / len(items)) 

if __name__ == '__main__':
    SalesByUser.run()