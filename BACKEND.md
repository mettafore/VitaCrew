# VitaCrew Backend Architecture

## System Overview
VitaCrew is powered by a multi-agent AI system built on CrewAI that provides personalized wellness support through specialized agents working in coordination.

## Core Components

### Agent Structure

#### Personal Trainer Agent
- Implements intelligent workout planning algorithms
- Tracks and analyzes user progress metrics
- Provides real-time form guidance via natural language
- Delivers personalized motivational messages and accountability reminders

#### Nutritionist Agent
- Generates customized meal plans aligned with user goals
- Creates smart grocery lists and shopping recommendations
- Provides evidence-based dietary advice and nutritional analysis
- Optimizes meal timing and macronutrient balance

#### Beauty & Skincare Specialist Agent
- Develops personalized skincare routines and regimens
- Recommends products based on skin type and concerns
- Monitors progress through systematic user feedback
- Provides lifestyle optimization guidance for skin health

#### Health Analytics Agent
- Processes and integrates data from all agent interactions
- Identifies meaningful patterns and correlations
- Facilitates inter-agent communication and coordination
- Generates comprehensive progress reports and actionable insights

#### Design & Report Agent
- Generates polished HTML reports integrating all agent recommendations
- Creates visually appealing layouts for workout plans and routines
- Designs clear nutritional charts and meal planning tables
- Produces professional skincare regimen documentation
- Formats progress tracking visualizations and analytics
- Ensures consistent branding and styling across reports
- Optimizes readability and information hierarchy
- Incorporates interactive elements for user engagement
- Generates downloadable PDF versions of wellness plans


## Technical Stack

### Core Technologies
- CrewAI Backend Framework
- Langchain Tools Integration
- Specialized Calculators:
  - BMR (Basal Metabolic Rate)
  - TDEE (Total Daily Energy Expenditure) 
  - Macronutrient Distribution
  - Calorie Deficit/Surplus

### User Input Parameters
- Personal Information:
  - Name
  - Age
  - Gender
  - Height
  - Weight
  - Waist Circumference
  - Hip Circumference
- Preferences & Goals:
  - Fitness objectives
  - Dietary requirements
  - Skin type and concerns
