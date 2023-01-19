from os import system
class Emulator:
    def __init__(self) -> None:
        self.createBank()
        self.registers = [0,0,0,0,0,0,0,0]
        self.updateScreen()
    def clearConsole(self):
        system("clear" if system == "nt" else "cls")
    def clearScreen(self):
        for i in range(1024):
            self.bank[15][i] = 0
    def createBank(self) -> None:
        self.bank = []
        for i in range(16):
            self.bank.append([])
            for a in range(pow(2, 16)):
                self.bank[i].append(0)
    def load(self, program: str) -> None:
        program = program.split("\n")
        for i in range(len(program)):
            program[i] = program[i].split(" ")
        for i in range(len(program)):
            for a in range(len(program[i])):
                program[i][a] = int(program[i][a])

    def updateScreen(self):
        self.clearConsole()
        printing = []
        for i in range(1024):
            if i % 63 == 0:
                printing.append("")
            printing[i//64] += chr(self.bank[15][i]) if self.bank[15][i] != 0 else " "
        print("_" * 64)
        printing.pop()
        for i in printing:
            print("|" + i + "|")
        print("-" * 64)
    


em = Emulator()
while True:
    em.updateScreen()
    input()