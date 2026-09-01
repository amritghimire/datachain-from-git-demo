"""A tiny DataChain job, for trying out running a job straight from git."""

import datachain as dc

DATASET_NAME = "from_git_demo"

numbers = dc.read_values(
    n=[1, 2, 3, 4, 5],
    label=["one", "two", "three", "four", "five"],
)

doubled = numbers.mutate(doubled=dc.C("n") * 2).save(DATASET_NAME)
doubled.show()
