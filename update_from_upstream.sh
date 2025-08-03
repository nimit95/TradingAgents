#!/bin/bash

# Script to update TradingAgents from upstream while preserving local changes

echo "🔄 Updating TradingAgents from upstream..."

# Check if there are any uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo "📦 Stashing local changes..."
    git stash push -m "Auto-stash before pulling upstream"
    STASHED=true
else
    STASHED=false
fi

# Pull latest changes from upstream
echo "⬇️  Pulling latest changes from upstream..."
git pull origin main

# Restore stashed changes if any
if [[ "$STASHED" == "true" ]]; then
    echo "📦 Restoring local changes..."
    git stash pop
fi

echo "✅ Update complete!"
echo "📋 Current status:"
git status --short 