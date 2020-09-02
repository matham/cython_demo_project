

def test_class_doc():
    from cython_demo_project.numeric import NumericComputation
    assert NumericComputation.__doc__ == 'Computes something numerically.'


def test_enum_doc():
    from cython_demo_project.numeric import Numbers
    assert Numbers.__doc__ == 'Number list.'
