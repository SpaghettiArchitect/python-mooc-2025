# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            self.minutes = self.minutes + 1 if self.minutes < 59 else 0

    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"


def main() -> None:
    watch = Stopwatch()

    for i in range(3600):
        print(watch)
        watch.tick()


if __name__ == "__main__":
    main()
