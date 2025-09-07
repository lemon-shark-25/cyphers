from frecuencyAnalysis import FrecuencyAnalysis, FrecuencyReference

running = True
text = ""
option = 0
analysis = FrecuencyAnalysis()

def menu():
    print("--- Frecuency Analysis --")
    print("1. Enter the text to analyse")
    print("2. Get statistics")
    print("3. Reference statistics")
    print("4. Close programme")


while running:
    menu()
    option = int(input("Choose an option: "))

    match option:
        case 1:
            text = str(input("Write the text to analyse:\n"))
        case 2:
            analysis.calAppereances(text)
            analysis.showStatistics()
        case 3:
            pass
        case 4:
            running = False
            print("Closing programme.")
        case _:
            print("Not a valid option.")

    input()
