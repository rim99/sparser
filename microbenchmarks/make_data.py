#
# Creates fake numeric CSV data.
#

import numpy as np
import sys

import argparse

def generate_data(rows, columns, maxint=1000000, filename="data/numbers.csv"):
    numbers = np.random.rand(rows,columns) * maxint
    np.savetxt("data/numbers.csv", numbers, fmt="%d")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Number of lines in the file.')
    parser.add_argument('-l', '--lines', metavar='lines', type=int, default=[1000000], nargs=1,
            help='number of lines to generate in the file')
    parser.add_argument('-c', '--cols', metavar='cols', type=int, default=[1], nargs=1,
            help='number of columns to generate in the file')

    args = parser.parse_args()

    rows = args.lines[0]
    columns = args.cols[0]
    generate_data(rows, columns)
