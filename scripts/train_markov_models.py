from pathlib import Path
from src.markov_generator import build_markov_model, save_model, get_model_path, ORDER
from src.utils import load_dataset

DATASET_PATH = Path("data/races_dataset.json")


def main() -> None:
    dataset = load_dataset(str(DATASET_PATH))

    for race, gender_dataset in dataset.items():
        for gender in ("male", "female"):
            names = gender_dataset[gender]
            input_count = len(names)
            valid_count = sum(len(name) >= ORDER for name in names)
            print(f"Training {race}_{gender}...")
            try:
                model = build_markov_model(names)
                model_path = get_model_path(race, gender)
                save_model(model, model_path)
                print(f"Saved {model_path}")
                print(f'Input names: {input_count}\nValid names: {valid_count}')
                print(f"Average length: {model['avg_length']:.2f}")
            except ValueError as e:
                print(f"Failed to train {race}_{gender}: {e}")
if __name__ == "__main__":
    main()