#!/bin/bash

echo ""
echo "Starting Development Tools Check..."

# Check Homebrew
echo ""
echo "Let's check with Homebrew..."
if brew --version >/dev/null 2>&1; then
    echo "Homebrew installed with version: $(brew --version)"
else
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check Git
echo ""
echo "Let's check with Git..."
if git --version >/dev/null 2>&1; then
    echo "Git installed with version: $(git --version)"
else
    echo "Git not found. Installing..."
    brew install git
    echo ""
    echo "Congrats!!! Git successfully installed with version: $(git --version)"
fi

# Check Python
echo ""
echo "Let's check with Python..."
if python3 --version >/dev/null 2>&1; then
    echo "Python installed with version: $(python3 --version)"
else
    echo "Python not found. Installing..."
    brew install python
    echo ""
    echo "Congrats!!! Python successfully installed with version: $(python3 --version)"
    echo "Congrats!!! pip also installed as pip comes along with python in unix with pip version: $(pip3 --version)"
fi

# Check node
echo ""
echo "Let's check with nodejs..."
if node --version >/dev/null 2>&1; then
    echo "Nodejs installed with version: $(node --version)"
else
    echo "Nodejs not found. Installing..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
    \. "$HOME/.nvm/nvm.sh"
    nvm install 24
    echo ""
    echo "Congrats!!! Nodejs successfully installed with version: $(node --version)"
    echo "node package manager installed with version: $(npm --version)"
    echo "node version manager version: $(nvm --version)"
fi

# Check Docker
echo ""
echo "Let's check with Docker..."
if docker --version >/dev/null 2>&1; then
    echo "docker desktop is installed with version: $(docker --version)"
else
    echo "docker not found. Installing..."
    softwareupdate --install-rosetta
    brew install --cask docker
    echo ""
    echo "Congrats!!! Docker is successfully installed with version: $(docker --version)"  
fi

echo ""
echo "all checks are completed! well done!"
echo ""