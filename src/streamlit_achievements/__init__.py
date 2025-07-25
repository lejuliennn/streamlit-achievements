from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_achievements,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_achievements", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_achievements(
    title: str = "",
    description: str = "",
    points: int = 0,
    icon_text: str = "",
    duration: int = 5000,
    icon_background_color: str = "#8BC34A",
    background_color: str = "#2E7D32",
    text_color: str = "#FFFFFF",
    shadow_color: str = "rgba(0,0,0,0.3)",
    key: Optional[str] = None,
):
    """
    Create an achievement notification with customizable colors and content.
    
    Parameters:
    - title: The achievement title (default: "")
    - description: The achievement description (default: "")
    - points: Points/score for the achievement (default: 0)
    - icon_text: Text or emoji to display in the achievement icon (default: "")
    - duration: Duration in milliseconds for the animation (default: 5000)
    - icon_background_color: Color for the circular icon background (default: "#8BC34A")
    - background_color: Color for the expanding background (default: "#2E7D32")
    - text_color: Color for the text and icon content (default: "#FFFFFF")
    - shadow_color: Color for shadows and depth effects (default: "rgba(0,0,0,0.3)")
    - key: Optional key for the component
    """
    # Add timestamp to make each call unique and prevent Streamlit caching issues
    import time
    timestamp = int(time.time() * 1000)  # Current time in milliseconds
    
    component_value = _component_func(
        title=title,
        description=description,
        points=points,
        icon_text=icon_text,
        duration=duration,
        icon_background_color=icon_background_color,
        background_color=background_color,
        text_color=text_color,
        shadow_color=shadow_color,
        timestamp=timestamp,  # Add timestamp to ensure uniqueness
        key=key,
    )

    return component_value


def main():
    st.write("## Achievement Component Example")
    
    # Example usage with defaults
    if st.button("Trigger Empty Achievement"):
        streamlit_achievements()
    
    # Example with custom values
    if st.button("Trigger Custom Achievement"):
        streamlit_achievements(
            title="Achievement Unlocked!",
            description="You Win",
            points=10,
            icon_text="🏆"
        )
    
    # Example with custom colors
    if st.button("Trigger Blue Achievement"):
        streamlit_achievements(
            title="Ocean Explorer",
            description="Deep Sea Discovery",
            points=25,
            icon_text="🌊",
            icon_background_color="#42A5F5",
            background_color="#1976D2"
        )
    
    st.write("Click the buttons above to see the achievement animations!")
    st.write("**Default values:** All fields default to empty strings ('')")


if __name__ == "__main__":
    main()
