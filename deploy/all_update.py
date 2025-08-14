import subprocess
import sys
import os

def update_app():
    # Pull latest changes from git
    try:
        print("Pulling latest changes from git...")
        subprocess.check_call(['git', 'pull'])
    except subprocess.CalledProcessError:
        print("Git pull failed.")
        sys.exit(1)

    # Stage all changes
    try:
        print("Staging all changes...")
        subprocess.check_call(['git', 'add', '.'])
    except subprocess.CalledProcessError:
        print("Git add failed.")
        sys.exit(1)

    # Commit changes
    try:
        print("Committing changes...")
        subprocess.check_call(['git', 'commit', '-m', 'update'])
    except subprocess.CalledProcessError:
        print("Git commit failed. (No changes to commit?)")

    # Push changes
    try:
        print("Pushing changes to git remote...")
        subprocess.check_call(['git', 'push'])
    except subprocess.CalledProcessError:
        print("Git push failed.")
        sys.exit(1)

    print("Git update complete.")

if __name__ == "__main__":
    update_app()