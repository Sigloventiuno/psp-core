# Copyright 2025 Proof Of Service Protocol
# Licensed under the Apache License, Version 2.0
# See LICENSE file for details.

"""
PSP Genesis Block
=================

The genesis block is the foundation of the PSP Protocol.
It is immutable and defines the initial state of the system.

PRINCIPLE: Without verified physical work, there is no emission.
"""

import hashlib
from datetime import datetime

GENESIS_BLOCK = {
    "block_number": 0,
    "version": "1.0.0",
    "timestamp": "2025-12-01T00:00:00Z",
    "previous_hash": "0" * 64,
    "protocol": "Proof Of Service Protocol",
    "total_psp_per_transaction": 7.500,
    "message": "SmartWork Always Leads To Greatness",
    "principles": [
        "Radical Trust",
        "Total Transparency", 
        "Real Utility",
        "Shared Responsibility",
        "Progressive Inclusion",
        "Respect for Time and Effort"
    ],
    "satoshi_legacy": "Without verified physical work, there is no emission.",
    "wallets": [
        "athena",
        "hermes", 
        "chronos",
        "prometheus",
        "apollo",
        "gaia",
        "zeus",
        "olympus"
    ],
    "immutable_rules": {
        "zeus_percentage": 1.00,
        "olympus_percentage": 1.00,
        "total_psp_fixed": 7.500
    }
}


def _compute_genesis_hash() -> str:
    """
    Compute the SHA-256 hash of the genesis block.
    This hash is deterministic and immutable.
    """
    genesis_string = (
        f"block:{GENESIS_BLOCK['block_number']}|"
        f"version:{GENESIS_BLOCK['version']}|"
        f"timestamp:{GENESIS_BLOCK['timestamp']}|"
        f"protocol:{GENESIS_BLOCK['protocol']}|"
        f"psp:{GENESIS_BLOCK['total_psp_per_transaction']}|"
        f"message:{GENESIS_BLOCK['message']}|"
        f"satoshi:{GENESIS_BLOCK['satoshi_legacy']}|"
        f"wallets:{','.join(GENESIS_BLOCK['wallets'])}|"
        f"zeus:{GENESIS_BLOCK['immutable_rules']['zeus_percentage']}|"
        f"olympus:{GENESIS_BLOCK['immutable_rules']['olympus_percentage']}"
    )
    return hashlib.sha256(genesis_string.encode('utf-8')).hexdigest()


GENESIS_HASH = _compute_genesis_hash()


def verify_genesis(provided_hash: str = None) -> dict:
    """
    Verify the integrity of the genesis block.
    
    Args:
        provided_hash: Optional hash to verify against
        
    Returns:
        dict with verification result
    """
    computed = _compute_genesis_hash()
    
    result = {
        "genesis_hash": computed,
        "block_number": 0,
        "timestamp": GENESIS_BLOCK['timestamp'],
        "protocol_version": GENESIS_BLOCK['version'],
        "total_psp": GENESIS_BLOCK['total_psp_per_transaction'],
        "wallet_count": len(GENESIS_BLOCK['wallets']),
        "verified": True
    }
    
    if provided_hash:
        result['provided_hash'] = provided_hash
        result['matches'] = (computed == provided_hash)
        result['verified'] = result['matches']
    
    return result


def get_genesis_info() -> dict:
    """Get public information about the genesis block."""
    return {
        "hash": GENESIS_HASH,
        "block_number": 0,
        "timestamp": GENESIS_BLOCK['timestamp'],
        "message": GENESIS_BLOCK['message'],
        "principles": GENESIS_BLOCK['principles'],
        "satoshi_legacy": GENESIS_BLOCK['satoshi_legacy'],
        "total_psp_per_transaction": GENESIS_BLOCK['total_psp_per_transaction']
    }
