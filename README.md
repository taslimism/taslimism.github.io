# 📚 Complete Website Documentation - Taslim Ansari's Personal Site

> **A comprehensive guide to understanding and modifying every aspect of this Zola-powered personal website**

---

## 🏗️ Architecture Overview

This website is built with **Zola** (a fast static site generator written in Rust) and uses the **Radion** theme with custom modifications. It features automatic content synchronization from your Obsidian Second Brain vault.

### Technology Stack

- **Static Site Generator**: Zola v0.18.0+
- **Theme**: Radion (customized)
- **Content Management**: Obsidian vault sync via Python
- **Styling**: SCSS/CSS with dark/light mode support
- **Search**: ElasticLunr.js
- **Syntax Highlighting**: One-Dark theme
- **Mathematical Notation**: MathJax (LaTeX support)

---

## 📁 Complete Directory Structure & Purpose

```
my_website/
│
├── 📄 config.toml                 # Main site configuration
├── 📄 sync_second_brain.py        # Python script for Obsidian sync
├── 📄 DETAILED_README.md          # This file - comprehensive guide
│
├── 📂 content/                    # All website content (Markdown files)
│   ├── _index.md                  # Homepage content configuration
│   ├── about.md                   # About page
│   ├── getting-started.md        # Getting started guide
│   ├── hello-world.md             # Sample blog post
│   └── 📂 photos/                 # Photo gallery section
│       ├── _index.md              # Photos section config
│       └── *.md                   # Individual photo entries
│
├── 📂 public/                     # Generated site (created by 'zola build')
│   ├── index.html                 # Generated homepage
│   ├── site.css                   # Compiled CSS
│   ├── search_index.en.json      # Search index
│   ├── 📂 js/                     # JavaScript files
│   │   ├── codeblock.js           # Code snippet functionality
│   │   ├── init-theme.js          # Theme initialization
│   │   ├── mathjax-config.js     # Math rendering config
│   │   ├── search.js              # Search functionality
│   │   └── toggle-theme.js       # Dark/light mode toggle
│   └── 📂 icons/                  # Site icons and favicons
│
├── 📂 static/                     # Static assets (copied directly to public/)
│   ├── favicon-readme.txt        # Favicon documentation
│   └── 📂 images/                 # Image storage
│       ├── README.md              # Images folder guide
│       └── photos-setup-guide.txt # Photo gallery setup
│
├── 📂 templates/                  # Custom page templates
│   └── photos.html                # Photo gallery template
│
├── 📂 sass/                       # Custom SCSS files (if any)
│
└── 📂 themes/                     # Installed themes
    └── 📂 radion/                 # Radion theme files
        ├── config.toml            # Theme configuration
        ├── 📂 templates/          # Theme templates
        ├── 📂 sass/               # Theme styles
        └── 📂 static/             # Theme static assets
```

---

## ⚙️ Configuration Files Explained

### 1. **config.toml** - Main Site Configuration

```toml
# Site URL - CRITICAL: Change this for production deployment
# base_url = "https://taslimansari.com"  # Your domain

# Basic Site Information
title = "Taslim Ansari"               # Browser title
description = "My place on the internet" # Meta description

# Theme Selection
theme = "radion"                      # Using Radion theme

# Features
build_search_index = true              # Enable search functionality
generate_feeds = true                  # Generate RSS/Atom feeds

# Content Organization (Taxonomies)
taxonomies = [
  { name = "tags", feed = true },     # Enable tags with RSS
  { name = "categories", feed = true }, # Enable categories with RSS
]

# Markdown Processing
[markdown]
highlight_code = true                  # Enable syntax highlighting
highlight_theme = "one-dark"           # Code theme (one-dark, monokai, etc.)
insert_anchor_links = "heading"        # Add anchor links to headings

# Search Configuration
[search]
index_format = "elasticlunr_json"      # Search index format

# Theme-Specific Settings
[extra]
author = "Taslim Ansari"              # Your name

# Social Links
github = "https://github.com/yourusername" # UPDATE THIS!

# Navigation Menu (order matters!)
radion_menu = [
  { url = "$BASE_URL/", name = "Home" },
  { url = "$BASE_URL/photos", name = "Photos" },
  { url = "$BASE_URL/categories", name = "Categories" },
  { url = "$BASE_URL/tags", name = "Tags" },
  { url = "$BASE_URL/about", name = "About" },
]

# Feature Toggles
codeblock = true                       # Copy-to-clipboard for code
latex = true                           # LaTeX math support
enable_search = true                   # Search bar
theme = "toggle"                       # Theme mode: "light", "dark", "auto", "toggle"
favicon = false                        # Show favicon
comments = false                       # Giscus comments (needs setup)
revision_history = false               # Git revision history
```

---

## 📝 Content Management

### Content File Structure

Every content file needs **front matter** (metadata) at the top:

```markdown
+++
title = "Your Post Title"              # Required
date = 2024-12-28                      # Required for blog posts
description = "Brief description"      # Optional but recommended
draft = false                          # Set true to hide from site
weight = 0                             # Sort order (lower = earlier)
slug = "custom-url"                    # Custom URL path
aliases = ["/old-url"]                 # Redirect old URLs here

[taxonomies]
tags = ["tag1", "tag2"]                # Post tags
categories = ["category1"]             # Post categories

[extra]
author = "Taslim Ansari"              # Override default author
toc = true                             # Show table of contents
comments = true                        # Enable comments for this page
+++

Your content goes here in Markdown format...
```

### Content Types & Locations

1. **Blog Posts**: `content/` (root level)

   - Automatically listed on homepage
   - Sorted by date

2. **Photo Gallery**: `content/photos/`

   - Each photo needs a `.md` file
   - Example photo entry:

   ```markdown
   +++
   title = "Sunset at the Beach"
   date = 2024-12-28
   description = "Beautiful sunset captured at Santa Monica"
   [extra]
   image = "/images/sunset-beach.jpg"  # Path to image
   process_image = true                # Enable image processing
   +++
   ```

3. **About Page**: `content/about.md`

   - Single page, not a blog post
   - No date required

4. **Custom Sections**: Create folders in `content/`
   - Each folder needs `_index.md`
   - Example: `content/projects/_index.md`

## 🎨 Styling & Theme Customization

### CSS Variables (Dark/Light Mode)

Edit in `themes/radion/templates/_base.html` or create override in `sass/custom.scss`:

```css
:root {
	/* Light mode colors */
	--background: #ffffff;
	--text-color: #1a1a1a;
	--link-color: #0066cc;
	--code-bg: #f5f5f5;
}

[data-theme="dark"] {
	/* Dark mode colors */
	--background: #1a1a1a;
	--text-color: #e5e5e5;
	--link-color: #66b3ff;
	--code-bg: #2d2d2d;
}
```

### Custom CSS

Add custom styles in `sass/custom.scss`:

```scss
// Import theme styles
@import "../themes/radion/sass/site";

// Your custom styles
.custom-class {
	// Your styles
}

// Mobile responsive
@media (max-width: 768px) {
	.custom-class {
		// Mobile styles
	}
}
```

---

## 🖼️ Photo Gallery Management

### Adding Photos

1. **Add image file**: Place in `static/images/`
2. **Create content file**: `content/photos/photo-name.md`

```markdown
+++
title = "Mountain Sunrise"
date = 2024-12-28
description = "Early morning hike to capture the sunrise"
weight = 10  # Display order

[taxonomies]
tags = ["nature", "mountains", "sunrise"]

[extra]
image = "/images/mountain-sunrise.jpg"
location = "Rocky Mountains, Colorado"
camera = "Canon EOS R5"
settings = "f/8, 1/250s, ISO 100"
process_image = true  # Enable Zola image processing
+++

Optional story or description about the photo...
```

### Photo Gallery Template Customization

Edit `templates/photos.html`:

```html
<!-- Masonry Layout Settings -->
<style>
	.photos-masonry {
		column-count: 4; /* Desktop columns */
		column-gap: 1rem; /* Space between columns */
	}

	/* Tablet view */
	@media (max-width: 1200px) {
		.photos-masonry {
			column-count: 3;
		}
	}

	/* Mobile view */
	@media (max-width: 768px) {
		.photos-masonry {
			column-count: 2;
		}
	}
</style>
```

---

## 🚀 Development Workflow

### Local Development

```bash
# 1. Start development server (auto-reload on changes)
zola serve
# Visit: http://127.0.0.1:1111

# 2. Build with drafts visible
zola serve --drafts

# 3. Test production build
zola build
# Then serve the public/ directory:
python3 -m http.server 8000 --directory public
```

### Common Development Tasks

#### Adding a New Blog Post

```bash
# 1. Create new post
echo '+++
title = "My New Post"
date = 2024-12-28
+++

Content here...' > content/my-new-post.md

# 2. Preview
zola serve
```

#### Adding a New Section

```bash
# 1. Create section directory
mkdir content/projects

# 2. Create section index
echo '+++
title = "Projects"
sort_by = "weight"
template = "section.html"
+++' > content/projects/_index.md

# 3. Add to navigation (edit config.toml)
```

#### Modifying Templates

1. **Override theme template**: Copy from `themes/radion/templates/` to `templates/`
2. **Edit the copy**: Your version takes precedence
3. **Test changes**: `zola serve`

---

## 🔍 Search Functionality

### Search Configuration

The site uses ElasticLunr for client-side search:

1. **Enable in config.toml**: `build_search_index = true`
2. **Search index location**: `public/search_index.en.json`
3. **Search script**: `public/js/search.js`

### Customizing Search

Edit search behavior in `themes/radion/static/js/search.js`:

```javascript
// Search configuration
const searchConfig = {
	boost: {
		title: 2, // Title importance
		description: 1, // Description importance
		content: 1, // Content importance
	},
	searchCutoff: 0.1, // Minimum relevance score
};
```

---

## 🔧 Advanced Customizations

### Adding Shortcodes

Create in `templates/shortcodes/`:

```html
<!-- templates/shortcodes/youtube.html -->
<div class="video-wrapper">
	<iframe src="https://www.youtube.com/embed/{{ id }}" allowfullscreen>
	</iframe>
</div>
```

Use in content:

```markdown
{{ youtube(id="dQw4w9WgXcQ") }}
```

### Custom Page Templates

Create in `templates/`:

```html
<!-- templates/custom-page.html -->
{% extends "index.html" %} {% block content %}
<h1>{{ page.title }}</h1>
{{ page.content | safe }} {% endblock %}
```

Use in front matter:

```toml
+++
template = "custom-page.html"
+++
```

### Adding Comments (Giscus)

1. **Setup Giscus**: Visit [giscus.app](https://giscus.app)
2. **Get configuration**
3. **Update config.toml**:

```toml
[extra.giscus]
enabled = true
repo = "username/repo"
repo_id = "..."
category = "..."
category_id = "..."
```

---

## 🚢 Deployment

### GitHub Pages

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        uses: shalzz/zola-deploy-action@v0.17.2
        env:
          PAGES_BRANCH: gh-pages
          TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Netlify

```toml
# netlify.toml
[build]
command = "zola build"
publish = "public"

[build.environment]
ZOLA_VERSION = "0.18.0"

[[redirects]]
from = "/old-url"
to = "/new-url"
status = 301
```

### Custom Domain Setup

1. **Update base_url**: `base_url = "https://yourdomain.com"`
2. **Build**: `zola build`
3. **Deploy public/ folder**
4. **DNS settings**: Point domain to hosting

---

## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue                   | Solution                                         |
| ----------------------- | ------------------------------------------------ |
| **Images not showing**  | Check paths start with `/` not `./`              |
| **Sync script fails**   | Verify Python path and file permissions          |
| **Styles not updating** | Clear browser cache, hard refresh (Ctrl+Shift+R) |
| **Search not working**  | Ensure `build_search_index = true` in config     |
| **404 on pages**        | Check `base_url` matches deployment URL          |
| **Dates showing wrong** | Use format: `date = 2024-12-28`                  |
| **Theme not loading**   | Run `git submodule update --init`                |

### Debug Commands

```bash
# Check Zola version
zola --version

# Validate configuration
zola check

# Build with verbose output
zola build --verbose

# Test specific page
zola serve --open
```

---

## 📊 Performance Optimization

### Image Optimization

Use Zola's built-in image processing:

```markdown
{% set image = resize_image(path="image.jpg", width=800, op="fit_width", quality=85) %}
<img src="{{ image.url }}" alt="Description">
```

### Minification

```toml
# config.toml
[minify]
minify_html = true
minify_css = true
minify_js = true
```

### Lazy Loading

Already implemented for images in photo gallery:

```html
<img loading="lazy" src="..." />
```

---

## 🔐 Security Considerations

### Sensitive Files

Never commit these files:

- API keys
- Personal information
- Passwords
- Private notes

Add to `.gitignore`:

```
# Sensitive files
*.key
*.secret
private/
.env
```

### Content Security

Review all synced content for:

- Personal information
- API keys in code examples
- Private URLs
- Sensitive screenshots

---

## 📚 Resources & References

### Official Documentation

- [Zola Documentation](https://www.getzola.org/documentation/)
- [Tera Template Engine](https://tera.netlify.app/)
- [Radion Theme](https://github.com/micahkepe/radion)

### Useful Tools

- [Markdown Guide](https://www.markdownguide.org/)
- [TOML Spec](https://toml.io/)
- [SCSS Documentation](https://sass-lang.com/documentation)

### Community

- [Zola Forum](https://zola.discourse.group/)
- [Zola GitHub](https://github.com/getzola/zola)

---

## 🎯 Quick Reference Cheatsheet

```bash
# Essential Commands
zola serve              # Start dev server
zola build              # Build for production
zola check              # Validate site

# Python Sync
python3 sync_second_brain.py  # Sync Obsidian content

# Git Commands
git add .               # Stage changes
git commit -m "msg"     # Commit
git push                # Deploy (if using CI/CD)

# File Locations Quick Reference
config.toml             # Main config
content/                # Your content
static/                 # Images, files
templates/              # Custom templates
public/                 # Built site
themes/radion/          # Theme files
```

---

## 💡 Pro Tips

1. **Always test locally** before deploying
2. **Keep backups** of your content
3. **Use drafts** (`draft = true`) for work-in-progress
4. **Optimize images** before uploading (max 1920px wide)
5. **Write front matter first**, content second
6. **Use tags consistently** for better organization
7. **Check mobile view** regularly
8. **Monitor build size** - keep under 100MB for fast loads

_Last updated: September 2025_
_Version: 1.0.0_
