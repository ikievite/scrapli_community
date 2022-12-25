"""scrapli_community.dlink.os.sync_driver"""
from scrapli.driver import GenericDriver


def default_sync_on_open(conn: GenericDriver) -> None:
    """
    dlink_os on_open callable
    Args:
        conn: NetworkDriver object
    Returns:
        N/A
    Raises:
        N/A
    """
    conn.send_command(command="disable clipaging")


def default_sync_on_close(conn: GenericDriver) -> None:
    """
    dlink_os on_close callable
    Args:
        conn: NetworkDriver object
    Returns:
        N/A
    Raises:
        N/A
    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    conn.send_command(command="enable clipaging")
    conn.channel.write(channel_input="logout")
    conn.channel.send_return()
