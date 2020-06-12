from mrjob import MRJob

class FriendByAge(mrjob):
    def mapper(self, _, line):
        (user, name, age, number) = line.split(',')

        yield age, int(number)

    def reducer(self, key, values):
        itens = list(values)

        yield key, sum(itens) / len(list)

if __name__ == "__main__":
    FriendByAge.run()