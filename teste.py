from func import soma, mult, div
def test_soma():
    assert soma([1, 2, 3]) == 6, "Deve ser 6"
def test_mult():
    assert mult((2, 3, 4)) == 24, "Deve ser 24"
def test_div():
    assert div((2, 3, 4)) == 24, "Deve ser 24"
if __name__ == "__main__":
    test_soma()
    test_mult()
    print('Tudo ok!')