# Program: Check Data Type and Perform Operations
# Check data type of given input and accordingly perform '+' and '*' operations.

def operate_by_type(val1, val2):
    print(f"val1: {val1} (type: {type(val1).__name__}) | val2: {val2} (type: {type(val2).__name__})")
    
    # '+' operation
    try:
        add_res = val1 + val2
        print("'+' Operation Result:", add_res)
    except Exception as e:
        print("'+' Operation not supported:", e)

    # '*' operation
    try:
        mul_res = val1 * val2
        print("'*' Operation Result:", mul_res)
    except Exception as e:
        print("'*' Operation not supported:", e)

print("--- Test 1: Integers ---")
operate_by_type(5, 3)

print("\n--- Test 2: Strings ---")
operate_by_type("Hello", "World")

print("\n--- Test 3: String and Integer ---")
operate_by_type("Python ", 3)
