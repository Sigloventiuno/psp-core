# PSP Core - Proof Of Service Protocol

> **PSP Core is a protocol implementation.**
> **It has no UX, no operator, and is not owned or donated by any entity.**

## Overview

PSP Core is the foundational layer of the Proof Of Service Protocol. It contains only pure protocol logic:

- **Genesis Block**: Immutable foundation with SHA-256 hash verification
- **Greek Wallets**: 8 distribution destinations (Athena, Hermes, Chronos, Prometheus, Apollo, Gaia, Zeus, Olympus)
- **Distribution Rules**: Exactly 7.500 PSP per validated service
- **Eternal Rules**: Immutable percentages for Zeus (1%) and Olympus (1%)

## Satoshi Principle

```
"Without verified physical work, there is no emission."
```

PSP tokens are only emitted when a service is:
1. Performed by a verified worker
2. Received by a verified client
3. Confirmed bilaterally by both parties
4. Recorded with cryptographic proof (PoServ Certificate)

## Distribution (7.500 PSP per service)

| Wallet | Amount | Percentage | Destination |
|--------|--------|------------|-------------|
| Athena | 2.000 | 26.67% | PSP Foundation |
| Hermes | 1.225 | 16.33% | Platform Operations |
| Chronos | 1.125 | 15.00% | Development Team |
| **Prometheus** | 1.000 | 13.33% | Worker (User) |
| **Apollo** | 1.000 | 13.33% | Client (User) |
| **Gaia** | 1.000 | 13.33% | Property NFT |
| Zeus | 0.075 | 1.00% | DAO (Immutable) |
| Olympus | 0.075 | 1.00% | Legal (Immutable) |

> **Note:** Percentages are protocol constants and cannot be modified without a fork.

## Gaia - Portable Protocol

Gaia's PSP goes **directly to the PropertyNFT**, not to the user:
- Property accumulates service history and PSP
- On property transfer, new owner inherits everything
- Creates verifiable "karma" for properties

## Example Usage

```python
from psp_core import (
    GENESIS_HASH,
    verify_genesis,
    distribute_for_service,
    get_distribution_summary
)

# Verify protocol integrity
result = verify_genesis()
print(f"Genesis Hash: {result['genesis_hash']}")

# Distribute PSP for a completed service
distribution = distribute_for_service(
    worker_id=123,
    client_id=456,
    property_id=789,
    certificate_id=1001,
    service_value_usd=150.00,
    dapp_origen='handyplan'
)
print(f"Total PSP: {distribution['total_psp']}")
print(f"Verified: {distribution['verified']}")
```

## What This Module Does NOT Contain

- ❌ User Interface (UX)
- ❌ Database connections
- ❌ API endpoints
- ❌ Authentication
- ❌ Business logic specific to any dApp
- ❌ Commercial features

## License

Apache License 2.0 - See [LICENSE](LICENSE) file.

## Principles

1. **Neutrality**: Protocol serves all dApps equally
2. **No Capture**: No entity owns or controls the protocol
3. **Transparency**: All rules are public and verifiable
4. **Immutability**: Core rules cannot be changed
5. **Determinism**: Same input always produces same output

---

> **This repository is intended to be consumed as a dependency, not as an application.**
