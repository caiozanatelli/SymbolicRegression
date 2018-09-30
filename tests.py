import glob as gl
import os
import subprocess as sp

TEST_OUTPUT  = 'test_output'
INPUT_FOLDER = 'datasets'

POP_SIZES = [50, 100, 500]
NGENS     = [50, 100, 500]
TOUR_SIZE = [2, 5]
PCROSS    = [0.9, 0.6]
PMUT      = [0.3]

params = ['--pop-size ' + str(p) + ' --tour-size ' + str(k) + \
        ' --ngen ' + str(g) + ' --cross-prob ' + str(c) + \
        ' --mut-prob ' + str(m) \
        for p in POP_SIZES for g in NGENS for k in TOUR_SIZE for (c,m) in \
        zip(PCROSS,PMUT)]

sp.call(['rm', '-rf', TEST_OUTPUT])
sp.call(['mkdir', TEST_OUTPUT])

input_folders = [f for f in os.listdir('./' + INPUT_FOLDER) if not os.path.isfile(f)]
num_tests = len(input_folders) * len(params_list) * 30
curr_test = 0

for folder in input_folders:
    name = TEST_OUTPUT + '/' + folder
    sp.call(['mkdir', name])

    for param in params_list
        name = name + '/' + param
        name = name.replace(' ', '-').replace('--', '-')
        sp.call('[mkdir', name)

        for seed in range(30):
            curr_test += 1
            output_name = name + '/' + str(seed) + '.out'
            output_file = open(output_name, 'w')

            arg_list = [
                        'src/syregression.py', folder + '/' + '/train.csv',
                        folder + '/' + '/test.csv'] + param.split() + \
                        ['--seed', str(seed)]

            progress = ((curr_test / num_tests) * 100)
            print('(' + str(round(progress, 2)) + '%)', ' '.join(arg_list))
            sp.call(arg_list, stdout = output_name)
            output_file.close()