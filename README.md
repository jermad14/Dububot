# Dububot

A simple Discord bot with Twitch integration.

## Features

*   **Twitch Integration:** Announces when a Twitch streamer goes live.
*   **Simple Commands:** Includes basic commands like `!ping`.
*   **Greetings:** Greets users who say "hello" or "hi".
*   **Customizable Status:** The bot's status can be changed by the owner.

## Getting Started

### Prerequisites

*   Python 3.6+
*   `discord.py` library

### Installation

#### 1. Clone the Repository

First, clone the Dububot repository to your local machine:

```bash
git clone https://github.com/jermad14/Dububot.git
cd Dububot
```

#### 2. Install Python and Dependencies

**For Linux (Debian/Ubuntu):**

1.  **Install Python 3 and pip:**
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
2.  **Install `discord.py`:**
    ```bash
    pip3 install -U discord.py
    ```

**For macOS:**

1.  **Install Python 3 and pip (if not already installed via Homebrew):**
    ```bash
    brew install python
    ```
    (If you don't have Homebrew, you can install it from `https://brew.sh/`)
    If Python 3 is already installed, ensure `pip3` is available.
2.  **Install `discord.py`:**
    ```bash
    pip3 install -U discord.py
    ```

**For Windows:**

1.  **Download and Install Python 3:**
    *   Go to the official Python website: `https://www.python.org/downloads/windows/`
    *   Download the latest Python 3 installer (e.g., "Windows installer (64-bit)").
    *   Run the installer. **Crucially, make sure to check "Add Python to PATH" during installation.** This will allow you to use `python` and `pip` from the command prompt.
2.  **Install `discord.py`:**
    *   Open Command Prompt (search for "cmd" in the Start Menu).
    *   Run the following command:
        ```bash
        pip install -U discord.py
        ```

### Configuration

1.  Rename `config_sample.ini` to `config.ini`.
2.  Open `config.ini` and fill in the required values:
    *   `owner_id`: Your Discord user ID.
    *   `command_prefix`: The prefix for bot commands (e.g., `!`).
    *   `token`: Your Discord bot token.
    *   `client_id`: Your Twitch client ID.
    *   `AnnounceChannelId`: The ID of the Discord channel where you want to send Twitch announcements.
    *   `MonitorChannels`: A comma-separated list of Twitch channel names to monitor.

### Launching the Bot

After completing the installation and configuration, you can launch the bot using the following command from the project's root directory:

```bash
python3 Dububot.py
```

## Usage

*   `!ping`: The bot will reply with "pong!".
*   `!status <game>`: The bot's owner can change the bot's status.

## Credits

*   [Jermad14](http://jermad14.com)
*   KPR

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.
