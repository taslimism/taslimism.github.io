#!/usr/bin/env python3
"""
Sync script to convert writings from Second Brain to blog format.
Converts plain markdown files to Radion theme format with proper frontmatter.
"""

import os
import shutil
import re
from datetime import datetime
from pathlib import Path
import argparse

# Configuration
SECOND_BRAIN_PATH = "/Users/taslim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
WRITINGS_PATH = os.path.join(SECOND_BRAIN_PATH, "writings")
BLOG_CONTENT_PATH = "/Users/taslim/Desktop/my_website/content"
DRAFTS_CONTENT_PATH = "/Users/taslim/Desktop/my_website/drafts"  # Separate drafts folder

# Category mapping based on folder structure
CATEGORY_MAPPING = {
    "thoughts": "thoughts",
    "react-internals": "technical",
    "projects": "projects",
    "coding": "technical",
    # Add more mappings as needed
}

def clean_title(filename):
    """Convert filename to clean title."""
    # Remove .md extension
    title = filename.replace('.md', '')
    # Replace hyphens and underscores with spaces
    title = title.replace('-', ' ').replace('_', ' ')
    # Capitalize each word
    title = ' '.join(word.capitalize() for word in title.split())
    return title

def generate_slug(filename):
    """Generate URL-friendly slug from filename."""
    slug = filename.replace('.md', '')
    # Replace spaces and special characters with hyphens
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', slug)
    # Remove leading/trailing hyphens and convert to lowercase
    slug = slug.strip('-').lower()
    return slug

def extract_tags_from_content(content):
    """Try to extract meaningful tags from content."""
    # Simple tag extraction - you can enhance this
    words = content.lower().split()
    common_tech_terms = ['react', 'javascript', 'python', 'web', 'development', 'programming']
    common_thought_terms = ['life', 'philosophy', 'mindset', 'growth', 'reflection']
    
    tags = []
    for term in common_tech_terms + common_thought_terms:
        if term in ' '.join(words):
            tags.append(term)
    
    # Limit to 3-5 tags
    return tags[:5] if tags else ['writing']

def get_file_creation_date(filepath):
    """Get file creation date in YYYY-MM-DD format."""
    stat = os.stat(filepath)
    # Use creation time (birth time) if available, otherwise modification time
    creation_time = getattr(stat, 'st_birthtime', stat.st_mtime)
    return datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

def is_draft(filename, relative_path):
    """Check if a file should be treated as a draft."""
    # Check if filename contains 'draft'
    if 'draft' in filename.lower():
        return True
    
    # Check if it's in a drafts folder
    if 'draft' in relative_path.lower():
        return True
        
    # Check for underscore prefix (common draft convention)
    if filename.startswith('_'):
        return True
        
    return False

def add_more_tag(content):
    """Add <!-- more --> tag at appropriate position in content."""
    lines = content.split('\n')
    
    # Skip empty lines at the beginning
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip():
            content_start = i
            break
    
    # Strategy 1: Add after first paragraph (double newline)
    paragraphs = content.split('\n\n')
    if len(paragraphs) > 1 and len(paragraphs[0].strip()) > 50:
        return paragraphs[0] + '\n\n<!-- more -->\n\n' + '\n\n'.join(paragraphs[1:])
    
    # Strategy 2: Add after first 2-3 sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)
    if len(sentences) >= 3:
        # Find a good break point (2-3 sentences, but not too short)
        first_part = sentences[0]
        if len(first_part) < 100 and len(sentences) > 1:
            first_part += ' ' + sentences[1]
        if len(first_part) < 150 and len(sentences) > 2:
            first_part += ' ' + sentences[2]
            
        remaining = ' '.join(sentences[len(first_part.split('. ')):]).lstrip()
        if remaining:
            return first_part + '\n\n<!-- more -->\n\n' + remaining
    
    # Strategy 3: Add after first 200 characters at sentence boundary
    if len(content) > 300:
        break_point = content.find('.', 200)
        if break_point != -1 and break_point < 400:
            return content[:break_point+1] + '\n\n<!-- more -->\n\n' + content[break_point+1:].lstrip()
    
    # If content is short or no good break point found, don't add more tag
    return content

def generate_description(content, max_length=100):
    """Generate description from first few sentences of content."""
    # Remove any existing frontmatter if present
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'^\+\+\+.*?\+\+\+\s*', '', content, flags=re.DOTALL)
    
    # Get first sentence or first max_length characters
    sentences = content.split('.')
    if sentences and len(sentences[0]) <= max_length:
        return sentences[0].strip() + '.'
    else:
        # Truncate to max_length and add ellipsis
        truncated = content[:max_length].strip()
        if len(content) > max_length:
            truncated += '...'
        return truncated

def create_frontmatter(title, date, description, category, tags):
    """Create TOML frontmatter for Radion theme."""
    tags_str = ', '.join(f'"{tag}"' for tag in tags)
    
    frontmatter = f"""+++
title = "{title}"
date = {date}
description = "{description}"

[taxonomies]
tags = [{tags_str}]
categories = ["{category}"]
+++

"""
    return frontmatter

def process_file(source_path, relative_path, dry_run=False, include_drafts=False):
    """Process a single markdown file."""
    print(f"Processing: {relative_path}")
    
    # Read original content
    with open(source_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Skip if file is empty
    if not original_content.strip():
        print(f"  Skipping empty file: {relative_path}")
        return False
        
    # Check if this is a draft
    filename = os.path.basename(source_path)
    is_draft_file = is_draft(filename, relative_path)
    
    if is_draft_file and not include_drafts:
        print(f"  📝 Skipping draft file: {relative_path}")
        return False
    elif is_draft_file:
        print(f"  📝 Processing as draft: {relative_path}")
    
    # Extract information
    filename = os.path.basename(source_path)
    folder = os.path.dirname(relative_path) if os.path.dirname(relative_path) else "general"
    
    title = clean_title(filename)
    date = get_file_creation_date(source_path)
    category = CATEGORY_MAPPING.get(folder, folder)
    tags = extract_tags_from_content(original_content)
    description = generate_description(original_content)
    slug = generate_slug(filename)
    
    # Add <!-- more --> tag to content for better previews
    content_with_more = add_more_tag(original_content)
    
    # Create new content with frontmatter
    frontmatter = create_frontmatter(title, date, description, category, tags)
    new_content = frontmatter + content_with_more
    
    # Determine output path based on draft status
    output_filename = f"{slug}.md"
    if is_draft_file:
        # Ensure drafts directory exists
        os.makedirs(DRAFTS_CONTENT_PATH, exist_ok=True)
        output_path = os.path.join(DRAFTS_CONTENT_PATH, output_filename)
    else:
        output_path = os.path.join(BLOG_CONTENT_PATH, output_filename)
    
    print(f"  Title: {title}")
    print(f"  Date: {date}")
    print(f"  Category: {category}")
    print(f"  Tags: {tags}")
    if is_draft_file:
        print(f"  Output: drafts/{output_filename} 📝")
    else:
        print(f"  Output: content/{output_filename} ✓")
    
    # Write file (if not dry run)
    if not dry_run:
        # Check if file already exists
        if os.path.exists(output_path):
            print(f"  Warning: File already exists, will overwrite: {output_filename}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        if is_draft_file:
            print(f"  ✓ Synced to drafts: {output_filename}")
        else:
            print(f"  ✓ Synced to blog: {output_filename}")
    else:
        if is_draft_file:
            print(f"  [DRY RUN] Would create draft: {output_filename}")
        else:
            print(f"  [DRY RUN] Would create blog post: {output_filename}")
    
    print()
    return True

def sync_writings(dry_run=False, force=False, include_drafts=False):
    """Main sync function."""
    mode_info = []
    if dry_run: mode_info.append("DRY RUN")
    if include_drafts: mode_info.append("INCLUDING DRAFTS")
    
    mode_str = ": " + " + ".join(mode_info) if mode_info else ""
    print(f"Syncing writings from Second Brain to blog{mode_str}...")
    print(f"Source: {WRITINGS_PATH}")
    print(f"Target: {BLOG_CONTENT_PATH}")
    if include_drafts:
        print(f"Drafts: {DRAFTS_CONTENT_PATH}")
    print()
    
    if not os.path.exists(WRITINGS_PATH):
        print(f"Error: Writings path not found: {WRITINGS_PATH}")
        return
    
    if not os.path.exists(BLOG_CONTENT_PATH):
        print(f"Error: Blog content path not found: {BLOG_CONTENT_PATH}")
        return
    
    processed_count = 0
    
    # Walk through all markdown files in writings directory
    for root, dirs, files in os.walk(WRITINGS_PATH):
        for file in files:
            if file.endswith('.md'):
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, WRITINGS_PATH)
                
                if process_file(source_path, relative_path, dry_run, include_drafts):
                    processed_count += 1
    
    print(f"{'[DRY RUN] ' if dry_run else ''}Processed {processed_count} files.")
    
    if dry_run:
        print("\nRun without --dry-run to actually sync the files.")
    else:
        print(f"\n✓ Sync complete! Check your blog at: {BLOG_CONTENT_PATH}")

def main():
    parser = argparse.ArgumentParser(description='Sync writings from Second Brain to blog')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without actually doing it')
    parser.add_argument('--force', action='store_true',
                       help='Overwrite existing files without warning')
    parser.add_argument('--drafts', action='store_true',
                       help='Include draft files (files with "draft" in name or path)')
    
    args = parser.parse_args()
    
    sync_writings(dry_run=args.dry_run, force=args.force, include_drafts=args.drafts)

if __name__ == "__main__":
    main()
