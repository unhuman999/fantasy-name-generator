import streamlit as st
import time
import random
from src.utils import load_dataset
from src.generator import random_names, generate_hybrid_name, generate_name
from src.markov_generator import load_model, get_model_path, markov_generate

st.set_page_config(page_title="Fantasy Name Generator", page_icon="🎲", layout="wide", initial_sidebar_state="auto")
st.title("Fantasy Name Generator")

@st.cache_data
def get_cached_dataset():
        races_dataset = load_dataset("data/races_dataset.json")
        return races_dataset
@st.cache_data
def get_cached_markov_model(race, gender):
    model_path = get_model_path(race, gender)
    return load_model(model_path)
try:
    races_dataset = get_cached_dataset()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

with st.sidebar:
    races = list(races_dataset.keys())
    selected_race = st.selectbox("Choose your race:", races)
    genders = list(races_dataset[selected_race].keys())
    selected_gender = st.radio("Choose your gender:", genders)
    method = ["Random name", "Splicing name", "Generated name"]
    selected_method = st.radio("What type of name you want to get?", method)


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
placeholder = st.empty()

def animate_name(final_name):
    for i in range(len(final_name)):
       ready_part = final_name[:i+1] 
       remaining = len(final_name) - (i + 1)
       noise = "".join(random.choice(chars) for _ in range(remaining))
       result=ready_part+noise
       placeholder.subheader(result)
       time.sleep(0.15)
    time.sleep(0.2) 
    placeholder.empty()
    st.success(f"### ✨ Generated Name: **{final_name}** ✨")


trigger = st.button("Generate!")
if trigger:
    mode = selected_method
    try:
        if mode == "Random name": 
            generated_name = generate_name(selected_race, selected_gender, races_dataset) 
            st.info("\n[Classic Mode]")
        elif mode == "Splicing name":
            n1, n2 = random_names(selected_race, selected_gender, races_dataset)
            generated_name = generate_hybrid_name(n1, n2)
            st.info(f"\nOriginal blueprints: {n1} + {n2}")
        elif mode == "Generated name":
            model = get_cached_markov_model(selected_race, selected_gender)
            generated_name = markov_generate(model)
            st.info("\nGenerated name")
        animate_name(generated_name)
    except ValueError as e:
        st.error(f"Not enough names available: {e}")
    except FileNotFoundError as e:
        st.error(f"Markov model not found — please run the training script first: {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")


