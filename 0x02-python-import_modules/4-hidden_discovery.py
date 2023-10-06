#!/usr/bin/python3

if __name__ == "__main__":
    """Print names as defined by hidden_4 modules."""
    import hidden_4

    modname = dir(hidden_4)
    for name in modname:
        if name[:2] != "__":
            print(name)
