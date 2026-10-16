# Program 3.12: Combined DS Program (To-Do List with Set Tags)
# Build a to-do list using list for ordering and set for unique tags.
# Each task = {"task": string, "tags": set}
# Functions: add_task, display_all, find_by_tag.

todo_list = []

def add_task(task_name, tags):
    # tags converted to a set to guarantee uniqueness
    task_entry = {
        "task": task_name,
        "tags": set(tags)
    }
    todo_list.append(task_entry)
    print(f"Task added: '{task_name}' with tags {set(tags)}")

def display_all():
    print("\n--- ALL TO-DO TASKS ---")
    if not todo_list:
        print("No tasks in the list.")
        return
    for i, t in enumerate(todo_list, 1):
        print(f"{i}. {t['task']} [Tags: {', '.join(sorted(t['tags']))}]")

def find_by_tag(search_tag):
    print(f"\n--- Tasks with Tag: '{search_tag}' ---")
    found = False
    for t in todo_list:
        if search_tag in t["tags"]:
            print(f"- {t['task']}")
            found = True
    if not found:
        print(f"No task found with tag '{search_tag}'.")

# Demonstration
add_task("Submit Python Assignment", ["college", "urgent", "python"])
add_task("Buy groceries", ["personal", "shopping"])
add_task("Prepare for Mid Sem Exam", ["college", "study", "urgent"])

display_all()
find_by_tag("urgent")
find_by_tag("college")
