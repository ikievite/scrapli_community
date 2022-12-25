"""scrapli_community.dlink.os.async_driver"""
from scrapli.driver import AsyncGenericDriver


async def default_async_on_open(conn: AsyncGenericDriver) -> None:
    """
    Async scrapli_example default on_open callable
    Args:
        conn: AsyncNetworkDriver object
    Returns:
        N/A
    Raises:
        N/A
    """
    await conn.send_command(command="disable clipaging")


async def default_async_on_close(conn: AsyncGenericDriver) -> None:
    """
    Async scrapli_example default on_close callable
    Args:
        conn: AsyncNetworkDriver object
    Returns:
        N/A
    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    await conn.send_command(command="enable clipaging")
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
