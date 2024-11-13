## 1. Prompts Used

Try at least three variations and use the same final prompts for both Copilot and another LLM

```
a pyhton code that reflects Collaboration: 
As Code that reflects teamwork and collaboration, perhaps through functions that interact or share data.
```

## 2. Prompting Strategy

I tired to implment a zero-shot prompt when implementing this I used a meta-prompting to continues prompt and describe the project at hand. the first prompt was the prompt above I ended up adding more details to insure i was getting a desired output 
here is what I add to the exist prompt 

```
 This code is a simple example of a function that takes a list of numbers and returns the sum of the numbers in the list.
# explaination: On how it refects teamwork and collaboration
# This code reflects teamwork and collaboration by using a function to perform a specific task (calculating the sum of a list of numbers).
# The function can be reused by multiple team members in different parts of the code, allowing them to work together more efficiently.
# Additionally, the function can be easily modified or extended by team members to suit their needs, promoting collaboration and teamwork in the codebase.
# The code also demonstrates good coding practices such as using descriptive variable names and comments to make it more readable and maintainable for the team.
# Overall, this code exemplifies how collaboration and teamwork can lead to more effective and efficient code development.
```

## 3. Output Evaluation

This iteration allowed for better guidance for generating code that emphasizes collaborative work dynamics, such as class definitions for teams, assigning tasks, and promoting teamwork through well-commented and extendable functions.

### Copilot

- **Narrative Structure**:
  - The organization reflects the theme of collaboration by constructing a clear flow: setting up a team, creating tasks, assigning members, and completing the tasks. This approach mimics a real-world collaborative workflow and clearly depicts how each part of the project is connected.
  - The narrative resembles a story of a software development project, with different actors (classes) playing roles like team members, tasks, and team management. There is a clear progression from creating team members to completing tasks.

- **Commentary and Documentation**:
  - Copilot's comments and docstrings provide a meaningful narrative to explain each function's purpose. For example, each function has a brief description explaining what it does, such as `"Create a new task and add it to the task pool"` or `"Add a new team member to the team"`.
  - The commentary contributes to the narrative by giving context, but it could benefit from more detailed explanations, especially regarding the design rationale for managing task assignment and balancing collaboration.

- **Design Choices**:
  - The class and function names are descriptive, which enhances readability and the narrative quality of the code. Using names like `TeamMember`, `Task`, and `CollaborativeTeam` allows readers to understand each component's purpose intuitively.
  - The variable `available` used to indicate if a team member is available reflects a good collaborative design choice, enabling an easy way to determine suitable members for tasks.
  - The choice to include a **find_suitable_members** function emphasizes collaboration by matching the skills of team members to tasks. This adds depth to the teamwork narrative, showing that tasks are assigned thoughtfully.

### Other Single LLM

- **Narrative Structure**:
  - The structure followed a similar flow as Copilot's output, beginning with team formation, creating tasks, and eventually assigning and completing them.
  - The narrative lacked a bit of depth in emphasizing collaboration—task assignment wasn't always tied to a skill match, which detracted from the collaborative theme. Copilot's version did a better job of emphasizing how specific team members were suitable for specific tasks.

- **Commentary and Documentation**:
  - The comments were helpful in understanding the overall purpose of each function but were often less explicit about collaborative dynamics compared to Copilot.
  - For example, the **assign_task** function lacked detailed commentary on the significance of collaborators, which made the collaboration narrative less prominent.

- **Design Choices**:
  - Variable and class naming conventions were generally clear, but sometimes they were less descriptive compared to Copilot. Names like `assign` instead of `assign_task` made it less explicit what the function does.
  - The use of a simple assignment model (without considering skills or availability) detracted from the story of effective collaboration, making it feel more like random delegation rather than a deliberate teamwork exercise.

## 4. Reflection

The prompt iterations significantly impacted the narrative quality of the generated code. By adding more details to the prompt about the need to reflect teamwork and collaboration, Copilot was better able to generate code that captured the essence of a collaborative workflow. The inclusion of additional context, such as emphasizing skill matching and team member availability, helped in guiding the LLMs towards generating code that clearly portrayed teamwork.

Copilot’s suggestions generally supported the collaborative story within the code by using descriptive naming conventions, skill-matching logic, and thoughtful member assignment. The narrative felt well-structured, with comments providing helpful guidance throughout. However, the other LLM lacked some of these refined aspects—particularly in generating detailed logic for effective teamwork—indicating that prompt iterations and specificity can make a substantial difference in enhancing narrative quality.
