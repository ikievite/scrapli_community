"""scrapli_community.huawei.smartax.huawei_smartax"""
from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.huawei.smartax.async_driver import (
    AsyncHuaweiSmartAXDriver,
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.huawei.smartax.sync_driver import (
    HuaweiSmartAXDriver,
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\w\./-]{1,63}>\s?$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^(\S{1,48})#$",
            name="privilege_exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^(\S{1,48})\(config(\-\S+)+\)|\(config\)#$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="quit",
            escalate="enable",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": {
        "sync": HuaweiSmartAXDriver,
        "async": AsyncHuaweiSmartAXDriver,
    },
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Error:",
        ],
        "textfsm_platform": "huawei_vrp",
        "genie_platform": "",
        # Force the screen to be 256 characters wide.
        # Might get overwritten by global Scrapli transport options.
        # See issue #18 for more details.
        "transport_options": {"ptyprocess": {"cols": 256}},
    },
}
