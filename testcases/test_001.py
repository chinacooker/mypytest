import  pytest
import pdb
def f():
    raise SystemExit
def test001():
    with pytest.raises(SystemExit):
        f()

@pytest.mark.test
def test002():
    # pdb.set_trace()
    print('xx')
    assert 1==1
pytest.main()


