def scanG():
    # набор всех состояний, которые присутствуют у нашего алгоритма, состоит из: "H", "A", "B", "C", "S", "ER"
    CS = "H" #устанавливаем текущее состояние равным H

    with open("data.txt", "r") as fp:
        c = fp.read(1)
        while True:
            if CS == "H":
                if c == 'a':
                    c = fp.read(1)
                    CS = "A"
                elif c == 'b':
                    c = fp.read(1)
                    CS = "A"
                else:
                    CS = "ER"

            if CS == "A":
                if c == 'b':
                    c = fp.read(1)
                    CS = "C"
                else:
                    CS = "ER"

            if CS == "B":
                if c == 'a':
                    c = fp.read(1)
                    CS = "C"
                else:
                    CS = "ER"

            if CS == "C":
                if c == 'a':
                    c = fp.read(1)
                    CS = "A"
                elif c == 'b':
                    c = fp.read(1)
                    CS = "B"
                elif c == "c":
                    CS = "S"
                else: CS = "ER"

            if (CS == "S" or CS == "ER"):
                break

    if CS == "ER":
        return -1
    else:
        return 0