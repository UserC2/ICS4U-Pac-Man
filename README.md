## Development Environment Setup
* Install [Visual Studio Code](https://code.visualstudio.com/Download)
  * Install [Microsoft's Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  * Click the settings button in the bottom left corner, then press "Settings":
    * Change "Auto Save" to `afterDelay`
    * Change "Autofetch" to `true` (notifies you of changes to the GitHub repository)
* Install [Git](https://git-scm.com/downloads)
  * In the installer, you may prefer to change a few options:
    * Change the default editor to one you prefer (or Nano).
    * Select "override branch name for new repositories" (leave it as "main").
* Install [Python](https://www.python.org/downloads/)
  * Make sure to select "Add Python 3.X to PATH" in the installer, otherwise `python` and `pip` will not be recognized in a terminal.
    * If you forgot, run the installer again, select "Modify", click "Next", then select "Add Python to environment variables".
* Install `pygame` once Python is installed:
  * Open a terminal (such as Command Prompt) and type `pip install pygame`

## Cloning this Repo
* Open VS Code, select the source control pane (third icon from the top on the left side of the screen), and then press "Clone Repository".
* Click "Clone from GitHub" and then sign in to your GitHub account if prompted.
* Select this repository (`ICS4U-Pac-Man`), then choose a folder to save it in.
  * If you haven't already installed the Python extension for VS Code, install it.
* To reopen this repo in the future, click "File", then "Open Folder" in VS Code.

## Running the Game
* Press "Terminal" at the top of the VS Code window, then click "New Terminal".
* Type `python main.py` (or `python3 main.py` depending on how your computer has python installed)
