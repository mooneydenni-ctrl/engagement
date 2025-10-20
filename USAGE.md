# Usage Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

Choose one of the following methods:

#### Method A: Configuration File (Recommended)
```bash
cp config.example.json config.json
# Edit config.json with your details
```

#### Method B: Environment Variables
```bash
export TIKTOK_USERNAME="your_username"
export TIKTOK_PASSWORD="your_password"
export TIKTOK_TARGET_USER="target_username"
```

#### Method C: Interactive Input
Just run the script and enter credentials when prompted.

### 3. Run the Script

```bash
python tiktok_engagement.py
```

## Configuration Parameters

Edit `config.json` to customize behavior:

```json
{
  "username": "your_tiktok_username_or_email",
  "password": "your_tiktok_password",
  "target_user": "target_tiktok_username",
  "headless": false,
  "max_videos": 10
}
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `username` | Your TikTok login (email or username) | Required |
| `password` | Your TikTok password | Required |
| `target_user` | Username to engage with (without @) | Required |
| `headless` | Run browser without UI | `false` |
| `max_videos` | Maximum videos to process | `10` |

## Example Output

```
🚀 TikTok Auto Engagement Script
============================================================
✓ WebDriver initialized

🔑 Logging into TikTok...
⏳ Waiting for login to complete...
✓ Login successful!

📹 Collecting videos from @target_user...
✓ Found 10 videos to engage with

🎯 Starting engagement with 10 videos...

📍 Video 1/10: https://www.tiktok.com/@user/video/123...
  ↳ ❤️ Liked
  ↳ 💾 Saved
  ↳ 💬 Commented: 'This is so inspiring! 🔥'
  ↳ 🔗 Shared (dialog opened)
  ⏳ Waiting 4.2s before next video...

📍 Video 2/10: https://www.tiktok.com/@user/video/456...
  ↳ Already liked
  ↳ 💾 Saved
  ↳ 💬 Commented: 'What filter is this? 😍'
  ↳ Skipped share
  ⏳ Waiting 5.8s before next video...

...

============================================================
✅ Engagement completed successfully!
============================================================
```

## Tips for Success

### 1. First Run
- Run with `headless: false` to observe the automation
- Verify TikTok doesn't require CAPTCHA or 2FA
- Check that all actions are performed correctly

### 2. Avoiding Detection
- Don't set `max_videos` too high (recommended: 5-15)
- Run at different times of day
- Don't run multiple times in quick succession
- The script adds random delays automatically

### 3. Troubleshooting

**Login fails:**
- Check credentials in `config.json`
- Disable 2FA temporarily
- Try running in non-headless mode to solve CAPTCHA manually

**Element not found errors:**
- TikTok's UI may have changed
- Update the script's XPath selectors
- Increase wait times in the script

**ChromeDriver issues:**
- Ensure Chrome browser is installed
- Update Selenium: `pip install --upgrade selenium`

## Safety and Ethics

⚠️ **Important Reminders:**

1. **Terms of Service**: Automated engagement may violate TikTok's ToS
2. **Rate Limiting**: Use conservative `max_videos` settings
3. **Privacy**: Never share your `config.json` file
4. **Responsibility**: This tool is for educational purposes only

## Advanced Usage

### Running in Headless Mode

For automated/scheduled runs:

```json
{
  "headless": true,
  "max_videos": 5
}
```

### Using as a Library

```python
from tiktok_engagement import TikTokEngagement

bot = TikTokEngagement(
    username="your_username",
    password="your_password",
    target_user="target_user",
    headless=False,
    max_videos=5
)

bot.run()
```

### Scheduling with Cron

Add to crontab for daily execution:

```bash
# Run every day at 10 AM
0 10 * * * cd /path/to/engagement && python3 tiktok_engagement.py
```

## Getting Help

If you encounter issues:

1. Check the error message in the console
2. Try running with `headless: false` to see what's happening
3. Verify your credentials are correct
4. Review the troubleshooting section above
5. Check if TikTok's HTML structure has changed

## Comment Customization

To modify comments, edit the `COMMENTS` list in `tiktok_engagement.py`:

```python
COMMENTS = [
    "Your custom comment 1",
    "Your custom comment 2",
    # Add more...
]
```

Keep a good mix of comment types for natural engagement!
