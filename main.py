class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start if not self.start % 2 else self.start + 1
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration()
        next_event = self.current
        self.current += 2
        return next_event


if __name__ == '__main__':
    en = EvenNumbers(10, 25)
    for i in en:
        print(i)
