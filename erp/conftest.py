import os

os.environ["PYTEST_RUNNING"] = "true"
from erp.general.tests.fixtures import *  # noqa: F401, F403, E402
from erp.user.tests.fixtures import *  # noqa: F401, F403, E402
