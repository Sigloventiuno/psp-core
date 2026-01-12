# Copyright 2025 Proof Of Service Protocol
# Licensed under the Apache License, Version 2.0
# See LICENSE file for details.

"""
PSP Distribution - Token Emission Rules
========================================

This module contains the pure distribution logic for the PSP Protocol.
It has no dependencies on databases, frameworks, or UX components.

SATOSHI PRINCIPLE: Without verified physical work, there is no emission.
"""

from datetime import datetime, timezone
from typing import Optional
from .constants import GREEK_WALLETS, TOTAL_PSP_PER_TRANSACTION, ETERNAL_RULES


def distribute_classic_7_5() -> dict:
    """
    Execute the classic 7.5 PSP distribution to all wallets.
    This is the standard emission for each validated service.
    
    Returns:
        dict with emissions list, total, and verification status
    """
    emissions = []
    
    for wallet_name, config in GREEK_WALLETS.items():
        emissions.append({
            'wallet': wallet_name,
            'name': config['name'],
            'role': config['role'],
            'amount_psp': config['psp_amount'],
            'percentage': config['percentage'],
            'destination_type': config['destination_type']
        })
    
    total = sum(e['amount_psp'] for e in emissions)
    
    return {
        'emissions': emissions,
        'total_psp': total,
        'verified': abs(total - TOTAL_PSP_PER_TRANSACTION) < 0.001,
        'timestamp': datetime.now(timezone.utc).isoformat()
    }


def distribute_for_service(
    worker_id: int,
    client_id: int,
    property_id: Optional[int] = None,
    certificate_id: Optional[int] = None,
    service_value_usd: float = 0.0,
    dapp_origen: str = 'generic'
) -> dict:
    """
    Distribute 7.500 PSP for a validated service certificate.
    
    SATOSHI PRINCIPLE: Without verified physical work, there is no emission.
    
    Destinations:
    - Prometheus (1.000) → worker_id (User)
    - Apollo (1.000) → client_id (User)
    - Gaia (1.000) → property_id (PropertyNFT) - DIRECT TO PROPERTY
    - Athena (2.000) → PSP Foundation
    - Hermes (1.225) → Platform
    - Chronos (1.125) → Developers
    - Zeus (0.075) → DAO (Immutable 1%)
    - Olympus (0.075) → Legal (Immutable 1%)
    
    Args:
        worker_id: ID of the worker who performed the service
        client_id: ID of the client who received the service
        property_id: Optional ID of the PropertyNFT where service was performed
        certificate_id: Optional ID of the PoServ certificate
        service_value_usd: Value of the service in USD
        dapp_origen: Origin dApp identifier (e.g., 'handyplan', 'academia')
    
    Returns:
        dict with complete distribution details
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    
    emissions = [
        {
            'wallet': 'athena',
            'amount_psp': 2.000,
            'destination_type': 'foundation',
            'destination_id': None,
            'role': 'PSP Foundation'
        },
        {
            'wallet': 'hermes',
            'amount_psp': 1.225,
            'destination_type': 'platform',
            'destination_id': None,
            'role': 'Platform'
        },
        {
            'wallet': 'chronos',
            'amount_psp': 1.125,
            'destination_type': 'developers',
            'destination_id': None,
            'role': 'Developers'
        },
        {
            'wallet': 'prometheus',
            'amount_psp': 1.000,
            'destination_type': 'user',
            'destination_id': worker_id,
            'role': 'Worker'
        },
        {
            'wallet': 'apollo',
            'amount_psp': 1.000,
            'destination_type': 'user',
            'destination_id': client_id,
            'role': 'Client'
        },
        {
            'wallet': 'gaia',
            'amount_psp': 1.000,
            'destination_type': 'property_nft',
            'destination_id': property_id,
            'role': 'Property NFT'
        },
        {
            'wallet': 'zeus',
            'amount_psp': 0.075,
            'destination_type': 'dao',
            'destination_id': None,
            'role': 'DAO/Protocol'
        },
        {
            'wallet': 'olympus',
            'amount_psp': 0.075,
            'destination_type': 'legal',
            'destination_id': None,
            'role': 'Legal'
        }
    ]
    
    total = sum(e['amount_psp'] for e in emissions)
    
    return {
        'certificate_id': certificate_id,
        'timestamp': timestamp,
        'total_psp': total,
        'service_value_usd': service_value_usd,
        'dapp_origen': dapp_origen,
        'emissions': emissions,
        'verified': abs(total - TOTAL_PSP_PER_TRANSACTION) < 0.001,
        'eternal_rules_applied': {
            'zeus_1_percent': True,
            'olympus_1_percent': True,
            'satoshi_principle': True
        }
    }


def get_wallet_info(wallet_name: str) -> dict:
    """Get information about a specific wallet."""
    if wallet_name not in GREEK_WALLETS:
        return None
    return {'name': wallet_name, **GREEK_WALLETS[wallet_name]}


def get_all_wallets() -> dict:
    """Get all wallet configurations."""
    return GREEK_WALLETS.copy()


def get_distribution_summary() -> dict:
    """Get summary of the distribution configuration."""
    return {
        'protocol': 'PSP - Proof Of Service Protocol',
        'version': '1.0.0',
        'total_psp_per_transaction': TOTAL_PSP_PER_TRANSACTION,
        'wallet_count': len(GREEK_WALLETS),
        'wallets': list(GREEK_WALLETS.keys()),
        'eternal_rules': ETERNAL_RULES,
        'distribution': {
            name: {
                'psp': info['psp_amount'],
                'percentage': info['percentage'],
                'role': info['display_role']
            }
            for name, info in GREEK_WALLETS.items()
        },
        'user_destinations': ['prometheus', 'apollo'],
        'property_destination': 'gaia',
        'system_destinations': ['athena', 'hermes', 'chronos', 'zeus', 'olympus']
    }


def get_gaia_protocol() -> dict:
    """
    IMPORTANT: Gaia goes DIRECTLY to PropertyNFT.
    
    The PSP balance of Gaia belongs to the property,
    not to the user. When the property is transferred,
    the new owner inherits the history AND accumulated PSP.
    """
    return {
        'wallet': 'gaia',
        'psp_amount': 1.000,
        'destination_type': 'property_nft',
        'description': 'PSP accumulated in the property, not in the user',
        'on_transfer': 'PSP remains with the property',
        'portable': True
    }
