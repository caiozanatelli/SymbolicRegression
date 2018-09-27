from multiprocessing import Process

class Mult:

    attrib = 0

    def __init__(self):
        attrib = 1

    def count(self, start ,end):
        for i in range(start, end):
            print(i)


if __name__ == '__main__':
    l = [Mult(), Mult(), Mult(), Mult()]

    for i in l:
        i.attrib = i.attrib + 200

    for i in l:
        print(i.attrib)