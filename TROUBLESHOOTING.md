# 🔧 Troubleshooting Guide

> **Specific error messages and their solutions for your Zola website**

---

## 🚨 Common Error Messages & Solutions

### Zola Errors

#### Error: "Failed to parse config.toml"
```
Error: Failed to parse config.toml
 --> config.toml:15:10
  |
15 | date = "2024-12-28"
  |        ^^^^^^^^^^^^
```
**Solution**: Dates should not have quotes
```toml
# Wrong
date = "2024-12-28"

# Correct
date = 2024-12-28
```

---

#### Error: "Page/Section without a date"
```
Error: Page content/my-post.md doesn't have a date
```
**Solution**: Add date to front matter
```toml
+++
title = "My Post"
date = 2024-12-28  # Add this line
+++
```

---

#### Error: "Template not found"
```
Error: Template 'custom.html' not found
```
**Solution**: 
1. Check template exists in `templates/` or `themes/radion/templates/`
2. Verify template name in front matter:
```toml
+++
template = "page.html"  # Must match actual file
+++
```

---

#### Error: "Failed to render content"
```
Error: Failed to render content of content/post.md
Reason: Invalid internal link
```
**Solution**: Fix internal link format
```markdown
# Wrong
[Link](post.md)
[Link](./post)

# Correct
[Link](@/post.md)
[Link](/post)
```

---

### Python Sync Script Errors

#### Error: "No module named 'frontmatter'"
```bash
ModuleNotFoundError: No module named 'frontmatter'
```
**Solution**: Install required Python packages
```bash
pip3 install python-frontmatter pyyaml
```

---

#### Error: "Permission denied"
```bash
PermissionError: [Errno 13] Permission denied: '/path/to/file'
```
**Solution**: Fix file permissions
```bash
chmod 755 sync_second_brain.py
chmod -R 644 content/
```

---

#### Error: "Path not found"
```python
FileNotFoundError: [Errno 2] No such file or directory: '/path'
```
**Solution**: Update paths in `sync_second_brain.py`:
```python
SECOND_BRAIN_PATH = Path("/correct/path/to/Second Brain")
WEBSITE_CONTENT_PATH = Path("/correct/path/to/my_website/content")
```

---

### Build & Deployment Errors

#### Error: "Address already in use"
```
Error: Address 127.0.0.1:1111 is already in use
```
**Solution**: Kill existing process or use different port
```bash
# Find and kill process
lsof -i :1111
kill -9 [PID]

# Or use different port
zola serve --port 8080
```

---

#### Error: "public directory not found"
```
Error: public directory does not exist
```
**Solution**: Build the site first
```bash
zola build
# Then check
ls -la public/
```

---

#### Error: "Base URL mismatch"
```
Links broken after deployment, CSS not loading
```
**Solution**: Update base_url for your deployment
```toml
# For local development
base_url = "http://127.0.0.1:1111"

# For production
base_url = "https://taslimansari.com"

# For GitHub Pages
base_url = "https://username.github.io/repo-name"
```

---

### Image & Asset Errors

#### Images Not Displaying
**Symptoms**: Broken image icons, 404 errors

**Solutions**:
1. Check image path starts with `/`:
```markdown
<!-- Wrong -->
![](images/photo.jpg)
![](./images/photo.jpg)

<!-- Correct -->
![](/images/photo.jpg)
```

2. Verify file exists:
```bash
ls -la static/images/photo.jpg
```

3. Check case sensitivity:
```bash
# Wrong: photo.JPG vs photo.jpg
# Make sure case matches exactly
```

---

#### CSS Not Loading
**Symptoms**: Site appears unstyled

**Solutions**:
1. Clear browser cache: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (PC)
2. Check theme is installed:
```bash
ls themes/radion/
```
3. Verify in config.toml:
```toml
theme = "radion"  # Must match folder name
```

---

### Search Issues

#### Search Not Working
**Symptoms**: Search box doesn't return results

**Solutions**:
1. Enable in config.toml:
```toml
build_search_index = true

[search]
index_format = "elasticlunr_json"
```

2. Rebuild site:
```bash
zola build
```

3. Check index exists:
```bash
ls public/search_index.en.json
```

---

### Content Sync Issues

#### Obsidian Links Not Converting
**Symptom**: `[[links]]` appearing in rendered site

**Solution**: Ensure sync script is running:
```bash
# Don't edit content/ files directly
# Edit in Obsidian, then:
python3 sync_second_brain.py
```

---

#### Missing Content After Sync
**Symptom**: Some files not appearing

**Check**:
1. File not in exclude list:
```python
EXCLUDE_PATTERNS = [
    "private",  # Check this list
    "drafts"
]
```

2. File has .md extension
3. File is in synced folders:
```python
SYNC_FOLDERS = {
    "writings": "writings",  # Source: Destination
}
```

---

## 🔍 Debugging Commands

### Diagnostic Commands
```bash
# Check Zola version
zola --version

# Validate configuration
zola check

# Test build without serving
zola build --output-dir test-build

# Verbose output
zola build --verbose

# Check file permissions
ls -la content/

# Find large files
find public -size +1M -type f

# Check Git status
git status --ignored
```

### Browser Debugging
1. Open Developer Tools: `F12`
2. Check Console for JavaScript errors
3. Check Network tab for 404s
4. Verify in Elements tab that HTML is correct

---

## 📊 Performance Issues

### Slow Build Times
**Solution**: Optimize images
```bash
# Find large images
find static/images -size +500k -type f

# Consider using image processing:
```
```toml
[extra]
process_images = true
image_quality = 85
```

### Slow Page Load
**Solutions**:
1. Enable minification:
```toml
[minify]
minify_html = true
minify_css = true
minify_js = true
```

2. Use lazy loading (already in photos template):
```html
<img loading="lazy" src="...">
```

---

## 🆘 When All Else Fails

### Nuclear Option - Fresh Start
```bash
# Backup current site
cp -r my_website my_website_backup

# Clean build
rm -rf public/
rm -rf .zola-cache/
zola build

# If still broken, reinstall theme
cd themes/
rm -rf radion/
git clone https://github.com/micahkepe/radion
```

### Getting Help

1. **Check Zola Docs**: [getzola.org/documentation](https://www.getzola.org/documentation/)

2. **Search the error**: Copy exact error message to Google

3. **Zola Forum**: [zola.discourse.group](https://zola.discourse.group/)

4. **GitHub Issues**: 
   - [Zola Issues](https://github.com/getzola/zola/issues)
   - [Radion Theme Issues](https://github.com/micahkepe/radion/issues)

5. **Make a minimal reproduction**:
```bash
# Create minimal test case
mkdir test-site
cd test-site
zola init
# Try to reproduce your issue
```

---

## ✅ Prevention Checklist

**Before Each Session**:
- [ ] Pull latest changes: `git pull`
- [ ] Check Zola version: `zola --version`
- [ ] Backup content: `cp -r content/ content-backup/`

**After Each Change**:
- [ ] Test locally: `zola serve`
- [ ] Check all pages load
- [ ] Verify images display
- [ ] Test on mobile view (DevTools)
- [ ] Commit to Git: `git commit -am "Description"`

**Weekly Maintenance**:
- [ ] Clear .zola-cache: `rm -rf .zola-cache/`
- [ ] Update dependencies
- [ ] Check for theme updates
- [ ] Review and optimize images
- [ ] Backup everything

---

## 📝 Error Log Template

When encountering an error, document it:

```markdown
## Error: [Brief Description]
**Date**: 2024-12-28
**Command Run**: `zola serve`
**Error Message**:
```
Exact error message here
```
**Solution**:
What fixed it

**Prevention**:
How to avoid in future
```

Keep this in `ERRORS_LOG.md` for future reference.

---

**Maker** 🔨: *"With these three documents, you have everything needed to understand, modify, and troubleshoot your website."*

**Checker** ✓: *"The documentation is comprehensive, covering architecture, daily operations, and error resolution. You're fully equipped to manage your site independently."*

---

*Troubleshooting Guide v1.0 - December 2024*
