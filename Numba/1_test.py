import random
import time
from skylynx.utils import cli_args


def get_random():
    """Put what ever the function you want here that will loop. This can be acc. by numba
    """
    return random.random()


def loop(n_loop_iterations):
    for n in range(n_loop_iterations):
        x = get_random()


if __name__ == "__main__":
    cli_params = dict(itrs=100
                      )

    args = cli_args(cli_params)
    n_loop_iterations = int(args['itrs'])

    st = time.time()

    loop(n_loop_iterations)

    et = time.time()

    print(et-st)