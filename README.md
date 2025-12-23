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

1.  Clone the repository:
    ```bash
    git clone https://github.com/jermad14/Dububot.git
    cd Dububot
    ```
2.  Install the required libraries:
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

## Usage

*   `!ping`: The bot will reply with "pong!".
*   `!status <game>`: The bot's owner can change the bot's status.

## Credits

*   [Jermad14](http://jermad14.com)
*   KPR

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.
