# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import timeit
    reps = 100000

    print("Set: ", timeit.timeit("run()", setup="from set import run", number=reps))
    print("Valeria: ", timeit.timeit("run()", setup="from valeria import run", number=reps))
