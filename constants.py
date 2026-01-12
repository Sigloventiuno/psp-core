# Copyright 2025 Proof Of Service Protocol
# Licensed under the Apache License, Version 2.0
# See LICENSE file for details.

"""
PSP Constants - Greek Wallets Configuration
============================================

Total per transaction: 7.500 PSP (exactly)

Distribution (Eternal Rule - Immutable):
- Zeus always receives 1% of 7.5 → Future DAO general
- Olympus always receives 1% of 7.5 → Community legal operations
- Nothing extra created - only classic 7.5 distributed
- All automatic, transparent and audited from day 1
"""

TOTAL_PSP_PER_TRANSACTION = 7.500

GREEK_WALLETS = {
    'athena': {
        'name': 'Athena',
        'role': 'foundation',
        'display_role': 'PSP Foundation',
        'psp_amount': 2.000,
        'percentage': 26.67,
        'description': 'Proof Of Service Protocol Foundation - Operational expenses',
        'destination_type': 'foundation',
        'immutable': False
    },
    'hermes': {
        'name': 'Hermes',
        'role': 'platform',
        'display_role': 'Platform Operations',
        'psp_amount': 1.225,
        'percentage': 16.33,
        'description': 'Platform operations and services',
        'destination_type': 'platform',
        'immutable': False
    },
    'chronos': {
        'name': 'Chronos',
        'role': 'development',
        'display_role': 'Development Team',
        'psp_amount': 1.125,
        'percentage': 15.00,
        'description': 'Development team rewards',
        'destination_type': 'developers',
        'immutable': False
    },
    'prometheus': {
        'name': 'Prometheus',
        'role': 'worker',
        'display_role': 'Worker/Technician',
        'psp_amount': 1.000,
        'percentage': 13.33,
        'description': 'Worker rewards for completed services',
        'destination_type': 'user',
        'immutable': False
    },
    'apollo': {
        'name': 'Apollo',
        'role': 'client',
        'display_role': 'Client',
        'psp_amount': 1.000,
        'percentage': 13.33,
        'description': 'Client rewards for confirmed services',
        'destination_type': 'user',
        'immutable': False
    },
    'gaia': {
        'name': 'Gaia',
        'role': 'property',
        'display_role': 'Property NFT',
        'psp_amount': 1.000,
        'percentage': 13.33,
        'description': 'Property NFT rewards - Portable Protocol',
        'destination_type': 'property_nft',
        'immutable': False,
        'special_rule': 'PSP goes directly to PropertyNFT, not to user. Transfers with property ownership.'
    },
    'zeus': {
        'name': 'Zeus',
        'role': 'dao',
        'display_role': 'DAO/Protocol',
        'psp_amount': 0.075,
        'percentage': 1.00,
        'description': 'Protocol DAO governance reserve - Immutable 1%',
        'destination_type': 'dao',
        'immutable': True
    },
    'olympus': {
        'name': 'Olympus',
        'role': 'legal',
        'display_role': 'Legal Operations',
        'psp_amount': 0.075,
        'percentage': 1.00,
        'description': 'Community legal operations - Immutable 1%',
        'destination_type': 'legal',
        'immutable': True
    }
}

WALLET_NAMES = list(GREEK_WALLETS.keys())

ETERNAL_RULES = {
    'zeus_percentage': 1.00,
    'olympus_percentage': 1.00,
    'total_psp_fixed': 7.500,
    'audited_from_day_1': True,
    'satoshi_principle': 'Without verified physical work, there is no emission.'
}

USER_WALLETS = ['prometheus', 'apollo']
PROPERTY_WALLETS = ['gaia']
SYSTEM_WALLETS = ['athena', 'hermes', 'chronos', 'zeus', 'olympus']
IMMUTABLE_WALLETS = ['zeus', 'olympus']


def validate_total() -> bool:
    """Validate that all wallet amounts sum to exactly 7.500 PSP."""
    total = sum(w['psp_amount'] for w in GREEK_WALLETS.values())
    return abs(total - TOTAL_PSP_PER_TRANSACTION) < 0.001


def get_wallet_by_role(role: str) -> dict:
    """Get wallet configuration by role name."""
    for name, config in GREEK_WALLETS.items():
        if config['role'] == role:
            return {'name': name, **config}
    return None
