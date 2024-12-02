
# Action Engine

The action engine will be used for verifying and validating records or running tasks calculating the nominal value in various currencies.

## Robot Framework

The action engine will use [Robot Framework](https://robotframework.org/) to process the rules and tasks, however with limited libraries. each rule or task should be a self contained robot framework test / task and should contain all the keywords it needs that are not available from libraries


# Rule Actions

A rule will be used for validation of record, blocks etc

Rules will be triggered automatically by the server on receiving something, whether from another server or a client.

# Task Actions

A task will be used for periodic server actions

### Robot Framework Libraries

Rules will have access to the following libraries:
- Builtin libraries:
 - Builtin
 - Collections
 - DateTime
 - Dialogs
 - Libdoc
 - OperatingSystem
 - Process
 - Rebot
 - Remote
 - Screenshot
 - String
 - Telnet
 - Testdoc
 - Tidy
 - XML
- Requests Library
