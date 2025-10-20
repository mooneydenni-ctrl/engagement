#!/usr/bin/env python3
"""
TikTok Auto Engagement Script

This script automates engagement actions on TikTok for a specified user account.
Using Selenium, it logs into TikTok, collects recent video URLs, and interacts
with each post by performing actions such as liking, saving, commenting, and sharing.
"""

import time
import random
import json
import os
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TikTokEngagement:
    """Handles automated engagement actions on TikTok."""
    
    # Curated comments list - motivational, playful, and filter-related phrases
    COMMENTS = [
        # Motivational
        "This is so inspiring! 🔥",
        "Keep up the amazing work! 💪",
        "You're crushing it! 🌟",
        "Absolutely incredible! ✨",
        "Love the energy here! ⚡",
        "This made my day! 😊",
        "So motivational! 🙌",
        "You're an inspiration! 💫",
        "Keep shining! ⭐",
        "This is pure gold! 🏆",
        
        # Playful
        "Haha this is gold! 😂",
        "Can't stop watching! 👀",
        "This is too good! 🤩",
        "Obsessed with this! 💯",
        "Yesss! 🎉",
        "Vibing with this! 🎵",
        "This hits different! 🔥",
        "Chef's kiss! 👨‍🍳💋",
        "No skip! ⏭️❌",
        "On repeat! 🔄",
        
        # Filter-related
        "What filter is this? 😍",
        "Filter name please! 🙏",
        "This filter is everything! ✨",
        "Need this filter! 💕",
        "Filter game strong! 💪",
        "The filter effect is amazing! 🌟",
        "How did you get this filter? 🤔",
        "Filter recommendation: 10/10! ⭐",
        "This filter is fire! 🔥",
        "Filter perfection! 👌"
    ]
    
    def __init__(self, username: str, password: str, target_user: str, 
                 headless: bool = False, max_videos: int = 10):
        """
        Initialize the TikTok engagement bot.
        
        Args:
            username: TikTok account username/email for login
            password: TikTok account password
            target_user: Target TikTok user to engage with
            headless: Run browser in headless mode (default: False)
            max_videos: Maximum number of videos to engage with (default: 10)
        """
        self.username = username
        self.password = password
        self.target_user = target_user
        self.headless = headless
        self.max_videos = max_videos
        self.driver = None
        
    def setup_driver(self):
        """Set up Chrome WebDriver with appropriate options."""
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        print("✓ WebDriver initialized")
        
    def login(self):
        """Log into TikTok with provided credentials."""
        print("\n🔑 Logging into TikTok...")
        self.driver.get("https://www.tiktok.com/login")
        time.sleep(3)
        
        try:
            # Click on "Use phone / email / username" option
            login_method = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Use phone / email / username')]"))
            )
            login_method.click()
            time.sleep(2)
            
            # Click on "Log in with email or username"
            email_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log in with email or username')]"))
            )
            email_login.click()
            time.sleep(2)
            
            # Enter username/email
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys(self.username)
            time.sleep(1)
            
            # Enter password
            password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
            password_field.send_keys(self.password)
            time.sleep(1)
            
            # Click login button
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            
            print("⏳ Waiting for login to complete...")
            time.sleep(10)  # Wait for login to process
            
            # Verify login success
            if "login" not in self.driver.current_url.lower():
                print("✓ Login successful!")
                return True
            else:
                print("✗ Login may have failed. Please check credentials.")
                return False
                
        except Exception as e:
            print(f"✗ Login error: {str(e)}")
            return False
    
    def collect_video_urls(self) -> List[str]:
        """
        Navigate to target user's profile and collect recent video URLs.
        
        Returns:
            List of video URLs
        """
        print(f"\n📹 Collecting videos from @{self.target_user}...")
        profile_url = f"https://www.tiktok.com/@{self.target_user}"
        self.driver.get(profile_url)
        time.sleep(5)
        
        video_urls = []
        
        try:
            # Scroll to load more videos
            for _ in range(3):
                self.driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(2)
            
            # Find video links
            video_elements = self.driver.find_elements(
                By.XPATH, 
                "//div[contains(@class, 'DivItemContainer')]//a"
            )
            
            for element in video_elements[:self.max_videos]:
                url = element.get_attribute('href')
                if url and '/video/' in url:
                    video_urls.append(url)
            
            print(f"✓ Found {len(video_urls)} videos to engage with")
            return video_urls
            
        except Exception as e:
            print(f"✗ Error collecting videos: {str(e)}")
            return video_urls
    
    def like_video(self) -> bool:
        """Like the current video."""
        try:
            like_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'like')]"))
            )
            
            # Check if already liked
            aria_label = like_button.get_attribute('aria-label')
            if aria_label and 'unlike' in aria_label.lower():
                print("  ↳ Already liked")
                return True
            
            like_button.click()
            time.sleep(1)
            print("  ↳ ❤️ Liked")
            return True
            
        except Exception as e:
            print(f"  ↳ Could not like: {str(e)}")
            return False
    
    def save_video(self) -> bool:
        """Save/favorite the current video."""
        try:
            save_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'favorite')]"))
            )
            
            # Check if already saved
            aria_label = save_button.get_attribute('aria-label')
            if aria_label and 'remove' in aria_label.lower():
                print("  ↳ Already saved")
                return True
            
            save_button.click()
            time.sleep(1)
            print("  ↳ 💾 Saved")
            return True
            
        except Exception as e:
            print(f"  ↳ Could not save: {str(e)}")
            return False
    
    def comment_on_video(self) -> bool:
        """Post a random comment on the current video."""
        try:
            # Click on comment section to focus
            comment_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'comment')]"))
            )
            comment_button.click()
            time.sleep(2)
            
            # Find comment input box
            comment_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
            )
            
            # Select random comment
            comment_text = random.choice(self.COMMENTS)
            comment_input.send_keys(comment_text)
            time.sleep(1)
            
            # Submit comment
            post_button = self.driver.find_element(
                By.XPATH, 
                "//div[contains(@class, 'CommentPost')]//button | //button[contains(text(), 'Post')]"
            )
            post_button.click()
            time.sleep(2)
            print(f"  ↳ 💬 Commented: '{comment_text}'")
            return True
            
        except Exception as e:
            print(f"  ↳ Could not comment: {str(e)}")
            return False
    
    def share_video(self) -> bool:
        """Share the current video (opens share dialog)."""
        try:
            share_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'share')]"))
            )
            share_button.click()
            time.sleep(1)
            
            # Close share dialog (just opening counts as engagement)
            close_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Close')]")
            close_button.click()
            time.sleep(1)
            print("  ↳ 🔗 Shared (dialog opened)")
            return True
            
        except Exception as e:
            print(f"  ↳ Could not share: {str(e)}")
            return False
    
    def engage_with_video(self, video_url: str, index: int):
        """
        Perform all engagement actions on a single video.
        
        Args:
            video_url: URL of the video to engage with
            index: Index of the video (for display)
        """
        print(f"\n📍 Video {index + 1}/{len(self.video_urls)}: {video_url}")
        
        try:
            self.driver.get(video_url)
            time.sleep(5)  # Wait for video to load
            
            # Perform engagement actions with random delays
            actions = [
                ('like', self.like_video),
                ('save', self.save_video),
                ('comment', self.comment_on_video),
                ('share', self.share_video)
            ]
            
            # Randomly decide which actions to perform (more natural)
            for action_name, action_func in actions:
                if random.random() > 0.2:  # 80% chance to perform each action
                    action_func()
                    time.sleep(random.uniform(1, 3))  # Random delay between actions
                else:
                    print(f"  ↳ Skipped {action_name}")
            
            # Random delay before next video
            delay = random.uniform(3, 7)
            print(f"  ⏳ Waiting {delay:.1f}s before next video...")
            time.sleep(delay)
            
        except Exception as e:
            print(f"✗ Error engaging with video: {str(e)}")
    
    def run(self):
        """Main execution method - runs the entire engagement process."""
        try:
            print("\n" + "="*60)
            print("🚀 TikTok Auto Engagement Script")
            print("="*60)
            
            self.setup_driver()
            
            if not self.login():
                print("\n✗ Failed to login. Exiting...")
                return
            
            self.video_urls = self.collect_video_urls()
            
            if not self.video_urls:
                print("\n✗ No videos found. Exiting...")
                return
            
            print(f"\n🎯 Starting engagement with {len(self.video_urls)} videos...")
            
            for i, video_url in enumerate(self.video_urls):
                self.engage_with_video(video_url, i)
            
            print("\n" + "="*60)
            print("✅ Engagement completed successfully!")
            print("="*60)
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Process interrupted by user")
            
        except Exception as e:
            print(f"\n✗ Unexpected error: {str(e)}")
            
        finally:
            if self.driver:
                print("\n🔚 Closing browser...")
                self.driver.quit()


def load_config(config_file: str = 'config.json') -> Dict:
    """
    Load configuration from JSON file.
    
    Args:
        config_file: Path to configuration file
        
    Returns:
        Dictionary with configuration values
    """
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    return {}


def main():
    """Main entry point for the script."""
    print("\n🤖 TikTok Auto Engagement Bot")
    print("-" * 40)
    
    # Try to load config from file
    config = load_config()
    
    # Get credentials from config or environment variables
    username = config.get('username') or os.getenv('TIKTOK_USERNAME')
    password = config.get('password') or os.getenv('TIKTOK_PASSWORD')
    target_user = config.get('target_user') or os.getenv('TIKTOK_TARGET_USER')
    
    # Prompt for missing values
    if not username:
        username = input("Enter your TikTok username/email: ")
    if not password:
        password = input("Enter your TikTok password: ")
    if not target_user:
        target_user = input("Enter target TikTok username (without @): ")
    
    # Get optional parameters
    headless = config.get('headless', False)
    max_videos = config.get('max_videos', 10)
    
    if not all([username, password, target_user]):
        print("\n✗ Missing required credentials. Exiting...")
        return
    
    # Create and run bot
    bot = TikTokEngagement(
        username=username,
        password=password,
        target_user=target_user,
        headless=headless,
        max_videos=max_videos
    )
    
    bot.run()


if __name__ == "__main__":
    main()
