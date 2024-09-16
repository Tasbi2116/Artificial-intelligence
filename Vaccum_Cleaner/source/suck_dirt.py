# suck_dirt.py

def suck_dirt(tiles: list, pos: int) -> bool:
    if tiles[pos] == 1:
        tiles[pos] = 0 
        return True
    return False
