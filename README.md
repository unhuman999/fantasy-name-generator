# Fantasy Name Generator

A Python console application that generates fantasy names based on the selected race and gender.
The project is currently under active development and aims to evolve from a random name selector into a procedural fantasy name generator, with future exploration of machine learning techniques.


## Project Status

🚧 This project is currently under active development.

Current version:
- Console application
- Random name selection from JSON datasets
- Support for Human, Elf, and Orc races
- Male and Female name generation


## Features

- Generate fantasy names for multiple races.
- Support for Human, Elf, and Orc races.
- Generate both male and female names.
- Store names in structured JSON datasets.
- Simple and lightweight console interface.
- Modular project structure for future expansion.


## Roadmap

### Dataset Expansion
- [ ] Expand the dataset with 20,000+ curated fantasy names.
- [ ] Add Dwarf race support.
- [ ] Improve dataset quality by removing duplicates and invalid names.

### Generator Improvements
- [ ] Replace pure random selection with syllable-based name generation.
- [ ] Introduce race-specific syllable patterns.
- [ ] Improve name diversity while preserving race identity.

### Project Improvements
- [ ] Add automated tests.
- [ ] Improve project documentation.
- [ ] Optimize project structure.

### Future Research
- [ ] Experiment with machine learning approaches for fantasy name generation.
- [ ] Compare rule-based and machine learning generators.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/unhuman999/fantasy-name-generator.git
```
2. Navigate to the project directory:
```bash
cd fantasy-name-generator
```
3. Create a virtual environment:
```bash
python -m venv .venv
```
4. Activate the virtual environment.
**Windows (cmd):**
```cmd
.venv\Scripts\activate
```
**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```
5. Install the required dependencies:
```bash
pip install -r requirements.txt
```


## Usage

Run the application from the project root:
```bash
python src/main.py
```

Follow the prompts in the console to:
1. Select a race.
2. Select a gender.
3. Receive a randomly selected fantasy name.


## Project Structure

```text
fantasy-name-generator/
│
├── data/              # JSON datasets 
├── src/               # Application source code 
├── .venv/             # Virtual environment (not tracked by Git) 
├── README.md
├── requirements.txt
└── .gitignore
```


## Dataset

Fantasy names are stored in JSON files.
Each race has separate datasets for male and female names.
The dataset is continuously expanding to improve name variety and support additional fantasy races.


## Technologies

- Python 3.14
- Pydantic
- JSON


## Author

Developed by unhuman999