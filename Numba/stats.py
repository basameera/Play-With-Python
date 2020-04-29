import subprocess
from skylynx.utils import yaml_write, cli_args, yaml_read
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    cli_params = dict(
        task=0,
        fname='abc'
    )
    usage = '\n\tpython stats.py -a 1 -b <test file name w/o .py ext>\n' + \
        '\tpython stats.py -a 2'
    args = cli_args(cli_params, usage=usage)
    task = int(args['task'])
    fname = args['fname']

    # test each file and save stats
    if task == 1:
        cmd = 'python {}.py'.format(fname)

        cmd_list = cmd.replace('"', '').split(' ')

        n_itr = 100
        print(cmd, n_itr)
        results = []

        for n in range(n_itr):
            res = subprocess.run(cmd_list, stdout=subprocess.PIPE)
            result = float(res.stdout.decode('utf-8'))
            results.append(result)

        yd = dict(data=results)
        yaml_write('{}.yml'.format(fname), yd)

    # combine files and plot
    if task == 2:
        files = ['abc', '2_abc', '3_abc', '4_abc']
        mean = []
        std = []
        data = dict()
        for f in files:
            dt = yaml_read('{}.yml'.format(f))
            data[f] = dt['data']
            mean.append(np.mean(dt['data']))
            std.append(np.std(dt['data']))

        # other references
        # https://pythonforundergradengineers.com/python-matplotlib-error-bars.html
        # https://seaborn.pydata.org/generated/seaborn.barplot.html
        # https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html?highlight=errorbar#plotting-with-error-bars

        # https://benalexkeen.com/bar-charts-in-matplotlib/
        plt.style.use('ggplot')
        x = ['Pure Python', 'Numba @jit', 'Numba @njit', 'Numba @jit(nopython)']
        energy = mean
        variance = std

        x_pos = [i for i, _ in enumerate(x)]

        fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

        ax.bar(x_pos, energy, color='green', yerr=variance, capsize=10.0)
        plt.xlabel("File names")
        plt.ylabel("Execution time (seconds)")
        plt.title("Effects of Numba (loop of 1e6)")

        plt.xticks(x_pos, x)
        plt.savefig('stats.pdf')
        plt.show()

