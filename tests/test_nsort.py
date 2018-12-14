from run import nsorted

def test_nsort():
    data = ['9-nine', '10-ten']
    assert list(nsorted(data)) == data
