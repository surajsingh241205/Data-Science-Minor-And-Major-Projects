# PANDAS FEATURE EXTRACTION

A small project for feature extraction using pandas on an anime dataset.

**Project**
- Purpose: Demonstrate feature extraction, cleaning, encoding, and basic preprocessing using pandas and common ML utilities.
- Dataset: `anime.csv` (included in the repository).
- Notebook: `Feature _Extraction.ipynb` contains the step-by-step workflow.

**Contents**
- `anime.csv` — raw dataset used for experiments.
- `Feature _Extraction.ipynb` — Jupyter Notebook with code, explanations, and outputs.

**Requirements**
- Python 3.8+
- Recommended packages: `pandas`, `numpy`,`jupyter`.

Install packages (example):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

**Usage**
- Open the notebook in Jupyter or VS Code and run cells in order.
- The notebook loads `anime.csv`, performs cleaning, feature engineering (encoding, scaling, derived features), and saves processed outputs where applicable.

**Typical workflow**
1. Inspect dataset and missing values.
2. Clean and normalize columns.
3. Encode categorical features and scale numeric features.
4. Create and validate new features.
5. Export processed dataset for modeling.

**Contributing**
- Suggestions, bug reports, and improvements are welcome — open an issue or PR.
