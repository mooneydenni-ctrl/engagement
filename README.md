# TikTok Auto Engagement Script

This Python script automates engagement actions on TikTok for a specified user account. Using the Selenium browser automation library, it logs into TikTok, collects recent video URLs, and interacts with each post by performing actions such as liking, saving, commenting, and sharing. Comments are randomly selected from a curated list of motivational, playful, and filter-related phrases, making the engagement appear natural and varied.

## Features

- 🔐 **Automated Login**: Securely logs into TikTok using provided credentials
- 📹 **Video Collection**: Automatically collects recent video URLs from target user's profile
- ❤️ **Like Videos**: Automatically likes videos (checks if already liked)
- 💾 **Save Videos**: Saves/favorites videos for later viewing
- 💬 **Smart Commenting**: Posts random comments from a curated list of:
  - Motivational phrases ("This is so inspiring! 🔥", "Keep up the amazing work! 💪")
  - Playful expressions ("Haha this is gold! 😂", "Can't stop watching! 👀")
  - Filter-related comments ("What filter is this? 😍", "Filter name please! 🙏")
- 🔗 **Share Interaction**: Opens share dialog (counts as engagement)
- 🎲 **Natural Behavior**: Random delays and action selection to simulate human behavior
- ⚙️ **Configurable**: Easy configuration via JSON file or environment variables

## Requirements

- Python 3.7 or higher
- Chrome browser installed
- ChromeDriver (will be managed automatically by webdriver-manager)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mooneydenni-ctrl/engagement.git
cd engagement
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

You can configure the script using either a configuration file or environment variables.

### Option 1: Configuration File

1. Copy the example configuration file:
```bash
cp config.example.json config.json
```

2. Edit `config.json` with your details:
```json
{
  "username": "your_tiktok_username_or_email",
  "password": "your_tiktok_password",
  "target_user": "target_tiktok_username",
  "headless": false,
  "max_videos": 10
}
```

**Note**: `config.json` is in `.gitignore` to protect your credentials.

### Option 2: Environment Variables

Set the following environment variables:
```bash
export TIKTOK_USERNAME="your_username"
export TIKTOK_PASSWORD="your_password"
export TIKTOK_TARGET_USER="target_username"
```

### Option 3: Interactive Input

If no configuration is found, the script will prompt you for credentials.

## Usage

Run the script:
```bash
python tiktok_engagement.py
```

The script will:
1. Initialize Chrome WebDriver
2. Log into TikTok with your credentials
3. Navigate to the target user's profile
4. Collect recent video URLs (up to `max_videos`)
5. For each video:
   - Like the video (if not already liked)
   - Save the video (if not already saved)
   - Post a random comment from the curated list
   - Open the share dialog
   - Wait random intervals between actions for natural behavior

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `username` | string | (required) | Your TikTok username or email |
| `password` | string | (required) | Your TikTok password |
| `target_user` | string | (required) | Target TikTok username (without @) |
| `headless` | boolean | `false` | Run browser in headless mode |
| `max_videos` | integer | `10` | Maximum number of videos to engage with |

## Comment Library

The script includes 30 pre-written comments across three categories:

**Motivational** (10 comments):
- "This is so inspiring! 🔥"
- "Keep up the amazing work! 💪"
- "You're crushing it! 🌟"
- And more...

**Playful** (10 comments):
- "Haha this is gold! 😂"
- "Can't stop watching! 👀"
- "This is too good! 🤩"
- And more...

**Filter-related** (10 comments):
- "What filter is this? 😍"
- "Filter name please! 🙏"
- "This filter is everything! ✨"
- And more...

## Safety Features

- **Random Delays**: Adds random delays between actions (1-7 seconds) to simulate human behavior
- **Action Randomization**: 80% chance to perform each action, making engagement patterns less predictable
- **Duplicate Prevention**: Checks if videos are already liked/saved before attempting to interact
- **Error Handling**: Graceful error handling to continue with other videos if one fails

## Important Notes

⚠️ **Use Responsibly**: This script is for educational purposes. Automated engagement may violate TikTok's Terms of Service. Use at your own risk.

🔒 **Security**: Never commit your `config.json` file or share your credentials. The `.gitignore` file is configured to exclude sensitive files.

⏱️ **Rate Limiting**: Consider the `max_videos` setting and add appropriate delays to avoid triggering TikTok's anti-spam measures.

## Troubleshooting

**Login Issues**:
- Ensure credentials are correct
- TikTok may require CAPTCHA verification - run in non-headless mode to solve manually
- Two-factor authentication (2FA) may need to be disabled temporarily

**ChromeDriver Issues**:
- The script uses `webdriver-manager` to handle ChromeDriver automatically
- Ensure Chrome browser is installed on your system

**Element Not Found Errors**:
- TikTok's HTML structure may change; selectors might need updates
- Try increasing wait times in the script

## License

MIT License - Feel free to modify and use as needed.

## Disclaimer

This tool is provided for educational purposes only. The authors are not responsible for any misuse or any violations of TikTok's Terms of Service. Always respect platform guidelines and use automation responsibly.
