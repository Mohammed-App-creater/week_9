# Task 1 Notebook Migration Instructions

## Current Status

The Task 1 notebook has been created at:
```
c:\Users\yoga\code\10_Academy\week_9\task1_data_preprocessing_eda.ipynb
```

## Action Required

To complete the repository setup, **manually copy** the notebook to the project structure:

### Option 1: Using File Explorer (Windows)
1. Navigate to: `C:\Users\yoga\code\10_Academy\week_9\`
2. Copy: `task1_data_preprocessing_eda.ipynb`
3. Paste into: `portfolio-optimization\notebooks\`
4. Rename to: `01_data_preprocessing_and_eda.ipynb`

### Option 2: Using Command Line (in week_9 directory)
```bash
copy task1_data_preprocessing_eda.ipynb portfolio-optimization\notebooks\01_data_preprocessing_and_eda.ipynb
```

### Option 3: Using Python (in week_9 directory)
```python
import shutil
shutil.copy(
    'task1_data_preprocessing_eda.ipynb',
    'portfolio-optimization/notebooks/01_data_preprocessing_and_eda.ipynb'
)
```

## Verification

After copying, verify the file exists:
```bash
dir portfolio-optimization\notebooks\*.ipynb
```

You should see:
```
01_data_preprocessing_and_eda.ipynb
```

## Why Manual Copy?

The automated file copy commands were cancelled during execution. A simple manual copy will complete the setup in seconds.

## Next Steps After Copy

1. Navigate to the project:
   ```bash
   cd portfolio-optimization
   ```

2. Run setup:
   ```bash
   python setup.py
   ```

3. Activate environment and launch Jupyter:
   ```bash
   venv\Scripts\activate
   jupyter notebook
   ```

---

*This is a one-time setup step. Once complete, the project structure will be fully operational.*
