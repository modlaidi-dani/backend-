from erp.corelib.utils.collection import deep_update
from erp.corelib.utils.setting import (
    ENVVAR_SETTINGS_PREFIX,
    get_settings_from_environment,
)

# Apply the settings
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore
