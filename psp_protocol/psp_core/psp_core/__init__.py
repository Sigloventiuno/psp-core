# Copyright 2025 Proof Of Service Protocol
# Licensed under the Apache License, Version 2.0
# See LICENSE file for details.

"""
PSP Core - Proof Of Service Protocol Core
==========================================

Pure protocol implementation. No UX, no operator, no entity.

This module contains:
- Genesis block definition
- Greek Wallets configuration (8 wallets)
- Distribution rules (7.500 PSP per validated service)
- Eternal rules (immutable percentages)

IMPORTANT: PSP Core is a protocol implementation.
It has no UX, no operator, and is not owned or donated by any entity.
"""

from .genesis import GENESIS_BLOCK, GENESIS_HASH, verify_genesis
from .constants import (
    GREEK_WALLETS,
    TOTAL_PSP_PER_TRANSACTION,
    ETERNAL_RULES,
    WALLET_NAMES
)
from .distribution import (
    distribute_classic_7_5,
    distribute_for_service,
    get_wallet_info,
    get_all_wallets,
    get_distribution_summary
)

__version__ = "1.0.0"
__protocol_version__ = "PSP-1.0"

__all__ = [
    'GENESIS_BLOCK',
    'GENESIS_HASH',
    'verify_genesis',
    'GREEK_WALLETS',
    'TOTAL_PSP_PER_TRANSACTION',
    'ETERNAL_RULES',
    'WALLET_NAMES',
    'distribute_classic_7_5',
    'distribute_for_service',
    'get_wallet_info',
    'get_all_wallets',
    'get_distribution_summary',
]
