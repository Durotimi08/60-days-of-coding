class Version(list):
    def __init__(self, version):
        self.value = version.split(".")

    def compare(self, other):
        if len(self.value) > len(other.value):
            other.value.extend(["0" for _ in range(len(self.value) - len(other.value))])
        elif len(self.value) < len(other.value):
            self.value.extend(["0" for _ in range(len(other.value) - len(self.value))])

        self.value = [int(_) for _ in self.value]
        other.value = [int(_) for _ in other.value]

        for index in range(len(self.value)):
            if self.value[index] > other.value[index]:
                return 1
            elif self.value[index] < other.value[index]:
                return -1

        return 0


version1 = Version("1.0.1")
version2 = Version("1.0.2")

print(version1.compare(version2))
