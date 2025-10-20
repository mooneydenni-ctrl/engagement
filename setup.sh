#!/bin/bash
# Setup script for TikTok Engagement Bot

echo "=================================="
echo "TikTok Engagement Bot - Setup"
echo "=================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher before running this script."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ Error: pip is not installed."
    echo "Please install pip before running this script."
    exit 1
fi

echo "✓ pip found"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to create virtual environment."
    exit 1
fi

echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to activate virtual environment."
    exit 1
fi

echo "✓ Virtual environment activated"
echo ""

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies."
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env file and add your credentials:"
    echo "   - TIKTOK_USERNAME"
    echo "   - TIKTOK_PASSWORD"
    echo "   - TARGET_USER"
else
    echo "✓ .env file already exists"
fi

echo ""
echo "=================================="
echo "✅ Setup complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your credentials"
echo "2. Activate virtual environment: source venv/bin/activate"
echo "3. Run the bot: python tiktok_engagement.py"
echo "   or try examples: python example_usage.py"
echo ""
