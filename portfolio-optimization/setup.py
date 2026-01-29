#!/usr/bin/env python3
"""
Setup script for portfolio-optimization project.

This script guides users through the initial setup process.
"""

import os
import subprocess
import sys
from pathlib import Path


def check_python_version():
    """Ensure Python 3.9+ is installed."""
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or higher is required.")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")


def create_venv():
    """Create a virtual environment if it doesn't exist."""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return

    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    print("✅ Virtual environment created")


def get_pip_path():
    """Get the path to pip in the virtual environment."""
    if sys.platform == "win32":
        return Path("venv/Scripts/pip.exe")
    return Path("venv/bin/pip")


def install_dependencies():
    """Install dependencies from requirements.txt."""
    pip = get_pip_path()
    
    print("\nInstalling dependencies...")
    subprocess.run([str(pip), "install", "--upgrade", "pip"], check=True)
    subprocess.run([str(pip), "install", "-r", "requirements.txt"], check=True)
    print("✅ Dependencies installed")


def display_next_steps():
    """Display instructions for next steps."""
    print("\n" + "="*60)
    print("🎉 Setup Complete!")
    print("="*60)
    
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    print("\nNext steps:")
    print(f"  1. Activate the virtual environment:")
    print(f"     {activate_cmd}")
    print(f"\n  2. Start Jupyter Notebook:")
    print(f"     jupyter notebook")
    print(f"\n  3. Navigate to notebooks/ and open:")
    print(f"     01_data_preprocessing_and_eda.ipynb")
    print(f"\n  4. Run all cells to execute Task 1")
    print("\n" + "="*60)


def main():
    """Main setup function."""
    print("="*60)
    print("Portfolio Optimization Project - Setup")
    print("="*60)
    print()

    check_python_version()
    create_venv()
    install_dependencies()
    display_next_steps()


if __name__ == "__main__":
    main()
