from mapperino import MyMap


class SeparateChaining(MyMap):

    def __setitem__(self, k, v):
        self.ensurecapacity()

        i = hash(k) % self.N
        if self.A[i] is None:
            self.A[i] = []
        bucket = self.A[i]

        for j in range(len(bucket)):
            kj, vj = bucket[j]
            if kj == k:
                bucket[j] = (k, v)
                return

        self.n += 1
        bucket.append((k,v))

    def __getitem__(self, k):

        i = hash(k) % self.N
        if self.A[i] is None:
            return

        bucket = self.A[i]
        for j in range(len(bucket)):
            kj, vj = bucket[j]
            if kj == k:
                return bucket[j]

    def __delitem__(self, k):
        i = hash(k) % self.N
        bucket = self.A[i]
        if bucket is None:
            return
        self.A[i] = [(ki, v) for ki, v in bucket if ki != k]
        self.n -= 1

    def __iter__(self):
        for bucket in self.A:
            if bucket:
                for kv in bucket:
                    yield kv


