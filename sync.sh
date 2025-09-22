#!/bin/bash
# Simple wrapper script for syncing writings

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYNC_SCRIPT="$SCRIPT_DIR/sync_writings.py"

echo "🧵 Weaver & 🔨 Maker: Syncing your writings to blog format..."
echo

# Check if Python script exists
if [ ! -f "$SYNC_SCRIPT" ]; then
    echo "Error: sync_writings.py not found in $SCRIPT_DIR"
    exit 1
fi

# Run the Python script with any passed arguments
python3 "$SYNC_SCRIPT" "$@"

echo
echo "💡 Usage examples:"
echo "  ./sync.sh --dry-run    # Preview what will be synced"
echo "  ./sync.sh              # Actually sync the files"
echo "  ./sync.sh --force      # Overwrite existing files"
echo "  ./sync.sh --drafts     # Include draft files"
echo "  ./sync.sh --dry-run --drafts  # Preview including drafts"
