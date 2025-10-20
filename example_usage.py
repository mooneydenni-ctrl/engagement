#!/usr/bin/env python3
"""
Example usage of the TikTok Engagement Bot

This script demonstrates how to use the TikTokEngagementBot class
with different configurations.
"""

from tiktok_engagement import TikTokEngagementBot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def example_basic_engagement():
    """Example: Basic engagement with like and save actions only."""
    print("=== Example 1: Basic Engagement ===\n")
    
    bot = TikTokEngagementBot(
        username=os.getenv('TIKTOK_USERNAME'),
        password=os.getenv('TIKTOK_PASSWORD'),
        target_user=os.getenv('TARGET_USER')
    )
    
    # Run with default actions (like and save)
    bot.run(max_videos=5, actions=['like', 'save'])


def example_full_engagement():
    """Example: Full engagement with all available actions."""
    print("\n=== Example 2: Full Engagement ===\n")
    
    bot = TikTokEngagementBot(
        username=os.getenv('TIKTOK_USERNAME'),
        password=os.getenv('TIKTOK_PASSWORD'),
        target_user=os.getenv('TARGET_USER')
    )
    
    # Custom comments
    custom_comments = [
        "This is amazing! 🔥",
        "Love your content! ❤️",
        "Keep creating! 💪",
        "Incredible work! ⭐",
        "Can't get enough! 🎉"
    ]
    
    # Run with all actions
    bot.run(
        max_videos=10,
        actions=['like', 'save', 'comment', 'share'],
        comments=custom_comments
    )


def example_custom_workflow():
    """Example: Custom workflow with manual control."""
    print("\n=== Example 3: Custom Workflow ===\n")
    
    bot = TikTokEngagementBot(
        username=os.getenv('TIKTOK_USERNAME'),
        password=os.getenv('TIKTOK_PASSWORD'),
        target_user=os.getenv('TARGET_USER')
    )
    
    try:
        # Setup
        bot.setup_driver(headless=False)
        
        # Login
        if not bot.login():
            print("Login failed!")
            return
        
        # Collect videos
        video_urls = bot.collect_video_urls(max_videos=5)
        
        # Engage with each video
        for url in video_urls:
            print(f"Engaging with: {url}")
            bot.engage_with_video(
                video_url=url,
                actions=['like', 'save'],
                comments=["Great content!"]
            )
        
        print("Engagement complete!")
        
    finally:
        bot.cleanup()


def example_like_only():
    """Example: Only like videos, no other actions."""
    print("\n=== Example 4: Like Only ===\n")
    
    bot = TikTokEngagementBot(
        username=os.getenv('TIKTOK_USERNAME'),
        password=os.getenv('TIKTOK_PASSWORD'),
        target_user=os.getenv('TARGET_USER')
    )
    
    # Only perform like action
    bot.run(max_videos=15, actions=['like'])


if __name__ == "__main__":
    # Check if credentials are set
    if not all([
        os.getenv('TIKTOK_USERNAME'),
        os.getenv('TIKTOK_PASSWORD'),
        os.getenv('TARGET_USER')
    ]):
        print("Error: Please set TIKTOK_USERNAME, TIKTOK_PASSWORD, and TARGET_USER")
        print("in your .env file before running this example.")
        exit(1)
    
    print("TikTok Engagement Bot - Usage Examples")
    print("=" * 50)
    print("\nChoose an example to run:")
    print("1. Basic Engagement (like + save)")
    print("2. Full Engagement (all actions)")
    print("3. Custom Workflow (manual control)")
    print("4. Like Only")
    print("\n0. Exit")
    
    choice = input("\nEnter your choice (0-4): ").strip()
    
    examples = {
        '1': example_basic_engagement,
        '2': example_full_engagement,
        '3': example_custom_workflow,
        '4': example_like_only
    }
    
    if choice in examples:
        examples[choice]()
    elif choice == '0':
        print("Exiting...")
    else:
        print("Invalid choice!")
