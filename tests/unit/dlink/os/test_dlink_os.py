import re

import pytest

from scrapli_community.dlink.os.dlink_os import SCRAPLI_PLATFORM


@pytest.mark.parametrize(
    "prompt",
    [
        "hostname:admin#",
        "DES-3200-28/ME:admin#",
        "DGS-3120-24TC:admin#",
    ],
)
def test_default_prompt_patterns(prompt):
    prompt_pattern = SCRAPLI_PLATFORM["defaults"]["comms_prompt_pattern"]
    match = re.search(pattern=prompt_pattern, string=prompt, flags=re.M | re.I)

    assert match
