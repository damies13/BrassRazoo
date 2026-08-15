# Brass Razoo Server

The Brass Razoo Server is written entirely in Python, ensuring it can operate across various operating systems and hardware setups. It runs efficiently, whether deployed on a low-power device like a Raspberry Pi or a high-performance Xeon server in a data centre.

## Initial Deployment

Upon its first run, the server will generate its configuration file. This file contains the server's unique ID—a Brass Razoo ID (see [BrassRazooIDs.md]). This Brass Razoo ID serves as the permanent identifier for the server.

## Hardware Migration and Identity Retention

If the server needs to be moved to new hardware, only the configuration file must be saved and migrated. The server will retain its original identity. It is essential to ensure the old server is completely shut down before starting the new instance, and that the old server cannot be restarted using its original Brass Razoo ID.

> [!WARNING] A robust method must be developed to detect duplicate servers and determine which server is the 'original' authority associated with a specific Brass Razoo ID.

## Staking Server Status

A Staking Server is defined as any server that has had a Brass Razoo stake allocated to it.

## Server Startup

On server startup, the server should verify every block in the chain for the shard it lives in, then it should pull all currently available block in the shard and verify them before becoming available for creating new blocks

This start up verificaton serves mulitple purposes:
- gives the server owner and stake holders confidence in the validity of the chain
- gives confidence to the chain that all servers agree on the chain being valid
- gives confidence to the chain that this server can create valid blocks

During start up verification if the server is not able to validate a Block of Truth, the server should shut down and report to the owner via the console which truth block validation failed.

If the server fails truth block validation on startup the server owner should roll back software versions until truth block validation succeeds, referring to the servers logs may be helpful in identifying what software has been updated recently and therefore what should be rolled back.

It's suggested to use stable releases of the servers operating system, python and Robot framework versions to avoid server outages.

## Blocks of Truth

- The first block in the Brass Razoo chain is the first block of truth
- As rules can not be applied to blocks before the rule existed, the block that introduced a new rule shall be the block of truth for that rule.

