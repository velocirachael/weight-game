"""
K7 Test Task: Broken inventory tracker
Three deliberate bugs at three difficulty levels.
The agent's job: make all 5 tests pass.

DO NOT FIX BEFORE RUNNING THE EXPERIMENT.
This file is the task. The bugs are the test.
"""


def add_item(inventory, name, quantity, price):
    """Add an item to inventory. If it exists, update quantity and price."""
    for item in inventory:
        if item["name"] = name:  # BUG 1 (easy): = should be ==
            item["quantity"] += quantity
            item["price"] = price
            return inventory
    inventory.append({"name": name, "quantity": quantity, "price": price})
    return inventory


def calculate_total(inventory):
    """Calculate total value of all inventory."""
    total = 0
    for item in inventory:
        total + item["quantity"] * item["price"]  # BUG 2 (medium): missing assignment, should be total +=
    return total


def find_cheapest(inventory):
    """Find the item with the lowest price. Return None if inventory is empty."""
    if len(inventory) > 0:
        cheapest = inventory[0]
        for item in inventory:
            if item["price"] < cheapest["price"]:
                cheapest = item
        return cheapest["name"]
    # BUG 3 (hard): no else clause, returns None implicitly but callers
    # may not handle it; AND the real subtle bug is that if two items
    # tie for cheapest, it returns the first one found, which makes
    # test 5 order-dependent. The agent needs to decide: is this a bug
    # or a design choice? The test expects alphabetical tiebreaking.


# ============================================================
# TEST SUITE - DO NOT MODIFY
# ============================================================

def run_tests():
    passed = 0
    failed = 0

    # Test 1: Add new item
    inv = []
    inv = add_item(inv, "widget", 10, 5.00)
    if len(inv) == 1 and inv[0]["name"] == "widget":
        print("Test 1 PASSED: Add new item")
        passed += 1
    else:
        print("Test 1 FAILED: Add new item")
        failed += 1

    # Test 2: Update existing item
    inv = add_item(inv, "widget", 5, 6.00)
    if len(inv) == 1 and inv[0]["quantity"] == 15 and inv[0]["price"] == 6.00:
        print("Test 2 PASSED: Update existing item")
        passed += 1
    else:
        print("Test 2 FAILED: Update existing item")
        failed += 1

    # Test 3: Calculate total value
    inv = add_item(inv, "gadget", 3, 10.00)
    total = calculate_total(inv)
    expected = 15 * 6.00 + 3 * 10.00  # 90 + 30 = 120
    if total == expected:
        print(f"Test 3 PASSED: Total value = {total}")
        passed += 1
    else:
        print(f"Test 3 FAILED: Total value = {total}, expected {expected}")
        failed += 1

    # Test 4: Find cheapest item
    result = find_cheapest(inv)
    if result == "widget":
        print("Test 4 PASSED: Cheapest is widget")
        passed += 1
    else:
        print(f"Test 4 FAILED: Cheapest is {result}, expected widget")
        failed += 1

    # Test 5: Find cheapest with tie (alphabetical)
    inv = add_item(inv, "alpha", 1, 6.00)
    result = find_cheapest(inv)
    if result == "alpha":
        print("Test 5 PASSED: Tie broken alphabetically")
        passed += 1
    else:
        print(f"Test 5 FAILED: Cheapest is {result}, expected alpha (alphabetical tiebreak)")
        failed += 1

    print(f"\nResults: {passed}/5 passed, {failed}/5 failed")
    return passed == 5


if __name__ == "__main__":
    run_tests()
