import ncs


def test_get_by_name():
    assert ncs.get(name='Royal Magenta').rgb == (100, 39, 72)
    assert ncs.get(name='Royal Magenta').hex == '642748'


def test_list_all():
    ncs_colors = ncs.all()
    assert ncs_colors[0].rgb == (209, 222, 221)
    assert ncs_colors[0].name == 'IRIS 8'
