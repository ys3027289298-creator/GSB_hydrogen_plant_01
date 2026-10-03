import json


def new_game():
    return {'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'count': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_5(state):
    return state["queue"][0]

def bug_12(state):
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_19(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def bug_26(state):
    prev_end = None
    for _, (start, end) in sorted(state["events"].items()):
        if start >= end:
            return False
        if prev_end is not None and start < prev_end:
            return False
        prev_end = end
    return True

def bug_3(state):
    return state["queue"].pop(0)

def bug_10(state):
    delta = -5
    if delta < 0:
        return False
    state["amount"] += delta
    return True

def bug_17(state):
    amount = -10
    if amount <= 0:
        return False
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_24(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def bug_8(state):
    state["count"] = 0
    state["amount"] = 0
    return True

def bug_30(state):
    if any(entry[1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
