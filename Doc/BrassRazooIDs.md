
# Brass Razoo ID's

Brass Razoo ID's are generated using the following process:
- generate a [V1 UUID ](https://docs.python.org/3/library/uuid.html#uuid.uuid1)
- get the [integer value of the UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID.int)
- [Yeast Encode](https://github.com/unshiftio/yeast/blob/master/README.md) the integer, In python use [python-yeast](https://github.com/BroHui/python-yeast)

This gives the advantages of a standard UUID in a more compact form to make the data smaller
