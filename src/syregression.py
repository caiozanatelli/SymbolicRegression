import argparse

def main(args):
    print('. : Symbolic Regression Solver : .')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A Genetic Programming approach \
                                    for Symbolic Regression')
    parser.add_argument('--pop-size', action='store', type=int, default=30,
                        help='Set the population size')
    parser.add_argument('--cross-prob', action='store', type=float, default=0.8,
                        help='Set the crossing-over probability')
    parser.add_argument('--mut-prob', action='store', type=float, default=0.05,
                        help='Set the mutation probability')
    parser.add_argument('--max-depth', action='store', type=int, default=7,
                        help='Set the maximum depth of the tree')
    parser.add_argument('--seed', action='store', type=int, default=1,
                        help='Set the seed for generating random numbers')
    parser.add_argument('--max-gen', action='store', type=int, default=30,
                        help='Set the number of generations that must be run')
    parser.add_argument('--tour-size', action='store', type=int, default=2,
                        help='Set the tournament size')
    parser.add_argument('--elitism', action='store', default=True,
                        help='Choose whether the algorithm must use elitism or not')
    parser.add_argument('--train', action='store', type=str, required=True,
                        help='Training dataset path')
    parser.add_argument('--out', action='store', type=str, required=True,
                        help='Output file path')
    args = parser.parse_args()
    main(args)