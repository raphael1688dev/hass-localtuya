"""Test for localtuya coordinator."""

from . import *

DPS_STATUS = {"1": True, "19": 1234}


def create_device(device_config: dict[str, Any]) -> coordinator.TuyaDevice:
    hass = HomeAssistant("")
    entry = ConfigEntry(**create_entry({DEVICE_NAME: device_config}))
    hass.data.setdefault(DOMAIN, {entry.entry_id: {}})
    device = coordinator.TuyaDevice(hass, entry, device_config)
    device._interface = Mock(is_connected=True)
    device._interface.status = AsyncMock(return_value=DPS_STATUS)
    device._interface.update_dps = AsyncMock()
    device.status_updated = Mock()
    return device


async def test_refresh_wifi_device_uses_update_dps():
    device = create_device({**DEVICE_CONFIG, "entities": []})

    await device._async_refresh(None)

    device._interface.update_dps.assert_awaited_once_with(cid=None)
    device._interface.status.assert_not_awaited()
    device.status_updated.assert_not_called()


async def test_refresh_subdevice_uses_dp_query():
    device = create_device({**DEVICE_CONFIG, "node_id": "a4c138", "entities": []})

    await device._async_refresh(None)

    device._interface.status.assert_awaited_once_with(cid="a4c138")
    device._interface.update_dps.assert_not_awaited()
    device.status_updated.assert_called_once_with(DPS_STATUS)


async def test_refresh_sleeping_subdevice_keeps_update_dps():
    device = create_device(
        {
            **DEVICE_CONFIG,
            "node_id": "a4c138",
            "device_sleep_time": 600,
            "entities": [],
        }
    )

    await device._async_refresh(None)

    device._interface.update_dps.assert_awaited_once_with(cid="a4c138")
    device._interface.status.assert_not_awaited()


async def test_refresh_subdevice_timeout_is_ignored():
    device = create_device({**DEVICE_CONFIG, "node_id": "a4c138", "entities": []})
    device._interface.status = AsyncMock(side_effect=TimeoutError)

    await device._async_refresh(None)

    device.status_updated.assert_not_called()
