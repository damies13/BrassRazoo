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