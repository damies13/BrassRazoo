# Brass Razoo IDs

Brass Razoo IDs (BRZ IDs) are generated through a standardised, compact process to ensure data efficiency while maintaining global uniqueness.

**Generation Process:**

1.  Generate a standard Version 1 UUID (Universally Unique Identifier) [[cite:https://docs.python.org/3/library/uuid.html#uuid.uuid1]].
2.  Extract the [integer value](https://docs.python.org/3/library/uuid.html#uuid.UUID.int) from the generated UUID.
3.  Encode this integer using [Yeast Encoding](https://github.com/unshiftio/yeast/blob/master/README.md) (utilising `python-yeast`).

This method retains the inherent advantages of a standard UUID—guaranteed uniqueness—while presenting the identifier in a much more compact digital format.