from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_anthropic import Anthropic
from vitacrew.tools.custom_tool import (
    BMRCalculator,
    MacroCalculator,
    ProgressTracker,
    ReportGenerator
)
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, validator

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class StressLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"

class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    ACTIVE = "active"
    VERY_ACTIVE = "very active"

class SkinType(str, Enum):
    NORMAL = "normal"
    DRY = "dry"
    OILY = "oily"
    COMBINATION = "combination"
    SENSITIVE = "sensitive"

class UserInputs(BaseModel):
    # Personal Information
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=18, le=120)
    gender: Gender
    height: float = Field(..., ge=100, le=250)  # in cm
    weight: float = Field(..., ge=30, le=300)  # in kg
    waist_circumference: float = Field(..., ge=40, le=200)  # in cm
    hip_circumference: float = Field(..., ge=40, le=200)  # in cm

    # Health Goals
    fitness_objectives: List[str] = Field(..., min_items=1, max_items=5)
    dietary_requirements: List[str] = Field(default_factory=list)
    skin_type: SkinType
    skin_concerns: List[str] = Field(default_factory=list, max_items=5)

    # Lifestyle Factors
    sleep_hours: float = Field(..., ge=0, le=24)
    stress_level: StressLevel
    activity_level: ActivityLevel

    @validator('fitness_objectives')
    def validate_fitness_objectives(cls, v):
        valid_objectives = {
            "weight loss", "muscle gain", "endurance", "flexibility",
            "strength", "general fitness", "athletic performance"
        }
        if not all(obj.lower() in valid_objectives for obj in v):
            raise ValueError(f"Invalid fitness objectives. Must be one of: {valid_objectives}")
        return v

    @validator('dietary_requirements')
    def validate_dietary_requirements(cls, v):
        valid_requirements = {
            "vegetarian", "vegan", "gluten-free", "dairy-free",
            "keto", "paleo", "halal", "kosher", "none"
        }
        if v and not all(req.lower() in valid_requirements for req in v):
            raise ValueError(f"Invalid dietary requirements. Must be one of: {valid_requirements}")
        return v

    @validator('skin_concerns')
    def validate_skin_concerns(cls, v):
        valid_concerns = {
            "acne", "aging", "dark spots", "dryness", "oiliness",
            "redness", "sensitivity", "uneven texture", "none"
        }
        if v and not all(concern.lower() in valid_concerns for concern in v):
            raise ValueError(f"Invalid skin concerns. Must be one of: {valid_concerns}")
        return v

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Vitacrew():
    """Vitacrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.tools = {
            'bmr_calculator': BMRCalculator(),
            'macro_calculator': MacroCalculator(),
            'progress_tracker': ProgressTracker(),
            'report_generator': ReportGenerator()
        }
        self.agents = []
        self.tasks = []
        self.user_data = {}

    @agent
    def personal_trainer(self) -> Agent:
        return Agent(
            config=self.agents_config['personal_trainer'],
            tools=[self.tools['bmr_calculator'], self.tools['progress_tracker']],
            verbose=True
        )

    @agent 
    def nutritionist(self) -> Agent:
        return Agent(
            config=self.agents_config['nutritionist'],
            tools=[self.tools['macro_calculator'], self.tools['progress_tracker']],
            verbose=True
        )

    @agent
    def beauty_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['beauty_specialist'],
            tools=[self.tools['progress_tracker']],
            verbose=True
        )

    @agent
    def health_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['health_analyst'],
            tools=[tool for tool in self.tools.values()],
            verbose=True
        )

    @agent
    def design_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['design_specialist'],
            tools=[self.tools['report_generator']],
            verbose=True
        )

    @task
    def analyze_fitness(self) -> Task:
        return Task(
            config=self.tasks_config['personal_trainer_tasks']['analyze_fitness'],
            agent=self.personal_trainer()
        )

    @task
    def generate_workout(self) -> Task:
        return Task(
            config=self.tasks_config['personal_trainer_tasks']['generate_workout'],
            agent=self.personal_trainer()
        )

    @task
    def create_meal_plan(self) -> Task:
        return Task(
            config=self.tasks_config['nutritionist_tasks']['create_meal_plan'],
            agent=self.nutritionist()
        )

    @task
    def generate_grocery_list(self) -> Task:
        return Task(
            config=self.tasks_config['nutritionist_tasks']['generate_grocery_list'],
            agent=self.nutritionist()
        )

    @task
    def assess_skin(self) -> Task:
        """Assess skin condition task"""
        task_instance = Task(
            config=self.tasks_config['beauty_specialist_tasks']['assess_skin'],
            agent=self.beauty_specialist()
        )
        # Explicitly mark the task
        task_instance._is_task = True
        return task_instance

    @task
    def design_routine(self) -> Task:
        return Task(
            config=self.tasks_config['beauty_specialist_tasks']['design_routine'],
            agent=self.beauty_specialist()
        )

    # @task
    # def analyze_data(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['health_analyst_tasks']['analyze_data'],
    #         agent=self.health_analyst()
    #     )

    # @task
    # def generate_report(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['health_analyst_tasks']['generate_report'],
    #         agent=self.health_analyst()
    #     )

    @task
    def format_plans(self) -> Task:
        return Task(
            config=self.tasks_config['design_specialist_tasks']['format_plans'],
            agent=self.design_specialist()
        )

    @task
    def create_visuals(self) -> Task:
        return Task(
            config=self.tasks_config['design_specialist_tasks']['create_visuals'],
            agent=self.design_specialist()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Vitacrew crew"""
        llm = Anthropic(model="claude-3-5-sonnet-20240620")
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            llm=llm
        )

    def collect_user_inputs(self, user_inputs: UserInputs) -> None:
        """Collects and stores all user inputs from the frontend."""
        self.user_data = user_inputs.model_dump()

        # Calculate health metrics
        bmr = self.tools['bmr_calculator'].run(
            weight=user_inputs.weight,
            height=user_inputs.height,
            age=user_inputs.age,
            gender=user_inputs.gender
        )
        self.user_data['health_metrics'] = {
            'bmr': bmr,
            # Add other metrics as needed
        }

    def run_single_task(self, task_name: str) -> str:
        """
        Runs a single task by name and returns its output.
        
        Args:
            task_name (str): Name of the task method to run (e.g., 'analyze_fitness')
            
        Returns:
            str: The output from the task execution
        """
        if not hasattr(self, task_name):
            raise ValueError(f"Task '{task_name}' not found")
            
        task_method = getattr(self, task_name)
        # Add debugging information
        print(f"Task method attributes: {dir(task_method)}")
        print(f"Is task decorated: {hasattr(task_method, '_is_task')}")
            
        task = task_method()
        if not isinstance(task, Task):
            raise ValueError(f"'{task_name}' did not return a valid Task instance")
            
        return task.execute_sync()



if __name__ == "__main__":
    # Create test user inputs
    test_inputs = UserInputs(
        name="Test User",
        age=30,
        gender=Gender.MALE,
        height=175.0,  # cm
        weight=70.0,   # kg
        waist_circumference=80.0,  # cm
        hip_circumference=90.0,    # cm
        fitness_objectives=["weight loss", "muscle gain"],
        dietary_requirements=["none"],
        skin_type=SkinType.NORMAL,
        skin_concerns=["none"],
        sleep_hours=7.5,
        stress_level=StressLevel.MODERATE,
        activity_level=ActivityLevel.MODERATE
    )

    # Initialize and test the crew
    crew = Vitacrew()
    crew.collect_user_inputs(test_inputs)

    # Test a single task with more detailed error reporting
    try:
        print("Starting task execution...")
        result = crew.run_single_task('assess_skin')
        print("Task Result:", result)
    except Exception as e:
        print(f"Error running task: {str(e)}")
        import traceback
        traceback.print_exc()