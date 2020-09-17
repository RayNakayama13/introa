with open('input.txt', 'r') as f:
    a = [f.read()]

class FizzBuzz():

    def __init__(self):
        list = [(int(x[0]), x[2:]) for x in a.split('\n')]
        list.sort()
        i = []
        s = []
        for n in len(list):
            i.append(list[n][0])
            s.append(list[n][1])
        m = a.pop(-1)
        return i, s, m

    def FizzBuzzExt(i, s, m):
        Output = []
        for I in i:
            if m%I  == 0:
                 Output.append(s)
            else:
                continue
        print(Output)
