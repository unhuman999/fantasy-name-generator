# Fantasy Name Generator

**MVP v0.2.1-alpha** · A Python console application that generates fantasy names by race and gender.

The project combines curated real-world datasets with procedural generation techniques, and is planned to evolve further — including a future exploration of Markov chain-based generation.

🔗 [GitHub Repository](https://github.com/unhuman999/fantasy-name-generator)

---

## Project Status

🚧 **Under active development.**

Current version (`v0.2.1-alpha`) includes:

- Console application with an interactive prompt
- Random name selection from curated JSON datasets
- A second generation mode that blends two existing names into a new one
- Support for **Human, Elf, Dwarf, and Orc** races
- Male and female name generation
- Automated test coverage for core generation and dataset-loading logic

---

## Features

- 🎲 **Classic mode** — pick a random, authentic name straight from the dataset
- 🧬 **Hybrid mode** — blend two existing names of the same race/gender into a new one
- 🧝 Four races supported: Human, Elf, Dwarf, Orc
- ⚥ Male and female generation for every race
- 📦 Names stored in structured, validated JSON datasets
- 🖥️ Lightweight console interface, no external services required
- 🧪 Unit-tested core logic (generation and dataset loading)
- 🧱 Modular project structure, built for future expansion

---

## Roadmap

### Dataset

- [x] Expand the dataset to 17,000+ curated fantasy names
- [x] Add Dwarf race support
- [x] Clean the dataset — remove duplicates and invalid entries

### Generator

- [x] Add a second generation mode that blends two existing names
- [ ] Rework name blending to respect syllable boundaries instead of raw character midpoints
- [ ] Improve name diversity while preserving each race's phonetic identity
- [ ] Explore Markov chain-based name generation (planned for v0.3)

### Project

- [x] Add automated tests
- [x] Expand documentation
- [ ] Refactor project structure for scale

### Future Research

- [ ] Explore machine learning approaches to name generation
- [ ] Compare rule-based generation against ML-based generation

---

## Installation

1. **Clone the repository**
```bash
   git clone https://github.com/unhuman999/fantasy-name-generator.git
   cd fantasy-name-generator
```

2. **Create a virtual environment**
```bash
   python -m venv .venv
```

3. **Activate it**

   Windows (cmd):
```cmd
   .venv\Scripts\activate
```
   Windows (PowerShell):
```powershell
   .venv\Scripts\Activate.ps1
```
   macOS/Linux:
```bash
   source .venv/bin/activate
```

4. **Install dependencies**
```bash
   pip install -r requirements.txt
```

---

## Usage

Run the application from the project root:

```bash
python src/main.py
```

Follow the interactive prompts to:

1. Choose a race — `Human`, `Elf`, `Dwarf`, or `Orc`
2. Choose a gender — `male` or `female`
3. Choose a generation mode:
   - **1 — Classic**: get an authentic name straight from the dataset
   - **2 — Hybrid**: get a new name blended from two existing ones
4. Receive your generated name

---

## Running Tests

The project uses `pytest` for automated testing. From the project root:

```bash
pytest
```

Tests cover:
- Hybrid name generation logic (`generate_hybrid_name`), including edge cases
- Seeded/deterministic generation via an injectable `random.Random` instance
- Error handling for datasets with insufficient names per race/gender
- Dataset loading: missing files, malformed JSON, and schema validation failures

---

## Project Structure

```text
fantasy-name-generator/
│
├── data/                      # Curated JSON name datasets
├── src/
│   ├── main.py                # CLI entry point and user interaction
│   ├── generator.py           # Name generation logic (classic & hybrid)
│   ├── models.py              # Pydantic schemas for dataset validation
│   └── utils.py                # Dataset loading and validation
├── tests/
│   ├── test_generator.py      # Tests for name generation logic
│   └── test_utils.py          # Tests for dataset loading
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset

Fantasy names are stored in structured, schema-validated JSON files.

- Separate name pools for each race
- Male and female names stored independently
- **17,000+** curated fantasy names, collected and filtered from public fan wikis
- Future updates will focus on further dataset quality improvements and additional races

### Data Sources

Names in this dataset were gathered from names appearing in the **Lord of the Rings**, **Dungeons & Dragons**, and **World of Warcraft** fictional universes, via public fan wiki sources. All rights to these original works, characters, and universes belong to their respective copyright holders (including but not limited to the Tolkien Estate, Wizards of the Coast/Hasbro, and Blizzard Entertainment).

This is a non-commercial, fan-made hobby project created for personal learning purposes. No affiliation with, or endorsement by, the rights holders is claimed or implied. No monetary or commercial benefit is derived from the use of these names.

---

## Technologies

- Python 3.14
- Pydantic
- pytest
- JSON

---

## Author

Developed by **unhuman999**