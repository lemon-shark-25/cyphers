
class FrecuencyAnalysis:

    def __init__(self):
        self._alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  
        self._appereances = {}
        self._initAppereances()

    def _initAppereances(self):
        for i in self._alphabet:
            self._appereances[i] = 0

    def calAppereances(self, text):
        self._appereances["length"] = len(text)
        for char in text.upper():
            if char in self._alphabet:
                self._appereances[char] += 1

    def showStatistics(self):
        print(f"{'Letter':^8} | {'Frequency (%)':^14} | {'Appearances':^12}")
        print("-" * 40)
        for i in self._alphabet:
            frequency = (self._appereances[i] / self._appereances['length']) * 100 if self._appereances['length'] > 0 else 0
            print(f"{i:^8} | {frequency:^14.2f} | {self._appereances[i]:^12}")
