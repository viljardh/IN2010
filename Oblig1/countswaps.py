class CountSwaps(list):
    swaps = 0

    def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]

    def mergeswap(self):
        self.swaps += 1