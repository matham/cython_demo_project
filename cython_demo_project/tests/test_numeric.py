
def test_sum():
    from cython_demo_project.numeric import NumericComputation

    assert NumericComputation(1, 2).compute_sum() == 3
