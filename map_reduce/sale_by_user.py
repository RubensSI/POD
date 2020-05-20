from mrjob.job import mrjob

class SelasByUser(WRJob):
    def mapper(self, _, line):
        (userID, _, amount) = line.split(',')
        yield userID, amount

    def reducer(self, key, values):
        yield key, sum(values)