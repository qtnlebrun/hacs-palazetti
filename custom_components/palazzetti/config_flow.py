"""Adds config flow for Palazzetti."""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from palazzetti_sdk_local_api import Hub
from .const import (
    CONF_HOST,
    DOMAIN,
    PLATFORMS,
)


class PalazzettiFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Palazzetti."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        self._errors = {}

        # Uncomment the next 2 lines if only a single instance of the integration is allowed:
        # if self._async_current_entries():
        #     return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            valid = await self._test_credentials(user_input[CONF_HOST])
            if valid:
                return self.async_create_entry(
                    title=user_input[CONF_HOST], data=user_input
                )
            else:
                self._errors["base"] = "auth"

            return await self._show_config_form(user_input)

        user_input = {}
        # Provide defaults for form
        user_input[CONF_HOST] = ""

        return await self._show_config_form(user_input)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return PalazzettiOptionsFlowHandler(config_entry)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        """Show the configuration form to edit host."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_HOST, default=user_input[CONF_HOST]): str}
            ),
            errors=self._errors,
        )

    async def _test_credentials(self, host):
        """Return true if host is valid."""
        try:
            hub = Hub(host)
            await hub.async_update(discovery=False, deep=False)
            if hub.hub_online:
                if hub.product_online:
                    return True
        except Exception:  # pylint: disable=broad-except
            pass
        return False


class PalazzettiOptionsFlowHandler(config_entries.OptionsFlow):
    """Palazzetti config flow options handler."""

    def __init__(self, config_entry):
        """Initialize HACS options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    async def async_step_init(self, user_input=None):  # pylint: disable=unused-argument
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            self.options.update(user_input)
            return await self._update_options()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(x, default=self.options.get(x, True)): bool
                    for x in sorted(PLATFORMS)
                }
            ),
        )

    async def _update_options(self):
        """Update config entry options."""
        return self.async_create_entry(
            title=self.config_entry.data.get(CONF_HOST), data=self.options
        )
