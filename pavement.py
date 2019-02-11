from paver.easy import *
from paver.setuputils import setup
import multiprocessing
import json
import os

setup(
    name="python-lettuce-todo",
    packages=['features'],
    version="1.0.0",
    url="https://www.lambdatest.com/",
    author="Lambdatest",
    description=("Lettuce Integration with Lambdatest"),
    license="MIT",
    author_email="support@lambdatest.com"
)


def run_behave_test(filename, task_id=0):
    sh('TASK_ID=%s env=%s lettuce features/test.feature ' % (task_id, filename,))


@task
@consume_nargs(1)
def run(args):
    """

    :return:
    """
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=run_behave_test, args=(args[0], i,))
        jobs.append(p)
        p.start()
