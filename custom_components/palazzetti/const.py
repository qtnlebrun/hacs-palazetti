"""Constants for palazzetti."""

from homeassistant.components.climate.const import FAN_AUTO, FAN_HIGH
from homeassistant.const import Platform
from homeassistant.helpers.entity import EntityCategory

# Base component constants
NAME = "Palazzetti"
DOMAIN = "palazzetti"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/qtnlebrun/hacs-palazetti/issues"

# Icons
ICON_FIRE = "mdi:fire"
ICON_INFO = "mdi:information-outline"

# Platforms
PLATFORMS = [Platform.CLIMATE, Platform.NUMBER, Platform.SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_HOST = "host"

# Defaults
DEFAULT_NAME = DOMAIN

# Fan levels
FAN_1 = "1"
FAN_2 = "2"
FAN_3 = "3"
FAN_4 = "4"
FAN_5 = "5"

FAN_PALAZZETTI_TO_HA = {
    1: FAN_1,
    2: FAN_2,
    3: FAN_3,
    4: FAN_4,
    5: FAN_5,
    6: FAN_HIGH,
    7: FAN_AUTO,
}

FAN_HA_TO_PALAZZETTI = {
    FAN_1: 1,
    FAN_2: 2,
    FAN_3: 3,
    FAN_4: 4,
    FAN_5: 5,
}

SENSOR_KEY = "key"
SENSOR_ATTRS = "attrs"
SENSOR_CATEGORY = "cat"
SENSOR_UNIT = "unit"

SENSORS = {
    "Status": dict(
        [
            (SENSOR_KEY, "STATE"),
            (SENSOR_ATTRS, {"status": "STATUS"}),
            (SENSOR_CATEGORY, EntityCategory.DIAGNOSTIC),
        ]
    ),
    "Dpress": dict(
        [
            (SENSOR_KEY, "DP"),
            (SENSOR_CATEGORY, EntityCategory.DIAGNOSTIC),
        ]
    ),
    "Dpress Target": dict(
        [
            (SENSOR_KEY, "DPT"),
            (SENSOR_CATEGORY, EntityCategory.DIAGNOSTIC),
        ]
    ),
    "Fan Speed": dict(
        [
            (SENSOR_KEY, "F1RPM"),
            (SENSOR_CATEGORY, EntityCategory.DIAGNOSTIC),
            (SENSOR_UNIT, "rpm"),
        ]
    ),
    "Power Time": dict(
        [
            (SENSOR_KEY, "POWERTIME"),
            (SENSOR_CATEGORY, EntityCategory.DIAGNOSTIC),
        ]
    ),
    "Service Time": dict(
        [
            (SENSOR_KEY, "SERVICETIME"),
            (SENSOR_CATEGORY, EntityCategory.DIAGNOSTIC),
        ]
    ),
}


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
