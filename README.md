![logo](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/logo-small.png)

# Local Tuya(Mod)

__A Home Assistant custom integration for local handling of Tuya-based devices.__

This is a modified fork of [hass-localtuya](https://github.com/xZetsubou/hass-localtuya) by xZetsubou, kept in step with current Home Assistant releases. In Home Assistant it shows up as **Local Tuya(Mod)**.

> [!IMPORTANT]
> Requires **Home Assistant 2026.11.0 or newer**. On older Home Assistant versions, use the [original integration](https://github.com/xZetsubou/hass-localtuya) instead.

## Differences from the original

- **Home Assistant 2026.11 compatibility**: follows the 2026.11 rules, including the ones Home Assistant only tolerates for custom integrations, and is ready for the device registry change in 2026.12.
- **Fixes from upstream pull requests** that the original hasn't merged yet:
  - number entities with scaling no longer get scaled again on every read;
  - the device registry always gets the protocol version as text.
- **Thread safety**: state updates and shutdown run on Home Assistant's event loop instead of worker threads.
- **Optional DP_QUERY refresh**, per device, for devices whose state stays stale because they ignore the periodic status request.
- **More auto-configure entities**:
  - presence sensors (`hps`): distance and illuminance sensors, hold time, delay, sensitivity and indicator;
  - sockets (`cz`/`pc`) with a night light: the night light and its countdown.

See the [releases](https://github.com/raphael1688dev/hass-localtuya/releases) for the full list of changes.

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?category=integration&repository=hass-localtuya&owner=raphael1688dev)

Or add it by hand: in HACS, open the ⋮ menu → **Custom repositories**, add `https://github.com/raphael1688dev/hass-localtuya` with the type **Integration**, then download **Local Tuya(Mod)** and restart Home Assistant.

### Switching from the original Local Tuya

This fork uses the same integration domain (`localtuya`), so your existing configuration, devices and entities are kept. Because of that, it can't be installed next to the original:

1. Make a backup of Home Assistant.
2. In HACS, remove the original **Local Tuya**. Don't delete the integration's entry under **Settings → Devices & services**.
3. Install **Local Tuya(Mod)** as above and restart Home Assistant.

## Usage and setup

The [documentation of the original integration](https://xzetsubou.github.io/hass-localtuya/) applies. Options added by this fork are described in this repository, for example [Refresh with DP_QUERY](https://github.com/raphael1688dev/hass-localtuya/blob/master/documentation/docs/usage/configure_add_device.md).

## Features

- Sub-devices: devices that work through a gateway.
- Remote entities: IR remotes through the native remote entity.
- Auto-configure devices: requires a cloud API setup.
- Automatic insertion: some fields require a cloud API setup.
- Device discovery: finds Tuya devices on your network.
- Cloud API: only helps you set up devices; the integration works without it.

## Reporting issues

Report problems with Local Tuya(Mod) in this repository's [issues](https://github.com/raphael1688dev/hass-localtuya/issues), not in the original repository. The original's [guide for reporting an issue](https://xzetsubou.github.io/hass-localtuya/report_issue/) explains how to collect debug logs and diagnostics.

<details><summary>Credits</summary>
<p>

[xZetsubou](https://github.com/xZetsubou), the maintainer of [hass-localtuya](https://github.com/xZetsubou/hass-localtuya), which this mod is based on.

[rospogrigio](https://github.com/rospogrigio), the original maintainer of LocalTuya. hass-localtuya was forked from the [original LocalTuya](https://github.com/rospogrigio/localtuya) at version `v5.2.1`.

[NameLessJedi](https://github.com/NameLessJedi/localtuya-homeassistant) and [mileperhour](https://github.com/mileperhour/localtuya-homeassistant), the major sources of inspiration, whose code for switches is substantially unchanged.

[TradeFace](https://github.com/TradeFace), for being the only one to provide the correct code for communication with the cover (in particular, the 0x0d command for the status instead of the 0x0a, and related needs such as double reply to be received).

sean6541, for the working (standard) Python Handler for Tuya devices.

[jasonacox](https://github.com/jasonacox), for the [TinyTuya](https://github.com/jasonacox/tinytuya) project, a major reference for the integration's protocol support.

[uzlonewolf](https://github.com/uzlonewolf), for maintaining TinyTuya, improving it a lot and adding features such as new protocols.

[postlund](https://github.com/postlund), for the ideas, for coding 95% of the refactoring and boosting the quality of the upstream repository.

</p>
</details>
