from algorithm import AlgorithmA
from visualization import draw

def main():

    algo = AlgorithmA()

    algo.run(1000)

    algo.statistics()

    draw(algo)


if __name__ == "__main__":
    main()