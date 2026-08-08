# Core Concepts

## Proof of Stake (PoS)

In contrast to Proof of Work (PoW) systems like Bitcoin and Ethereum (which become computationally intensive as the algorithm difficulty increases), Brass Razoo utilises a Proof of Stake model. PoS addresses the environmental concerns and sustainability issues often criticised in PoW systems.

In this model, coin owners stake their holdings with a server. A server possessing one or more stakes is selected to generate the next block. Stake holders are rewarded with a commission on the block as compensation for locking up and guaranteeing the records within the block.

The PoS design allows the system to run efficiently, as each server only requires a minimal amount of computational power. This means small, low-power Single Board Computers (SBCs), such as a Raspberry Pi or a RISC-V equivalent, can operate as a Brass Razoo server using a battery and a small solar panel.

## Records

A record is a digital asset that can represent virtually any transaction or entity, including:

*   A sale or transfer of goods.
*   An employment contract.
*   A user account or identity.
*   The registration of an artwork.
*   A defined system rule.

Specific rules exist to verify each type of record (see [Action Engine](Action_Engine.md)). The intention is that these rules are created and voted upon within the chain; once approved, the rules are enforced to ensure the correct creation and integrity of all records.