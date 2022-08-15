import logging
import voluptuous as vol

from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.components.button import (PLATFORM_SCHEMA, ButtonEntity)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity_platform import AddEntitiesCallback

_LOGGER = logging.getLogger("prova")

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
})

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:

    button = {
        "name": config[CONF_NAME]
    }

    add_entities([MyButton(button, hass)])

class MyButton(ButtonEntity):
    # Implement one of these methods.

    def __init__(self, button, hass):
        self._unique_id = "caciocavallo"
        self._name = button["name"]
        self.hass = hass
    
    @property
    def unique_id(self) -> str:
        return self._unique_id

    @property
    def name(self) -> str:
        """Name of the entity."""
        return self._name

    def press(self) -> None:
        """Handle the button press."""
        self.hass.states.set("prova.pisani", "premutot")
        
    async def async_press(self) -> None:
        """Handle the button press."""