"""scrapli_community.dlink.os.dlink_os"""
from scrapli_community.dlink.os.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.dlink.os.sync_driver import default_sync_on_close, default_sync_on_open

SCRAPLI_PLATFORM = {
    "driver_type": "generic",
    "defaults": {
        "comms_prompt_pattern": r"^[a-z0-9.\-_@/:]{1,63}#$",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Next possible completions:",
            "Available commands:",
        ],
    },
}
