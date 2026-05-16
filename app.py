# Basic Streamlit app to demonstrate the BaseAgent
import streamlit as st
from agents.base_agent import BaseAgent
def main():
    st.title("MiniMind Base Agent Demo")
    
    # Create an instance of the BaseAgent
    agent = BaseAgent(name="TestAgent")
    
    # Display agent information
    st.write(f"Agent Name: {agent.name}")
    
    # Simulate an observation
    observation = "Sample observation"
    st.write(f"Observation: {observation}")
    
    # Get the agent's action based on the observation
    action = agent.act(observation)
    st.write(f"Agent Action: {action}")

if __name__ == "__main__":
    main()