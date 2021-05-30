from notebook import _sysinfo

def test_notebook():
    repo, hash = _sysinfo.pkg_commit_hash("../notebook")
    assert repo == "repository"
    assert len(hash) > 0 # git hash 


def test_current():
    repo, hash = _sysinfo.pkg_commit_hash(".")
    assert repo == ''
    assert hash == ''
