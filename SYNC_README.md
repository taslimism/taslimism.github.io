# Writing Sync Scripts

**Checker ✓ & Maker 🔨** have created a sync system to convert your Second Brain writings into blog-ready format for the Radion theme.

## What the Scripts Do

### 🧵 **Smart Conversion Process:**
- Scans all `.md` files in your `writings/` folder (including subdirectories)
- Uses **file creation date** as the writing date (not sync date!)
- Generates clean titles from filenames
- Auto-detects categories based on folder structure:
  - `thoughts/` → "thoughts" category
  - `react-internals/` → "technical" category
- Extracts relevant tags from content
- **✨ NEW: Adds `<!-- more -->` tags** for blog post previews
- **📝 NEW: Draft system** - skips files with "draft" in name/path
- Creates proper TOML frontmatter for Radion theme
- Generates URL-friendly slugs

### 📝 **Draft Management:**
- Files with "draft" in filename are treated as drafts
- Files in folders containing "draft" are treated as drafts  
- Files starting with `_` are treated as drafts
- Drafts are saved to `/drafts/` folder (separate from published content)
- Use `--drafts` flag to include drafts in sync

### ✨ **Preview Generation:**
- Automatically adds `<!-- more -->` tag for post previews
- Smart placement: after first paragraph or 2-3 sentences
- Ensures good break points for reader engagement
- Short posts (under 300 chars) don't get more tags

### 📁 **File Structure:**
```
writings/
├── thoughts/
│   ├── content.md → becomes "content.md" with "thoughts" category
│   └── doglapan.md → becomes "doglapan.md" with "thoughts" category
└── react-internals/
    └── intro to rerenders.md → becomes "intro-to-rerenders.md" with "technical" category
```

## Usage

### 1. **Preview First (Recommended):**
```bash
cd /Users/taslim/Desktop/my_website
python3 sync_writings.py --dry-run
```
*This shows what will be created without actually doing it*

### 2. **Actually Sync:**
```bash
python3 sync_writings.py
```

### 3. **Include Drafts:**
```bash
python3 sync_writings.py --drafts        # Sync drafts to /drafts/ folder
python3 sync_writings.py --dry-run --drafts  # Preview drafts
```

### 4. **Using the Shell Wrapper:**
```bash
./sync.sh --dry-run         # Preview published content only
./sync.sh                   # Sync published content
./sync.sh --drafts          # Include drafts  
./sync.sh --dry-run --drafts # Preview everything including drafts
./sync.sh --force           # Overwrite existing files
```

## Example Output Format

Your writing files get converted from:
```markdown
consuming content is a deeply personal thing...
```

To blog format:
```markdown
+++
title = "Content"
date = 2025-08-24
description = "consuming content is a deeply personal thing. our liking is shaped by our experiences in life..."

[taxonomies]
tags = ["writing", "life", "philosophy"]
categories = ["thoughts"]
+++

consuming content is a deeply personal thing. our liking is shaped by our experiences in life. people who have never consumed art which resonated with them, never build taste and never truly enjoy art.

<!-- more -->

they can never watch a movie before looking at their imdb ratings, cannot enjoy songs by not so mainstream artists...
```

## Safety Features

✓ **Dry-run mode** to preview changes  
✓ **File existence warnings** before overwriting  
✓ **Preserves original creation dates**  
✓ **Skips empty files**  
✓ **Handles special characters in filenames**  
✓ **Draft protection** - keeps unfinished work separate  
✓ **Smart preview breaks** - won't break mid-sentence  
✓ **Separate draft folder** - `/drafts/` vs `/content/`  

## Customization

Edit these sections in `sync_writings.py`:

### Add New Categories:
```python
CATEGORY_MAPPING = {
    "thoughts": "thoughts",
    "react-internals": "technical",
    "your-new-folder": "your-category",  # Add this
}
```

### Modify Tag Detection:
```python
common_tech_terms = ['react', 'javascript', 'python', 'web', 'development', 'programming']
common_thought_terms = ['life', 'philosophy', 'mindset', 'growth', 'reflection']
```

## Regular Usage

Run this whenever you add new writings or want to update existing blog posts:

```bash
# Check what's new (published content only)
./sync.sh --dry-run

# Sync published content  
./sync.sh

# Work with drafts
./sync.sh --dry-run --drafts  # See drafts too
./sync.sh --drafts            # Sync drafts to /drafts/
```

### 📝 **Draft Workflow:**
1. Create files like `draft-my-idea.md` or put them in `writings/drafts/`
2. Use `./sync.sh --drafts` to sync them to `/drafts/` folder  
3. When ready to publish, rename file (remove "draft") and run normal sync
4. Drafts stay separate from your published blog content

The script is designed to be run regularly - it will handle both new files and updates to existing ones.

---
*Created by the Think Center Council - Weaver 🧵 for strategy, Maker 🔨 for execution, Checker ✓ for quality assurance*
