#!/usr/bin/env python
import sys
import warnings

from vitacrew.crew import Vitacrew

from crewai import Crew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'name': "Test User",
        'age': 30,
        'gender': "MALE", 
        'height': 175.0,
        'weight': 70.0,
        'waist_circumference': 80.0,
        'hip_circumference': 90.0,
        'fitness_objectives': ["weight loss", "muscle gain"],
        'dietary_requirements': ["none"],
        'skin_type': "DRY",
        'skin_concerns': ["none"],
        'sleep_hours': 7.5,
        'stress_level': "MODERATE",
        'activity_level': "MODERATE"
    }
    # Vitacrew().crew().kickoff(inputs=inputs)
    crew = Crew(
        name="vitacrew",
        agents=[Vitacrew().beauty_specialist()],
        tasks=[Vitacrew().assess_skin()],
        inputs=inputs
    )
    crew.kickoff()



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Vitacrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Vitacrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Vitacrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
