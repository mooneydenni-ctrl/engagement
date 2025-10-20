# TikTok Auto Engagement Script

This Python script automates engagement actions on TikTok for a specified user account. Using the Selenium browser automation library, it logs into TikTok, collects recent video URLs, and interacts with each post by performing actions such as liking, saving, commenting, and sharing.

## Features

- 🤖 **Automated Login**: Logs into TikTok using your credentials
- 📹 **Video Collection**: Collects recent video URLs from a target user's profile
- ❤️ **Like Videos**: Automatically likes videos
- 💾 **Save Videos**: Saves/favorites videos to your account
- 💬 **Comment**: Posts randomized comments on videos
- 🔄 **Share**: Opens share dialog for videos
- 🎲 **Human-like Behavior**: Random delays to mimic natural user behavior
- 📝 **Logging**: Comprehensive logging of all actions

## Requirements

- Python 3.7+
- Chrome browser installed
- TikTok account

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mooneydenni-ctrl/engagement.git
cd engagement
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Edit the `.env` file with your credentials:
```env
TIKTOK_USERNAME=your_username
TIKTOK_PASSWORD=your_password
TARGET_USER=target_username
```

## Usage

### Basic Usage

Run the script with default settings (like and save actions):
```bash
python tiktok_engagement.py
```

### Advanced Usage

You can customize the bot by modifying the `main()` function in `tiktok_engagement.py`:

```python
# Configure engagement actions
actions = ['like', 'save', 'comment', 'share']

# Run with custom settings
bot.run(max_videos=20, actions=actions)
```

### Customizing Comments

Edit the comments list in the `run()` method:
```python
comments = [
    "Great content! 🔥",
    "Love this! ❤️",
    "Amazing! 👏",
    "Your custom comment here"
]
```

## Configuration

The script supports the following configuration options:

- `max_videos`: Maximum number of videos to engage with (default: 10)
- `actions`: List of actions to perform: `['like', 'save', 'comment', 'share']`
- `comments`: List of possible comments (randomly selected)
- `headless`: Run browser in headless mode (default: False)

## Important Notes

⚠️ **Use Responsibly**: 
- This script is for educational purposes
- Excessive automation may violate TikTok's Terms of Service
- Use at your own risk
- Consider rate limiting to avoid account restrictions

⚠️ **Security**:
- Never commit your `.env` file with real credentials
- Keep your credentials secure
- Use a dedicated test account if possible

⚠️ **Login Challenges**:
- TikTok has strong anti-bot measures
- Manual intervention may be required during login
- Consider using cookies or session management for repeated use

## Troubleshooting

### ChromeDriver Issues
If you encounter ChromeDriver issues, ensure Chrome browser is installed and up to date.

### Login Failures
TikTok's login process may require:
- Manual CAPTCHA solving
- Two-factor authentication
- Email/SMS verification

The script will pause to allow manual intervention when needed.

### Element Not Found Errors
TikTok's UI changes frequently. Element selectors may need updates if the script fails to find elements.

## Project Structure

```
engagement/
├── tiktok_engagement.py   # Main script
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for educational purposes.

## Disclaimer

This script is provided for educational purposes only. The authors are not responsible for any misuse or consequences resulting from the use of this script. Always respect platform terms of service and use automation responsibly.
