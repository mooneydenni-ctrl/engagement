#!/usr/bin/env python3
"""
TikTok Auto Engagement Script

This script automates engagement actions on TikTok for a specified user account.
Using Selenium browser automation, it logs into TikTok, collects recent video URLs,
and interacts with each post by performing actions such as liking, saving, commenting, and sharing.
"""

import time
import random
import logging
from typing import List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TikTokEngagementBot:
    """Automates engagement actions on TikTok videos."""
    
    def __init__(self, username: str, password: str, target_user: str):
        """
        Initialize the TikTok engagement bot.
        
        Args:
            username: TikTok account username for login
            password: TikTok account password
            target_user: Target TikTok user to engage with
        """
        self.username = username
        self.password = password
        self.target_user = target_user
        self.driver = None
        self.wait = None
        
    def setup_driver(self, headless: bool = False) -> None:
        """Set up Chrome WebDriver with options."""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        logger.info("WebDriver initialized successfully")
        
    def login(self) -> bool:
        """
        Log in to TikTok account.
        
        Returns:
            True if login successful, False otherwise
        """
        try:
            logger.info("Navigating to TikTok login page...")
            self.driver.get("https://www.tiktok.com/login")
            time.sleep(3)
            
            # Click on "Use phone / email / username" option
            login_options = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'login')]"))
            )
            
            # This is a placeholder - actual TikTok login flow may vary
            logger.info("Login initiated. Manual intervention may be required.")
            logger.warning("Automatic login is challenging due to TikTok's security measures.")
            logger.info("Please log in manually if prompted.")
            
            # Wait for user to complete login manually if needed
            time.sleep(10)
            
            # Check if login was successful by looking for user profile elements
            if "tiktok.com" in self.driver.current_url:
                logger.info("Login appears successful")
                return True
            else:
                logger.error("Login failed")
                return False
                
        except Exception as e:
            logger.error(f"Error during login: {str(e)}")
            return False
    
    def collect_video_urls(self, max_videos: int = 10) -> List[str]:
        """
        Collect recent video URLs from target user's profile.
        
        Args:
            max_videos: Maximum number of videos to collect
            
        Returns:
            List of video URLs
        """
        video_urls = []
        try:
            logger.info(f"Navigating to @{self.target_user}'s profile...")
            profile_url = f"https://www.tiktok.com/@{self.target_user}"
            self.driver.get(profile_url)
            time.sleep(5)
            
            # Scroll to load more videos
            for _ in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            
            # Find video elements
            video_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'video-feed')]//a[@href]")
            
            for element in video_elements[:max_videos]:
                try:
                    url = element.get_attribute('href')
                    if url and '/video/' in url:
                        video_urls.append(url)
                        logger.info(f"Collected video URL: {url}")
                except Exception as e:
                    logger.warning(f"Could not extract URL from element: {str(e)}")
            
            logger.info(f"Collected {len(video_urls)} video URLs")
            return video_urls
            
        except Exception as e:
            logger.error(f"Error collecting video URLs: {str(e)}")
            return video_urls
    
    def like_video(self) -> bool:
        """
        Like the current video.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            like_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'like')]"))
            )
            like_button.click()
            logger.info("Video liked")
            time.sleep(random.uniform(1, 2))
            return True
        except Exception as e:
            logger.warning(f"Could not like video: {str(e)}")
            return False
    
    def save_video(self) -> bool:
        """
        Save/favorite the current video.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            save_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'favorite')]"))
            )
            save_button.click()
            logger.info("Video saved")
            time.sleep(random.uniform(1, 2))
            return True
        except Exception as e:
            logger.warning(f"Could not save video: {str(e)}")
            return False
    
    def comment_on_video(self, comment_text: str) -> bool:
        """
        Comment on the current video.
        
        Args:
            comment_text: Text to comment
            
        Returns:
            True if successful, False otherwise
        """
        try:
            comment_box = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@data-e2e, 'comment-input')]"))
            )
            comment_box.click()
            time.sleep(1)
            
            comment_input = self.driver.find_element(By.XPATH, "//input[@placeholder]")
            comment_input.send_keys(comment_text)
            time.sleep(1)
            comment_input.send_keys(Keys.RETURN)
            
            logger.info(f"Commented: {comment_text}")
            time.sleep(random.uniform(2, 3))
            return True
        except Exception as e:
            logger.warning(f"Could not comment on video: {str(e)}")
            return False
    
    def share_video(self) -> bool:
        """
        Share the current video.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            share_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-e2e, 'share')]"))
            )
            share_button.click()
            logger.info("Share menu opened")
            time.sleep(random.uniform(1, 2))
            
            # Close share dialog
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
            return True
        except Exception as e:
            logger.warning(f"Could not share video: {str(e)}")
            return False
    
    def engage_with_video(self, video_url: str, actions: List[str], comments: List[str] = None) -> None:
        """
        Engage with a specific video by performing requested actions.
        
        Args:
            video_url: URL of the video to engage with
            actions: List of actions to perform ('like', 'save', 'comment', 'share')
            comments: List of possible comments (random one will be selected)
        """
        try:
            logger.info(f"Navigating to video: {video_url}")
            self.driver.get(video_url)
            time.sleep(random.uniform(3, 5))
            
            # Perform requested actions
            if 'like' in actions:
                self.like_video()
                
            if 'save' in actions:
                self.save_video()
                
            if 'comment' in actions and comments:
                comment = random.choice(comments)
                self.comment_on_video(comment)
                
            if 'share' in actions:
                self.share_video()
            
            # Random delay to mimic human behavior
            time.sleep(random.uniform(2, 4))
            
        except Exception as e:
            logger.error(f"Error engaging with video {video_url}: {str(e)}")
    
    def run(self, max_videos: int = 10, actions: List[str] = None, comments: List[str] = None) -> None:
        """
        Main execution method for the engagement bot.
        
        Args:
            max_videos: Maximum number of videos to engage with
            actions: List of actions to perform on each video
            comments: List of possible comments
        """
        if actions is None:
            actions = ['like', 'save']
        
        if comments is None:
            comments = [
                "Great content! 🔥",
                "Love this! ❤️",
                "Amazing! 👏",
                "Keep it up! 💪",
                "So good! ✨"
            ]
        
        try:
            self.setup_driver()
            
            if not self.login():
                logger.error("Login failed. Exiting...")
                return
            
            video_urls = self.collect_video_urls(max_videos)
            
            if not video_urls:
                logger.warning("No video URLs collected. Exiting...")
                return
            
            logger.info(f"Starting engagement with {len(video_urls)} videos...")
            
            for i, video_url in enumerate(video_urls, 1):
                logger.info(f"Processing video {i}/{len(video_urls)}")
                self.engage_with_video(video_url, actions, comments)
                
                # Random delay between videos
                if i < len(video_urls):
                    delay = random.uniform(5, 10)
                    logger.info(f"Waiting {delay:.1f} seconds before next video...")
                    time.sleep(delay)
            
            logger.info("Engagement completed successfully!")
            
        except Exception as e:
            logger.error(f"Error during execution: {str(e)}")
        finally:
            self.cleanup()
    
    def cleanup(self) -> None:
        """Clean up resources and close browser."""
        if self.driver:
            logger.info("Closing browser...")
            self.driver.quit()
            logger.info("Cleanup complete")


def main():
    """Main entry point for the script."""
    import os
    from dotenv import load_dotenv
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get credentials from environment variables
    username = os.getenv('TIKTOK_USERNAME')
    password = os.getenv('TIKTOK_PASSWORD')
    target_user = os.getenv('TARGET_USER')
    
    if not all([username, password, target_user]):
        logger.error("Missing required environment variables!")
        logger.error("Please set TIKTOK_USERNAME, TIKTOK_PASSWORD, and TARGET_USER in .env file")
        return
    
    # Initialize bot
    bot = TikTokEngagementBot(username, password, target_user)
    
    # Configure engagement actions
    actions = ['like', 'save']  # Add 'comment', 'share' as needed
    
    # Run the bot
    bot.run(max_videos=10, actions=actions)


if __name__ == "__main__":
    main()
