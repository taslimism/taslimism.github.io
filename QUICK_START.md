# 🚀 Quick Start Guide - Common Tasks

> **For Taslim - Your go-to reference for everyday website operations**

---

## 📝 Adding New Content

### 1. Quick Blog Post
```bash
# Create a new blog post
cat > content/my-new-post.md << 'EOF'
+++
title = "Your Post Title Here"
date = 2024-12-28
description = "Brief description for previews"
[taxonomies]
tags = ["thoughts", "tech"]
categories = ["blog"]
+++

Write your content here in Markdown...

## Subheading

Your text...
EOF

# Preview it
zola serve
```

### 2. Adding a Photo to Gallery
```bash
# Step 1: Add image to static folder
cp ~/Downloads/your-photo.jpg static/images/

# Step 2: Create photo entry
cat > content/photos/your-photo.md << 'EOF'
+++
title = "Photo Title"
date = 2024-12-28
description = "What this photo is about"
[extra]
image = "/images/your-photo.jpg"
location = "Where taken"
camera = "Camera used"
+++

Story behind the photo (optional)...
EOF
```

### 3. Sync from Obsidian
```bash
# Run sync script
python3 sync_second_brain.py

# Preview changes
zola serve

# If happy, build
zola build
```

---

## 🎨 Quick Style Changes

### Change Site Colors
Edit `config.toml`:
```toml
[extra]
# Add custom color scheme
primary_color = "#8b5cf6"  # Purple
secondary_color = "#f59e0b" # Orange
```

### Change Font
Add to `sass/custom.scss`:
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

body {
    font-family: 'Inter', sans-serif;
}
```

---

## 🔄 Daily Workflow

### Morning Routine
```bash
# 1. Navigate to website folder
cd ~/Desktop/my_website

# 2. Sync latest from Obsidian
python3 sync_second_brain.py

# 3. Start dev server
zola serve

# 4. Make edits as needed
# 5. Build when ready
zola build
```

### Adding Content from Obsidian
1. Write in Obsidian as normal
2. Run: `python3 sync_second_brain.py`
3. Check with: `zola serve`
4. Deploy with: `zola build`

---

## 🚨 Quick Fixes

### Images Not Showing
```markdown
<!-- Wrong -->
<img src="./images/photo.jpg">
<img src="images/photo.jpg">

<!-- Correct -->
<img src="/images/photo.jpg">
```

### Date Format Issues
```toml
# Wrong
date = "2024-12-28"
date = "28-12-2024"

# Correct
date = 2024-12-28  # No quotes!
```

### Link Format
```markdown
<!-- Internal link -->
[About](/about)
[Another post](@/my-post.md)

<!-- External link -->
[GitHub](https://github.com)
```

---

## 📋 Pre-Deployment Checklist

- [ ] Run `zola check` - no errors?
- [ ] Update `base_url` in `config.toml`
- [ ] Test all links work
- [ ] Check images load
- [ ] Verify mobile view
- [ ] Clear browser cache and test
- [ ] Run `zola build`
- [ ] Test `public/` folder locally

---

## 🎯 Most Used Commands

```bash
# Development
zola serve                    # Start dev server
zola serve --drafts          # Include draft posts
zola serve --open            # Open in browser

# Building
zola build                   # Build site
zola build --base-url https://example.com  # Custom URL

# Checking
zola check                   # Validate config
ls -la public/              # Check build output

# Syncing
python3 sync_second_brain.py # Sync Obsidian

# Git
git status                   # Check changes
git add .                    # Stage all
git commit -m "Update"       # Commit
git push                     # Push to GitHub
```

---

## 📝 Content Templates

### Standard Blog Post
```markdown
+++
title = "Title"
date = 2024-12-28
description = "Description"
[taxonomies]
tags = ["tag1", "tag2"]
categories = ["category"]
+++

## Introduction

Your content...

## Main Points

1. Point one
2. Point two

## Conclusion

Final thoughts...
```

### Photo Entry
```markdown
+++
title = "Photo Title"
date = 2024-12-28
description = "Brief description"
[extra]
image = "/images/filename.jpg"
location = "Location"
camera = "Camera Model"
settings = "f/8, 1/250s, ISO 100"
+++

Optional story...
```

### Page (Not a Post)
```markdown
+++
title = "Page Title"
template = "page.html"
+++

Content without date...
```

---

## 🔗 Important Paths

| What | Where |
|------|-------|
| **Main Config** | `config.toml` |
| **Content** | `content/` |
| **Images** | `static/images/` |
| **Generated Site** | `public/` |
| **Sync Script** | `sync_second_brain.py` |
| **Custom CSS** | `sass/custom.scss` |
| **Templates** | `templates/` |
| **Theme** | `themes/radion/` |

---

## 💬 Council Integration

Add perspective markers to posts:

```markdown
+++
title = "Strategic Planning"
date = 2024-12-28
[extra]
perspective = "weaver"  # or "maker" or "checker"
+++

🧵 **Weaver perspective**: Looking at the big picture...
```

---

## 🆘 Emergency Contacts

- **Zola Issues**: [Forum](https://zola.discourse.group/)
- **Theme Issues**: Check `themes/radion/README.md`
- **Sync Issues**: Check Python version with `python3 --version`

---

**Remember**: 
- Always `zola serve` before `zola build`
- Keep backups of your content
- Test on mobile regularly
- Commit to Git frequently

---

*Quick Guide Version 1.0 - December 2024*
