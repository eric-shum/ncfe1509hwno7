class strCompare:
    def __init__(self):
        self.mismatchchar = 0

    def compare(self, str1, str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                print("char mismatch: " + str1[i] + ", " + str2[i])
                self.mismatchchar += 1
                break
        return self.mismatchchar
