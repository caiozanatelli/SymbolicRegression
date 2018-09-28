import numpy as np
import csv
import sys

class Singleton(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class IOUtils(object):
    __metaclass__ = Singleton

    def __init__(self):
        pass

    def read_csv(self, file_dir):
        try:
            dataset_input = []
            with open(file_dir, 'rb') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                count = 0
                for row in csv_reader:
                    count += 1
                    dataset_input.append(map(float, row))
            return dataset_input
        except IOError as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)

    def write_output(self, file_dir, stats):
        try:
            with open(file_dir, 'a') as output:
                output.write(stats)
        except IOError as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)
