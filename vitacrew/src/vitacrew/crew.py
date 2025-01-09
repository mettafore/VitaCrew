from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Vitacrew():
    """Vitacrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def personal_trainer(self) -> Agent:
        return Agent(
            config=self.agents_config['personal_trainer'],
            verbose=True
        )

    @agent 
    def nutritionist(self) -> Agent:
        return Agent(
            config=self.agents_config['nutritionist'],
            verbose=True
        )

    @agent
    def beauty_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['beauty_specialist'],
            verbose=True
        )

    @agent
    def health_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['health_analyst'],
            verbose=True
        )

    @agent
    def design_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['design_specialist'],
            verbose=True
        )

    @task
    def analyze_fitness(self) -> Task:
        return Task(
            config=self.tasks_config['personal_trainer_tasks']['analyze_fitness']
        )

    @task
    def generate_workout(self) -> Task:
        return Task(
            config=self.tasks_config['personal_trainer_tasks']['generate_workout']
        )

    @task
    def create_meal_plan(self) -> Task:
        return Task(
            config=self.tasks_config['nutritionist_tasks']['create_meal_plan']
        )

    @task
    def generate_grocery_list(self) -> Task:
        return Task(
            config=self.tasks_config['nutritionist_tasks']['generate_grocery_list']
        )

    @task
    def assess_skin(self) -> Task:
        return Task(
            config=self.tasks_config['beauty_specialist_tasks']['assess_skin']
        )

    @task
    def design_routine(self) -> Task:
        return Task(
            config=self.tasks_config['beauty_specialist_tasks']['design_routine']
        )

    @task
    def analyze_data(self) -> Task:
        return Task(
            config=self.tasks_config['health_analyst_tasks']['analyze_data']
        )

    @task
    def generate_report(self) -> Task:
        return Task(
            config=self.tasks_config['health_analyst_tasks']['generate_report']
        )

    @task
    def format_plans(self) -> Task:
        return Task(
            config=self.tasks_config['design_specialist_tasks']['format_plans']
        )

    @task
    def create_visuals(self) -> Task:
        return Task(
            config=self.tasks_config['design_specialist_tasks']['create_visuals']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Vitacrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )