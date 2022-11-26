"""PalazzettiEntity class"""

from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, NAME, VERSION, ATTRIBUTION


class PalazzettiEntity(CoordinatorEntity):
    """PalazzettiEntity class"""

    _entity_id = None

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        config_entry: ConfigEntry,
        entity_id: str = None,
    ):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.entity_id = entity_id

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        if self._entity_id is not None:
            return self.config_entry.entry_id + "_" + self._entity_id
        return self.config_entry.entry_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("SN")),
            "integration": DOMAIN,
        }
