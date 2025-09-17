+++
title = "Read [Invent With Python Books](https://inventwithpython.com/) with readable line length"
description = "A useful chrome-extension that makes your online reading experience better"
date = 2025-08-31
updated = 2025-08-31

[extra]
# Project links and status
github_url = "https://github.com/taslimism/read_better"
# demo_url = "https://asciinema.org/a/demo-file-organizer"  # Add your real demo URL here
status = "completed"
featured = true
featured_image = "/images/projects/cli-organizer-demo.gif"

# Project details
tech_stack = ["JS"]
project_type = "chrome-extension"
duration = "1 day"
team_size = 1
role = "Developer"

[taxonomies]
tags = ["chrome-extension", "javscript", "book-reader"]
categories = ["projects"]
+++

## 📚 Overview

A Chrome extension that transforms online programming books into comfortable, distraction-free reading experiences. Specifically optimized for "Automate the Boring Stuff with Python" and other books on automatetheboringstuff.com, making long reading sessions easier on your eyes.

<!-- more -->

## 🎯 Purpose

Online programming books often have poor typography with lines that stretch across the entire screen, making them difficult to read. This extension applies research-backed readability improvements to create an experience similar to well-designed ebooks or Medium articles.

## ✨ Features

### Core Reading Improvements

- **Optimal Line Length**: Constrains text to ~700px width (approximately 65-75 characters per line)
- **Professional Typography**: Georgia serif font for body text, improving readability for long-form content
- **Generous Spacing**: 1.8x line height reduces eye strain during extended reading
- **Dark Mode**: Perfect for late-night coding sessions or reducing eye fatigue
- **Adjustable Font Size**: Scale from 14px to 24px based on your preference

### Smart Features

- **Auto-Activation**: Reading mode enables automatically on supported sites
- **Persistent Settings**: Remembers your preferences across sessions
- **Clean Layout**: Removes distractions while preserving navigation
- **Code Block Enhancement**: Improved formatting and contrast for code examples
- **Smooth Transitions**: Elegant animations when toggling modes

## 🔧 Technical Details

### Architecture

- **Content Script**: Injects CSS and manages reading mode state
- **Popup Interface**: Clean settings panel with toggle switches
- **Chrome Storage API**: Saves user preferences persistently
- **CSS Override System**: Uses `!important` declarations to ensure consistent styling

### Typography Choices

- **Body Font**: Georgia (serif) - Better for sustained reading
- **Headers**: System fonts (San Francisco, Segoe UI) - Clear hierarchy
- **Code**: Consolas/Monaco (monospace) - Optimal for code readability
- **Line Height**: 1.8 - Research shows this reduces reading fatigue

### Color Schemes

#### Light Mode

- Background: `#f9f7f4` (Warm off-white)
- Text: `#333` (Soft black)
- Links: `#4a90e2` (Accessible blue)
- Code Background: `#f5f5f5`

#### Dark Mode

- Background: `#1a1a1a`
- Container: `#2a2a2a`
- Text: `#e0e0e0`
- Links: `#6db3f2`
- Code Background: `#1e1e1e`

## 📁 Project Structure

```
better-book-reader/
├── manifest.json       # Extension configuration
├── content.css        # Reading mode styles
├── content.js        # State management & settings
├── popup.html       # Settings interface
├── popup.js        # Popup functionality
└── README.md      # Documentation
```

## 🚀 Installation

### Quick Install

1. Open Chrome → `chrome://extensions/`
2. Enable **"Developer mode"** (top-right toggle)
3. Click **"Load unpacked"**
4. Select this folder: `/Users/taslim/Desktop/fun_projects/my_chrome_extensions/better-book-reader`
5. Visit https://automatetheboringstuff.com/3e/chapter1.html
6. Enjoy comfortable reading! 📖

### First Use

- Extension activates automatically on supported sites
- Click the extension icon to access settings
- Toggle dark mode with one click
- Adjust font size with the slider

## 💡 Usage Tips

### Keyboard Reading

- Use arrow keys to navigate between sections
- Space bar for page-down scrolling
- Combine with browser zoom for additional control

### Best Settings

- **Daytime**: Light mode, 18px font
- **Night**: Dark mode, 16-20px font
- **Large Monitor**: 20-22px font
- **Laptop**: 16-18px font

## 🎨 Design Philosophy

### Research-Based Decisions

1. **Line Length**: 45-75 characters is optimal for reading comprehension
2. **Serif Fonts**: Guide the eye along text lines, crucial for technical content
3. **Warm Background**: Reduces harsh contrast compared to pure white
4. **Generous Spacing**: Prevents line confusion and reduces cognitive load

### User Experience Principles

- **Zero Configuration**: Works immediately after installation
- **Respectful Defaults**: Enhances without disrupting
- **User Control**: Every aspect is customizable
- **Performance**: Minimal impact on page load

## 📊 Impact Metrics

### Before Extension

- Line length: 120-150+ characters
- Font: System default (often Arial/Helvetica)
- Line height: 1.2-1.4x
- Full-width layout
- No reading optimization

### After Extension

- Line length: 65-75 characters ✅
- Font: Georgia serif (optimized for reading) ✅
- Line height: 1.8x (reduces eye strain) ✅
- Centered, focused layout ✅
- Dark mode option ✅

## 🔄 Version History

### v1.0.0 (Current)

- Initial release
- Core reading mode functionality
- Dark mode support
- Font size adjustment
- Auto-activation on automatetheboringstuff.com

## 🚧 Roadmap

### Planned Features

- [ ] Support for more programming book sites
- [ ] Customizable color themes
- [ ] Reading progress tracking
- [ ] Bookmark functionality
- [ ] Export to PDF with formatting
- [ ] Multiple font choices
- [ ] Reading time estimates
- [ ] Syntax highlighting improvements

### Potential Sites to Support

- [ ] Real Python tutorials
- [ ] MDN Web Docs
- [ ] Python.org documentation
- [ ] Other Al Sweigart books
- [ ] Free programming books on GitHub

## 🐛 Known Issues

- Font size changes require page refresh on some pages
- Navigation menu might need manual adjustment on some chapters

## 🤝 Credits

### Created by

**Maker** 🔨 - Taslim Raza Ansari

### Inspired by

- Medium's reading experience
- Safari Reader Mode
- Research on typography and readability

## 📝 License

Personal project for educational and productivity purposes

## 🏷️ Tags

`chrome-extension` `reading-mode` `typography` `python-books` `productivity` `accessibility`

---

_Making technical books as pleasant to read as they are valuable to learn from_ 📚
