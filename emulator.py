from os import system
class Emulator:
    def __init__(self) -> None:
        self.createBank()
        self.registers = ["0" * 64 for i in range(8)]
        self.updateScreen()
    def clearConsole(self):
        system("clear" if system == "nt" else "cls")
    def clearScreen(self):
        for i in range(1024):
            self.bank[15][i] = "0" * 64
    def createBank(self) -> None:
        self.bank = []
        for i in range(16):
            self.bank.append([])
            for a in range(pow(2, 16)):
                self.bank[i].append("0" * 64)
    def load(self, program: str) -> None:
        print(program)
        program = program.split("\n")
        for i in range(len(program)):
            program[i] = program[i].split(" ")
        for i in range(len(program)):
            for a in range(len(program[i])):
                self.bank[0][a*(i+1)] = program[i][a]

    def updateScreen(self):
        self.clearConsole()
        printing = []
        for i in range(1024):
            if i % 63 == 0:
                printing.append("")
            printing[i//64] += chr(int(self.bank[15][i],2)) if int(self.bank[15][i],2) != 0 else " "
        print("_" * 64)
        printing.pop()
        for i in printing:
            print("|" + i + "|")
        print("-" * 64)

    def runASM(self):
        i = 0
        presses = []
        while i < len(self.bank[0]):
            opcode = self.bank[0][i]
            print(f"Opcode: {opcode}, i: {i}")
            a = int(self.bank[0][i + 1],2)
            b = int(self.bank[0][i + 2],2)
            c = int(self.bank[0][i + 3],2)
            
            if opcode[0] == "1":
                a = self.registers[a]
            if opcode[1] == "1":
                b = self.registers[b]

            opcode = int(opcode[2:],2)
            if opcode == 0:
                i += 4
                continue
            elif opcode == 1:
                self.registers[c] = a
            elif opcode == 2:
                self.registers[c] = a + b
            elif opcode == 3:
                self.registers[c] = a - b
            elif opcode == 4:
                self.registers[c] = a * b
            elif opcode == 5:
                self.registers[c] = a // b
            elif opcode == 6:
                self.registers[c] = a & b
            elif opcode == 7:
                self.registers[c] = a | b
            elif opcode == 8:
                self.registers[c] = a ^ b
            elif opcode == 9:
                self.registers[c] = a << b
            elif opcode == 10:
                self.registers[c] = a >> b
            elif opcode == 11:
                self.registers[c] = ~a
            elif opcode == 12:
                i = c
            elif opcode == 13:
                if a == b:
                    i = c
            elif opcode == 14:
                if a != b:
                    i = c
            elif opcode == 15:
                if a < b:
                    i = c
            elif opcode == 16:
                if a <= b:
                    i = c
            elif opcode == 17:
                if a > b:
                    i = c
            elif opcode == 18:
                if a >= b:
                    i = c
            elif opcode == 19:
                self.bank[c][b] = a
            elif opcode == 20:
                self.registers[a] = self.bank[c][b]
            elif opcode == 21:
                self.updateScreen()
            elif opcode == 22:
                break
            i += 4
                



if __name__ == "__main__":
    em = Emulator()
    with open(input("File: "), "r") as f:
        em.load(f.read())
        em.runASM()