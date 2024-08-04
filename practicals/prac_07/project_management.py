
import datetime
from project import Project, project_from_string

FILENAME = "projects.txt"

def main():
    """Manage projects."""
    projects = load_projects(FILENAME)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    running = True
    while running:
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = get_valid_input("Show projects that start after date (dd/mm/yyyy): ", str, is_valid_date,
                                          "Invalid date format, please use dd/mm/yyyy.")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            project = add_new_project()
            projects.append(project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input(f"Would you like to save to {FILENAME}? (yes/no): ").lower()
            if save == 'yes':
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            running = False
def sort_by_priority(project):
    """Return the priority of a project."""
    return project.priority

def sort_by_start_date(project):
    """Return the start date of a project."""
    return project.start_date

def valid_project_choice(index, projects):
    """Check if the given index is a valid project choice."""
    return 0 <= index < len(projects)

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            projects.append(project_from_string(line.strip()))
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("name\tstart_date\tpriority\tcost_estimate\tpercent_complete\n")
        for project in projects:
            file.write(project.to_string() + '\n')

def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=sort_by_priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete_projects, key=sort_by_priority):
        print(f"  {project}")

def filter_projects_by_date(projects, date):
    """Filter and display projects starting after a given date."""
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in sorted(filtered_projects, key=sort_by_start_date):
        print(f"  {project}")

def get_valid_input(prompt, input_type=str, validation_fn=None, error_message="Invalid input, please try again.",
                    allow_empty=False, default=None):
    """Get and validate user input."""
    user_input_valid = False
    while not user_input_valid:
        user_input = input(prompt)
        if user_input == "" and allow_empty:
            return default
        try:
            user_input = input_type(user_input)
            if validation_fn is None or validation_fn(user_input):
                user_input_valid = True
            else:
                print(error_message)
        except ValueError:
            print(error_message)
    return user_input

def is_valid_date(date_string):
    """Check if a date string is valid (format: dd/mm/yyyy)."""
    try:
        datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        return True
    except ValueError:
        return False

def is_non_negative(value):
    """Check if a value is non-negative (0 or greater)."""
    return value >= 0

def is_percentage(value):
    """Check if a value is a valid percentage (0-100)."""
    return 0 <= value <= 100

def add_new_project():
    """Prompt user to add a new project."""
    print("Let's add a new project")
    name = get_valid_input("Name: ", str, default="Untitled Project")
    start_date = get_valid_input("Start date (dd/mm/yyyy): ", str, is_valid_date,
                                 "Invalid date format, please use dd/mm/yyyy.", allow_empty=True, default="01/01/2000")
    priority = get_valid_input("Priority: ", int, is_non_negative, "Priority must be a positive integer.", allow_empty=True,
                               default=1)
    cost_estimate = get_valid_input("Cost estimate: $", float, is_non_negative, "Cost estimate must be a number.",
                                    allow_empty=True, default=0.0)
    percent_complete = get_valid_input("Percent complete: ", int, is_percentage,
                                       "Percentage must be between 0 and 100.", allow_empty=True, default=0)

    return Project(name, start_date, priority, cost_estimate, percent_complete)

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = get_valid_input("Project choice: ", int, validation_fn=lambda x: valid_project_choice(x, projects),
                                     error_message="Invalid project choice.")
    project = projects[project_choice]

    print(project)
    new_percent_complete = get_valid_input("New Percentage: ", int, is_percentage,
                                           "Percentage must be between 0 and 100.", allow_empty=True,
                                           default=project.percent_complete)
    new_priority = get_valid_input("New Priority: ", int, is_non_negative, "Priority must be a positive integer.",
                                   allow_empty=True, default=project.priority)

    project.update(new_percent_complete, new_priority)

if __name__ == "__main__":
    main()
