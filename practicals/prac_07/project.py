

import datetime


class Project:
    """Represent a project with details like name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """
        Initialize a new Project instance.
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __repr__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%")

    def is_complete(self):
        """Return True if the project is complete (100%), otherwise False."""
        return self.percent_complete == 100

    def update(self, percent_complete=None, priority=None):
        """
        Update the project's completion percentage and priority.

        """
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if priority is not None:
            self.priority = priority

    def to_string(self):
        """Convert the Project instance to a tab-separated string."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.percent_complete}"


def project_from_string(project_string):
    """Create a Project instance from a string of tab-separated values."""
    name, start_date, priority, cost_estimate, percent_complete = project_string.split('\t')
    return Project(name, start_date, int(priority), float(cost_estimate), int(percent_complete))
