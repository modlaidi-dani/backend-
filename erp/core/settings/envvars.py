from erp.general.utils.collection import deep_update
from erp.general.utils.setting import get_settings_from_environment

# Apply the settings
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))   # type: ignore
