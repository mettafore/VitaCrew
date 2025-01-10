import streamlit as st
from vitacrew.crew import Vitacrew, UserInputs, Gender, StressLevel, ActivityLevel, SkinType

class VitaCrewUI:
    def __init__(self):
        self.vitacrew = Vitacrew()

    def initialize_session_state(self):
        """Initialize session state variables if they don't exist"""
        if "user_inputs" not in st.session_state:
            st.session_state.user_inputs = {}
        if "generating_plan" not in st.session_state:
            st.session_state.generating_plan = False
        if "wellness_plan" not in st.session_state:
            st.session_state.wellness_plan = None

    def personal_info_form(self):
        """Collect personal information from user"""
        st.subheader("Personal Information")
        
        name = st.text_input("Name", key="name")
        age = st.number_input("Age", min_value=18, max_value=120, key="age")
        gender = st.selectbox("Gender", options=[g.value for g in Gender], key="gender")
        
        col1, col2 = st.columns(2)
        with col1:
            height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, key="height")
            waist = st.number_input("Waist Circumference (cm)", min_value=40.0, max_value=200.0, key="waist")
        with col2:
            weight = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, key="weight")
            hip = st.number_input("Hip Circumference (cm)", min_value=40.0, max_value=200.0, key="hip")

        return {
            "name": name,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "waist_circumference": waist,
            "hip_circumference": hip
        }

    def health_goals_form(self):
        """Collect health goals and preferences"""
        st.subheader("Health Goals & Preferences")

        fitness_objectives = st.multiselect(
            "Fitness Objectives",
            options=["weight loss", "muscle gain", "endurance", "flexibility",
                    "strength", "general fitness", "athletic performance"],
            key="fitness_objectives"
        )

        dietary_requirements = st.multiselect(
            "Dietary Requirements",
            options=["vegetarian", "vegan", "gluten-free", "dairy-free",
                    "keto", "paleo", "halal", "kosher", "none"],
            key="dietary_requirements"
        )

        skin_type = st.selectbox("Skin Type", options=[s.value for s in SkinType], key="skin_type")
        
        skin_concerns = st.multiselect(
            "Skin Concerns",
            options=["acne", "aging", "dark spots", "dryness", "oiliness",
                    "redness", "sensitivity", "uneven texture", "none"],
            key="skin_concerns"
        )

        return {
            "fitness_objectives": fitness_objectives,
            "dietary_requirements": dietary_requirements,
            "skin_type": skin_type,
            "skin_concerns": skin_concerns
        }

    def lifestyle_factors_form(self):
        """Collect lifestyle information"""
        st.subheader("Lifestyle Factors")

        sleep_hours = st.slider("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0, step=0.5, key="sleep_hours")
        stress_level = st.selectbox("Stress Level", options=[s.value for s in StressLevel], key="stress_level")
        activity_level = st.selectbox("Activity Level", options=[a.value for a in ActivityLevel], key="activity_level")

        return {
            "sleep_hours": sleep_hours,
            "stress_level": stress_level,
            "activity_level": activity_level
        }

    def display_health_metrics(self):
        """Display calculated health metrics"""
        if "user_inputs" in st.session_state and st.session_state.user_inputs:
            st.subheader("Health Metrics")
            
            col1, col2 = st.columns(2)
            with col1:
                if "health_metrics" in st.session_state.user_inputs:
                    metrics = st.session_state.user_inputs["health_metrics"]
                    st.metric("BMR (kcal/day)", f"{metrics['bmr']:.0f}")

    def display_agent_interactions(self):
        """Display agent interactions and progress"""
        if st.session_state.generating_plan:
            st.header("Generating Your Wellness Plan")
            
            with st.spinner("Personal Trainer analyzing your fitness profile..."):
                # Simulate agent work - in real implementation, this would be actual agent tasks
                st.progress(0.25)
            
            with st.spinner("Nutritionist creating your meal plan..."):
                st.progress(0.50)
            
            with st.spinner("Beauty Specialist designing your skincare routine..."):
                st.progress(0.75)
            
            with st.spinner("Health Analyst compiling your comprehensive report..."):
                st.progress(1.0)

            st.session_state.generating_plan = False
            st.session_state.wellness_plan = "Generated"  # This would be actual plan in real implementation

        if st.session_state.wellness_plan:
            st.success("Your Wellness Plan is ready!")
            st.download_button(
                label="Download Wellness Plan (PDF)",
                data="Your wellness plan content here",  # This would be actual PDF in real implementation
                file_name="wellness_plan.pdf",
                mime="application/pdf"
            )

    def sidebar(self):
        """Render the sidebar with user input forms"""
        with st.sidebar:
            st.title("VitaCrew")
            st.write("Your AI-powered wellness team")

            # Collect all user inputs
            personal_info = self.personal_info_form()
            health_goals = self.health_goals_form()
            lifestyle_factors = self.lifestyle_factors_form()

            # Combine all inputs
            if st.button("Generate Wellness Plan"):
                try:
                    user_inputs = UserInputs(
                        **personal_info,
                        **health_goals,
                        **lifestyle_factors
                    )
                    st.session_state.user_inputs = user_inputs.model_dump()
                    st.session_state.generating_plan = True
                except Exception as e:
                    st.error(f"Please fill in all required fields: {str(e)}")

    def render(self):
        """Main render function"""
        st.set_page_config(
            page_title="VitaCrew - Your AI Wellness Team",
            page_icon="💪",
            layout="wide"
        )

        self.initialize_session_state()
        
        # Render sidebar with input forms
        self.sidebar()

        # Main panel
        if not st.session_state.generating_plan and not st.session_state.wellness_plan:
            st.title("Welcome to VitaCrew")
            st.write("""
            👈 Fill out your information in the sidebar to get started with your personalized wellness journey.
            
            Our AI agents will work together to create a comprehensive wellness plan including:
            - Personalized workout routines
            - Custom meal plans
            - Skincare regimens
            - Progress tracking tools
            """)
        
        # Display health metrics
        self.display_health_metrics()
        
        # Display agent interactions and progress
        self.display_agent_interactions()

if __name__ == "__main__":
    VitaCrewUI().render() 