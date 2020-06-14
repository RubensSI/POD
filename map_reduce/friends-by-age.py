from mrjob.job import MRJob

class FriendsByAge(MRJob):

    def mapper(self, _, line):
        (_, _, age, amount) = line.split(',')
        yield age, int(amount)

    def reducer(self, key, values):
        listFriends = list(values)
        
        yield key, sum(listFriends) / len(listFriends)

if __name__ == "__main__":
    FriendsByAge.run()