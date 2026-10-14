# MTSF Notes

My notes and code for *Modern Time Series Forecasting with Python*, organized by chapter.

## Setup

1. Create the Anaconda environment (from the project root):

   ```bash
   conda env create -f anaconda_env.yml
   conda activate modern_ts
   ```

   Alternative with pip only: `pip install -r requirements.txt`

2. Check the install:

   ```bash
   python test_installation.py
   ```

3. Kaggle datasets need an API key. Download `kaggle.json` from your Kaggle account settings and save it as `api_keys/kaggle.json`. This folder is git-ignored.

## Data

Datasets are downloaded into `data/`, which is git-ignored. To fetch the London Smart Meters data:

```bash
python scripts/download_data.py
```

## Running the notebooks

Run them in this order:

1. `notebooks/Chapter02/Chapter-2.ipynb`: preprocessing. Creates the cleaned London Smart Meter data that later chapters use.
2. Chapter notebooks in `notebooks/Chapter04/` and onward.

## Layout

```
notebooks/   chapter notebooks (Chapter01/, Chapter02/, ...)
scripts/     data download helpers
api_keys/    local only (git-ignored)
data/        local only (git-ignored)
```
