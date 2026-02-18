#!/usr/bin/env python3
import sys
import os

# Add the current directory to path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orchestrator import ContentOrchestrator

import sys
import os
import json
from pathlib import Path

# Add the current directory to path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orchestrator import ContentOrchestrator

def load_latest_news():
    scrapper_output = Path(__file__).parent.parent.parent / "binance_news_scrapper" / "binance_all_news.json"
    if scrapper_output.exists():
        with open(scrapper_output, "r") as f:
            data = json.load(f)
            posts = data.get("posts", [])
            if posts:
                print(f"Loaded {len(posts)} posts from scrapper output.")
                return posts[0] # Return the first one as an example
    return None

def main():
    print("\n" + "="*40)
    print("   Fintech Monster Content Engine   ")
    print("="*40 + "\n")
    
    news_item = load_latest_news()
    
    if not news_item:
        print("No news found in scrapper output. Using default example.")
        news_item = {
            "title": "Example Fintech News",
            "text": "Breaking: A major fintech startup just raised $100M in Series C."
        }
    else:
        print(f"Target News: {news_item.get('title', 'Unknown Title')}")

    input("\nPress Enter to start the multi-persona pipeline...")
    
    orchestrator = ContentOrchestrator()
    final_post = orchestrator.run_pipeline(news_item)
    
    if final_post:
        print("\n" + "="*40)
        print("   FINAL POST COMPLETED   ")
        print("="*40)
        print(final_post)
        
        save_choice = input("\nSave to content folder? (y/n): ").lower().strip()
        if save_choice == 'y':
            # Logic to save as .md in content/startups/
            print("Saving logic to be implemented...")
    else:
        print("\nPipeline stopped or rejected.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
