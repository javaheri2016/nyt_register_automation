from driver import browser
from tests.test_login import *
from tests.test_register import *
from pytest_bdd import scenarios, feature
import pytest


scenarios('test_scenarios.feature')

