from crewai.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field

# Calculation Tools
class BMRCalculatorInput(BaseModel):
    """Input for BMR Calculator"""
    weight: float = Field(..., description="Weight in kg")
    height: float = Field(..., description="Height in cm")
    age: int = Field(..., description="Age in years")
    gender: str = Field(..., description="Gender (male/female)")

class BMRCalculator(BaseTool):
    name: str = "BMR Calculator"
    description: str = "Calculates Basal Metabolic Rate based on weight, height, age, and gender"
    args_schema: Type[BaseModel] = BMRCalculatorInput

    def _run(self, weight: float, height: float, age: int, gender: str) -> float:
        if gender.lower() == "male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return round(bmr, 2)

class MacroCalculatorInput(BaseModel):
    """Input for Macronutrient Calculator"""
    calories: float = Field(..., description="Daily calorie target")
    goal: str = Field(..., description="Fitness goal (maintenance/bulking/cutting)")

class MacroCalculator(BaseTool):
    name: str = "Macronutrient Calculator"
    description: str = "Calculates optimal macronutrient ratios based on calorie target and fitness goal"
    args_schema: Type[BaseModel] = MacroCalculatorInput

    def _run(self, calories: float, goal: str) -> dict:
        ratios = {
            "maintenance": {"protein": 0.3, "carbs": 0.4, "fats": 0.3},
            "bulking": {"protein": 0.25, "carbs": 0.5, "fats": 0.25},
            "cutting": {"protein": 0.4, "carbs": 0.3, "fats": 0.3}
        }
        
        goal_ratio = ratios.get(goal.lower(), ratios["maintenance"])
        return {
            "protein": round((calories * goal_ratio["protein"]) / 4, 1),  # 4 cal/g
            "carbs": round((calories * goal_ratio["carbs"]) / 4, 1),     # 4 cal/g
            "fats": round((calories * goal_ratio["fats"]) / 9, 1)        # 9 cal/g
        }

# Progress Tracking Tools
class ProgressTrackerInput(BaseModel):
    """Input for Progress Tracker"""
    metric_type: str = Field(..., description="Type of metric to track (workout/nutrition/skin)")
    value: float = Field(..., description="Current metric value")
    date: str = Field(..., description="Date of measurement")
    notes: Optional[str] = Field(None, description="Additional notes")

class ProgressTracker(BaseTool):
    name: str = "Progress Tracker"
    description: str = "Tracks progress for various health and fitness metrics"
    args_schema: Type[BaseModel] = ProgressTrackerInput

    def _run(self, metric_type: str, value: float, date: str, notes: Optional[str] = None) -> dict:
        return {
            "metric_type": metric_type,
            "value": value,
            "date": date,
            "notes": notes,
            "status": "recorded"
        }

# Report Generation Tools
class ReportGeneratorInput(BaseModel):
    """Input for Report Generator"""
    report_type: str = Field(..., description="Type of report to generate")
    data: dict = Field(..., description="Data to include in the report")
    format: str = Field(..., description="Output format (pdf/html)")

class ReportGenerator(BaseTool):
    name: str = "Report Generator"
    description: str = "Generates formatted reports for various health and fitness metrics"
    args_schema: Type[BaseModel] = ReportGeneratorInput

    def _run(self, report_type: str, data: dict, format: str) -> str:
        # In a real implementation, this would generate actual reports
        return f"Generated {format} report for {report_type} with provided data"
