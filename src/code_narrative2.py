from datetime import datetime, timedelta
from typing import List, Dict, Optional

class TeamMember:
    def __init__(self, name: str, role: str, skills: List[str]):
        self.name = name
        self.role = role
        self.skills = skills
        self.current_task = None
        self.completed_tasks = []
        self.available = True

class Task:
    def __init__(self, title: str, description: str, required_skills: List[str], 
                 estimated_hours: int):
        self.title = title
        self.description = description
        self.required_skills = required_skills
        self.estimated_hours = estimated_hours
        self.status = "Not Started"
        self.assigned_to = None
        self.created_at = datetime.now()
        self.completed_at = None
        self.collaborators = []

class CollaborativeTeam:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.members = []
        self.tasks = []
        self.completed_projects = []
    
    def add_team_member(self, member: TeamMember) -> None:
        """Add a new team member to the team."""
        self.members.append(member)
        print(f"Welcome {member.name} ({member.role}) to {self.team_name}!")

    def create_task(self, task: Task) -> None:
        """Create a new task and add it to the task pool."""
        self.tasks.append(task)
        print(f"New task created: {task.title}")
        
        # Find suitable team members for the task
        potential_assignees = self.find_suitable_members(task)
        if potential_assignees:
            print("Suggested team members for this task:")
            for member in potential_assignees:
                print(f"- {member.name} ({member.role})")

    def find_suitable_members(self, task: Task) -> List[TeamMember]:
        """Find team members with matching skills for a task."""
        suitable_members = []
        for member in self.members:
            if member.available and any(skill in member.skills for skill in task.required_skills):
                suitable_members.append(member)
        return suitable_members

    def assign_task(self, task: Task, primary_assignee: TeamMember, 
                   collaborators: List[TeamMember] = None) -> None:
        """Assign a task to a team member and optional collaborators."""
        if task in self.tasks and primary_assignee in self.members:
            task.assigned_to = primary_assignee
            task.status = "In Progress"
            primary_assignee.current_task = task
            primary_assignee.available = False
            
            if collaborators:
                task.collaborators = collaborators
                print(f"Task '{task.title}' assigned to {primary_assignee.name} with collaborators: "
                      f"{', '.join(c.name for c in collaborators)}")
            else:
                print(f"Task '{task.title}' assigned to {primary_assignee.name}")

    def complete_task(self, task: Task) -> None:
        """Mark a task as completed and update team member status."""
        if task in self.tasks:
            task.status = "Completed"
            task.completed_at = datetime.now()
            
            # Update primary assignee status
            if task.assigned_to:
                task.assigned_to.completed_tasks.append(task)
                task.assigned_to.current_task = None
                task.assigned_to.available = True
            
            # Move task to completed projects
            self.completed_projects.append(task)
            self.tasks.remove(task)
            
            print(f"Task '{task.title}' completed successfully!")
            self.generate_task_report(task)

    def generate_task_report(self, task: Task) -> None:
        """Generate a report for a completed task."""
        duration = task.completed_at - task.created_at
        print("\nTask Completion Report:")
        print(f"Title: {task.title}")
        print(f"Led by: {task.assigned_to.name}")
        if task.collaborators:
            print(f"Collaborators: {', '.join(c.name for c in task.collaborators)}")
        print(f"Duration: {duration.days} days, {duration.seconds // 3600} hours")
        print(f"Status: {task.status}")

# Example Usage
if __name__ == "__main__":
    # Create a new team
    dev_team = CollaborativeTeam("Innovation Squad")
    
    # Create team members with different skills
    alice = TeamMember("Alice", "Frontend Developer", ["JavaScript", "React", "CSS"])
    bob = TeamMember("Bob", "Backend Developer", ["Python", "Django", "SQL"])
    carol = TeamMember("Carol", "Full Stack Developer", ["Python", "React", "DevOps"])
    
    # Add members to the team
    for member in [alice, bob, carol]:
        dev_team.create_task(member)
    
    # Create a new collaborative task
    new_feature = Task(
        title="Implement User Authentication",
        description="Create a secure user authentication system with OAuth support",
        required_skills=["Python", "React", "Security"],
        estimated_hours=20
    )
    
    # Create and assign the task
    dev_team.create_task(new_feature)
    dev_team.assign_task(new_feature, carol, collaborators=[alice, bob])
    
    # Complete the task
    dev_team.complete_task(new_feature)
