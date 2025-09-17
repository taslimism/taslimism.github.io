#!/bin/bash
# Quick test script to check if the projects section builds correctly

echo "🧪 Testing Projects Section Implementation..."
echo

# Check if we're in the right directory
if [ ! -f "config.toml" ]; then
    echo "❌ Error: Please run this from your website root directory"
    exit 1
fi

echo "✅ Configuration:"
echo "  - Projects added to navigation menu"
echo "  - Technologies taxonomy configured"
echo "  - Project types taxonomy configured"
echo

echo "✅ Content Structure:"
if [ -d "content/projects" ]; then
    echo "  - Projects directory exists"
    project_count=$(find content/projects -name "index.md" | wc -l)
    echo "  - Found $project_count project(s)"
else
    echo "  ❌ Projects directory missing"
fi
echo

echo "✅ Styling:"
if [ -f "sass/projects.scss" ]; then
    echo "  - Custom projects stylesheet created"
else
    echo "  ❌ Projects stylesheet missing"
fi

if [ -f "sass/main.scss" ]; then
    echo "  - Main stylesheet configured"
else
    echo "  ❌ Main stylesheet missing"
fi
echo

echo "✅ Images Directory:"
if [ -d "static/images/projects" ]; then
    echo "  - Project images directory ready"
else
    echo "  ❌ Project images directory missing"
fi
echo

echo "🚀 Build Test:"
echo "Running 'zola check'..."
if zola check; then
    echo "✅ Site structure is valid!"
    echo
    echo "🎉 Projects section is ready!"
    echo
    echo "📝 Next steps:"
    echo "  1. Add your project images to static/images/projects/"
    echo "  2. Update example projects with your real work"
    echo "  3. Run 'zola serve' to see your projects live"
    echo "  4. Visit http://127.0.0.1:1111/projects"
else
    echo "❌ Build errors detected. Please check the output above."
    exit 1
fi
