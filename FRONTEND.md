# VitaCrew Frontend Architecture

## Overview
The VitaCrew frontend leverages Streamlit to create an intuitive interface that collects user information, displays agent interactions, and generates personalized wellness plans.

## Core Components

### User Input Panel (Left Sidebar)
- Personal Information Form
  - Name
  - Age
  - Gender
  - Height
  - Weight
  - Waist Circumference
  - Hip Circumference
- Health Goals Form
  - Fitness Objectives (weight loss, muscle gain, endurance etc.)
  - Dietary Requirements (vegetarian, vegan, allergies etc.)
  - Skin Type and Concerns
  - Lifestyle Factors (sleep, stress, activity level)
- Calculate Health Metrics
  - BMR (Basal Metabolic Rate)
  - TDEE (Total Daily Energy Expenditure)
  - Body Composition Analysis
- Generate Plan Button

### Agent Interaction Display (Main Panel)
- Multi-Agent Conversation View
  - Personal Trainer Agent discussions
    - Workout planning
    - Form guidance
    - Progress tracking
  - Nutritionist Agent discussions
    - Meal planning
    - Dietary analysis
    - Shopping recommendations
  - Beauty & Skincare Specialist discussions
    - Skincare routines
    - Product recommendations
  - Health Analytics Agent insights
    - Data correlation
    - Progress patterns
    - Inter-agent coordination
- Real-time progress indicators
- Interactive feedback system

### PDF Report Generation
- Comprehensive Wellness Plan
  - Personalized workout routines
  - Custom meal plans and grocery lists
  - Skincare regimens
  - Supplement recommendations
  - Progress tracking tools
  - Health metrics analysis
  - Agent recommendations and guidelines

## Technical Implementation

### Streamlit Components
- st.sidebar for user input forms
- st.container for agent conversation display
- st.download_button for PDF export
- st.session_state for maintaining user data
- st.progress for loading indicators
- st.metrics for health calculations display

