#!/usr/bin/env python3
"""
Simple Text Adventure Game (pure Python, no libraries)

Save this file as adventure.py and run:
    python adventure.py
or
    python3 adventure.py

Commands: go <direction>, look, take <item>, use <item>, inventory, map, save, load, quit, help
"""

import sys

# ---------- Game Data ----------
VERSION = "1.0"

# Map of rooms. Each room: description, exits dict, items list, optional locked info, special actions
ROOMS = {
    "clearing": {
        "desc": "You are in a small clearing surrounded by dark trees. A path leads north into a ruined tower and south back to the village.",
        "exits": {"north": "tower_gate", "south": "village"},
        "items": ["note"]
    },
    "village": {
        "desc": "A quiet village with a single inn. The innkeeper eyes you suspiciously.",
        "exits": {"north": "clearing"},
        "items": ["apple"]
    },
    "tower_gate": {
        "desc": "A cracked stone gate blocks the tower entrance. There's a rusted keyhole and a faint inscription.",
        "exits": {"south": "clearing", "north": "tower_hall"},
        "items": [],
        "locked": True,        # requires 'silver_key' or solve puzzle
        "lock_note": "The gate is locked. The inscription reads: 'Speak the number of moons.'"
    },
    "tower_hall": {
        "desc": "A tall hall with a spiral staircase and portraits whose eyes seem to follow you.",
        "exits": {"south": "tower_gate", "up": "tower_top"},
        "items": ["silver_key", "lantern"]
    },
    "tower_top": {
        "desc": "At the very top you find a broken telescope pointed at the night sky and a chest.",
        "exits": {"down": "tower_hall"},
        "items": ["chest"],
        "chest_locked": True
    },
    "secret_room": {
        "desc": "A hidden room filled with strange runes and a glowing gem. You feel the air hum with power.",
        "exits": {"out": "tower_top"},
        "items": ["glowing_gem"]
    }
}

START_LOCATION = "village"
SAVE_FILE = "adventure_save.txt"

# ---------- Player State ----------
player = {
    "location": START_LOCATION,
    "inventory": [],
    "flags": {}  # for puzzles and state like 'lantern_lit': True
}

# ---------- Utility Functions ----------
def print_wrapped(text):
    print(text)

def show_help():
    print_wrapped("""
Available commands:
  go <direction>      - move north/south/east/west/up/down
  look                - examine current location
  inspect <object>    - inspect an item in the room or inventory
  take <item>         - pick up an item from the room
  drop <item>         - drop an item in the room
  use <item>          - use an item from your inventory
  inventory (i)       - show inventory
  map                 - show small map hint
  save                - save game to file
  load                - load game from file
  quit                - exit the game
  help                - show this help
Short forms: i for inventory, q for quit
""")

def get_room(name):
    return ROOMS.get(name)

def describe_location():
    loc = player["location"]
    room = get_room(loc)
    print_wrapped(f"\n-- {loc.upper()} --")
    print_wrapped(room["desc"])
    # list items
    if room.get("items"):
        visible = [it for it in room["items"] if it is not None]
        if visible:
            print_wrapped("You see: " + ", ".join(visible))
    # locked?
    if room.get("locked"):
        print_wrapped(room.get("lock_note", "It seems to be locked."))

def move(direction):
    loc = player["location"]
    room = get_room(loc)
    exits = room.get("exits", {})
    if direction in exits:
        target = exits[direction]
        # check locked on target (when approaching north into tower_hall we check tower_gate locked)
        # if moving into a room that is behind a locked object, handle locks
        # special case: moving north from clearing -> tower_gate has tower_gate locked
        target_room = get_room(target)
        if target_room and target_room.get("locked"):
            # check if player has silver_key
            if "silver_key" in player["inventory"]:
                print_wrapped("You use the silver key to unlock the gate.")
                target_room["locked"] = False
            else:
                print_wrapped(target_room.get("lock_note", "The way is blocked."))
                return
        player["location"] = target
        describe_location()
    else:
        print_wrapped("You can't go that way.")

# ---------- Item actions ----------
def take_item(item):
    room = get_room(player["location"])
    if item in (room.get("items") or []):
        player["inventory"].append(item)
        room["items"].remove(item)
        print_wrapped(f"You take the {item}.")
        # small special behavior
        if item == "apple":
            print_wrapped("It looks fresh. You could eat it with 'use apple'.")
    else:
        print_wrapped("There is no such item here.")

def drop_item(item):
    if item in player["inventory"]:
        player["inventory"].remove(item)
        get_room(player["location"])["items"].append(item)
        print_wrapped(f"You drop the {item}.")
    else:
        print_wrapped("You don't have that.")

def inspect_object(obj):
    # inspect items in room or inventory or objects like 'gate', 'chest'
    room = get_room(player["location"])
    if obj in player["inventory"]:
        if obj == "note":
            print_wrapped("The note reads: 'Three moons watched the tower fall.'")
        elif obj == "silver_key":
            print_wrapped("A small silver key with a star engraved on it.")
        elif obj == "apple":
            print_wrapped("A crisp red apple. Tasty.")
        elif obj == "lantern":
            print_wrapped("An old lantern. It might need lighting.")
        elif obj == "glowing_gem":
            print_wrapped("The gem hums softly. It warms your palm.")
        else:
            print_wrapped(f"It's a {obj}.")
        return
    # inspect room objects
    if obj == "gate" and "gate" in room.get("desc", "").lower() or obj == "gate":
        r = get_room("tower_gate")
        if r.get("locked"):
            print_wrapped(r.get("lock_note"))
        else:
            print_wrapped("The gate stands open.")
        return
    if obj == "chest" and "chest" in (room.get("items") or []):
        if room.get("chest_locked"):
            print_wrapped("The chest is locked and has a strange rune. Maybe the telescope or gem interacts.")
        else:
            print_wrapped("The chest is open. Inside you find a small paper with coordinates: 'secret at top when stars align.'")
        return
    print_wrapped("You don't see that here to inspect.")

def use_item(item):
    loc = player["location"]
    room = get_room(loc)
    if item not in player["inventory"]:
        print_wrapped("You don't have that item.")
        return
    # Using apple - eat
    if item == "apple":
        print_wrapped("You eat the apple. Restored your spirits.")
        player["inventory"].remove("apple")
        player["flags"]["ate_apple"] = True
        return
    # Use lantern
    if item == "lantern":
        if player["flags"].get("lantern_lit"):
            print_wrapped("The lantern is already lit.")
        else:
            print_wrapped("You rub the lantern and light a small wick. The lantern glows.")
            player["flags"]["lantern_lit"] = True
        return
    # Use silver_key optionally on chest/gate
    if item == "silver_key":
        # if at tower_gate, it will auto-unlock when moving, but allow using
        if loc == "tower_gate":
            r = get_room("tower_gate")
            if r.get("locked"):
                r["locked"] = False
                print_wrapped("You unlock the gate with the silver key.")
            else:
                print_wrapped("The gate is already unlocked.")
            return
        if loc == "tower_top":
            # try chest
            if get_room("tower_top").get("chest_locked"):
                get_room("tower_top")["chest_locked"] = False
                print_wrapped("You turn the key in the chest and it opens with a click.")
                # reveal a clue
                get_room("tower_top")["items"].append("paper")
            else:
                print_wrapped("The chest is already open.")
            return
        print_wrapped("You fiddle with the key, but nothing happens here.")
        return
    # Use glowing_gem
    if item == "glowing_gem":
        if loc == "tower_top":
            # open secret room
            print_wrapped("As you hold the gem near the broken telescope, a hidden hatch slides open revealing a secret stair.")
            # connect secret room
            get_room("tower_top")["exits"]["down_secret"] = "secret_room"
            # move player optionally
            return
        else:
            print_wrapped("The gem vibrates but nothing else happens.")
            return
    # Use paper
    if item == "paper":
        print_wrapped("The paper has a scribble: 'When three moons are counted, the gate will open.'")
        return
    print_wrapped("Using that does nothing obvious.")

# ---------- Parsing & Commands ----------
def parse_command(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    parts = cmd.split()
    verb = parts[0].lower()

    if verb in ("q", "quit", "exit"):
        print_wrapped("Thanks for playing. Goodbye.")
        sys.exit(0)
    elif verb in ("help", "?"):
        show_help()
    elif verb in ("look", "l"):
        describe_location()
    elif verb in ("i", "inventory"):
        if player["inventory"]:
            print_wrapped("You carry: " + ", ".join(player["inventory"]))
        else:
            print_wrapped("You carry nothing.")
    elif verb == "map":
        show_map_hint()
    elif verb == "go" and len(parts) >= 2:
        move(parts[1].lower())
    elif verb in ("north","south","east","west","up","down") and len(parts) == 1:
        move(verb)
    elif verb == "take" and len(parts) >= 2:
        take_item(" ".join(parts[1:]))
    elif verb == "drop" and len(parts) >= 2:
        drop_item(" ".join(parts[1:]))
    elif verb == "inspect" and len(parts) >= 2:
        inspect_object(" ".join(parts[1:]))
    elif verb == "use" and len(parts) >= 2:
        use_item(" ".join(parts[1:]))
    elif verb == "save":
        save_game()
    elif verb == "load":
        load_game()
    else:
        print_wrapped("I don't understand that. Type 'help' for commands.")

# ---------- Map & Hints ----------
def show_map_hint():
    print_wrapped("""
Map hint:
   [village] <-> [clearing] <-> [tower_gate] <-> [tower_hall] <-> [tower_top]
                               (secret hidden under tower_top)
""")

# ---------- Save / Load ----------
def save_game():
    try:
        with open(SAVE_FILE, "w") as f:
            # simple format: location|comma separated inventory|flags as key=val semicolon
            inv = ",".join(player["inventory"])
            flags = ";".join(f"{k}={v}" for k, v in player["flags"].items())
            f.write("|".join([player["location"], inv, flags]))
        print_wrapped(f"Game saved to {SAVE_FILE}.")
    except Exception as e:
        print_wrapped("Failed to save: " + str(e))

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = f.read().split("|")
            if len(data) >= 1:
                player["location"] = data[0] or START_LOCATION
            if len(data) >= 2:
                player["inventory"] = data[1].split(",") if data[1] else []
            if len(data) >= 3:
                flags = {}
                for pair in data[2].split(";"):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        # Rudimentary bool/int parsing
                        if v.lower() in ("true","false"):
                            flags[k] = v.lower() == "true"
                        else:
                            try:
                                flags[k] = int(v)
                            except:
                                flags[k] = v
                player["flags"] = flags
        print_wrapped("Game loaded.")
        describe_location()
    except FileNotFoundError:
        print_wrapped("No save file found.")
    except Exception as e:
        print_wrapped("Failed to load: " + str(e))

# ---------- Game Setup & Intro ----------
def start_game():
    print_wrapped("Welcome to 'Moonlight Ruins' — a tiny text adventure.")
    print_wrapped("Type 'help' for commands. Save with 'save', load with 'load'.")
    describe_location()
    # small demo hint
    if "note" in get_room("clearing").get("items", []):
        pass

# ---------- Main Loop ----------
def main_loop():
    start_game()
    while True:
        try:
            cmd = input("\n> ")
        except (EOFError, KeyboardInterrupt):
            print_wrapped("\nGoodbye.")
            break
        parse_command(cmd)
        # check for a win condition: player has glowing_gem and returns to village
        if "glowing_gem" in player["inventory"] and player["location"] == "village":
            print_wrapped("\nAs you step into the village holding the glowing gem, people gather in awe.")
            print_wrapped("You have returned with the ancient gem — the village is saved. YOU WIN!")
            break

if __name__ == "__main__":
    main_loop()