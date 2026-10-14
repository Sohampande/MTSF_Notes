"""Check that the key packages from anaconda_env.yml import correctly."""

import importlib

PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "sklearn",
    "statsmodels",
    "statsforecast",
    "darts",
    "pytorch_lightning",
    "optuna",
]

failed = []
for name in PACKAGES:
    try:
        module = importlib.import_module(name)
        print(f"OK   {name} {getattr(module, '__version__', '')}")
    except Exception as exc:  # report every failure, not just the first
        print(f"FAIL {name}: {exc}")
        failed.append(name)

if failed:
    raise SystemExit(f"Missing or broken packages: {', '.join(failed)}")
print("All packages imported.")
