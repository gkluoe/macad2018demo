""" Some sample pytest tests """
import subprocess
from ConfigParser import ConfigParser
from pylint import epylint as lint
from pytest import raises
import macad2018demo 


def test_lint():
    (out, err) = lint.py_run('macad2018demo', return_std="True")
    result = out.read()
    if not '10.00/10' in result.split(" "):
       print "Failed pylint!"
       print result 
       assert False


def test_version(capsys):
    """Test that the version number reported by our tool
       matches what we think it should be

       capsys is a _fixture_:
         https://docs.pytest.org/en/latest/fixture.html
    """
    # Read our supposed version from setup.cfg
    config = ConfigParser()
    config.read('setup.cfg')
    cfg_version = config.get('bumpversion', 'current_version')

    # Call our tool's argument processing function with
    # a single argumnent of '-v'. This should report the
    # version number and exit - except, we trap the exit.
    with raises(SystemExit): # Trap the SystemExit exception
        macad2018demo.process_args(['-v'])

    # Stderr contains our version number
    out, err = capsys.readouterr()

    # Do they match?
    assert err.strip() == cfg_version

