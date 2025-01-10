import pytest
from unittest.mock import Mock, patch
from ..crew import Vitacrew, UserInputs, Gender, StressLevel, ActivityLevel, SkinType

@pytest.fixture
def vitacrew():
    return Vitacrew()

@pytest.fixture
def mock_user_inputs():
    return UserInputs(
        name="Test User",
        age=30,
        gender=Gender.MALE,
        height=175.0,
        weight=70.0,
        waist_circumference=80.0,
        hip_circumference=90.0,
        fitness_objectives=["weight loss", "muscle gain"],
        dietary_requirements=["vegetarian"],
        skin_type=SkinType.NORMAL,
        skin_concerns=["acne"],
        sleep_hours=7.5,
        stress_level=StressLevel.MODERATE,
        activity_level=ActivityLevel.MODERATE
    )

@pytest.mark.asyncio
async def test_analyze_fitness_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.analyze_fitness()
    print(f"\nAnalyze Fitness Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "analyze" in task.description.lower()
    assert "fitness" in task.description.lower()

@pytest.mark.asyncio
async def test_generate_workout_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.generate_workout()
    print(f"\nGenerate Workout Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "workout" in task.description.lower()

@pytest.mark.asyncio
async def test_create_meal_plan_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.create_meal_plan()
    print(f"\nCreate Meal Plan Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "meal" in task.description.lower()
    assert "plan" in task.description.lower()

@pytest.mark.asyncio
async def test_generate_grocery_list_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.generate_grocery_list()
    print(f"\nGenerate Grocery List Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "grocery" in task.description.lower()

@pytest.mark.asyncio
async def test_assess_skin_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.assess_skin()
    
    # Execute the task using run() instead of execute()
    result = await task.run()
    print(f"\nTask Output: {result}")
    
    # Your existing assertions
    assert task is not None
    assert task.description is not None
    assert "skin" in task.description.lower()
    assert "assess" in task.description.lower()

@pytest.mark.asyncio
async def test_design_routine_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.design_routine()
    print(f"\nDesign Routine Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "routine" in task.description.lower()

@pytest.mark.asyncio
async def test_analyze_data_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.analyze_data()
    print(f"\nAnalyze Data Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "analyze" in task.description.lower()
    assert "data" in task.description.lower()

@pytest.mark.asyncio
async def test_generate_report_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.generate_report()
    print(f"\nGenerate Report Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "report" in task.description.lower()

@pytest.mark.asyncio
async def test_format_plans_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.format_plans()
    print(f"\nFormat Plans Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "format" in task.description.lower()
    assert "plans" in task.description.lower()

@pytest.mark.asyncio
async def test_create_visuals_task(vitacrew, mock_user_inputs):
    vitacrew.collect_user_inputs(mock_user_inputs)
    task = vitacrew.create_visuals()
    print(f"\nCreate Visuals Task Description: {task.description}")
    assert task is not None
    assert task.description is not None
    assert "visual" in task.description.lower()