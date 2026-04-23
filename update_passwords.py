import glob

old_script = '''    <script>
        // Password protection for this page
        if (sessionStorage.getItem('auth_pages') !== 'eakids123') {
            document.documentElement.style.display = 'none'; // Hide content while prompting
            let pwd = prompt('このページの閲覧にはパスワードが必要です。');
            if (pwd === 'eakids123') {
                sessionStorage.setItem('auth_pages', 'eakids123');
                document.documentElement.style.display = ''; // Show content
            } else {
                alert('パスワードが間違っています。ホームページに戻ります。');
                window.location.href = 'index.html';
            }
        }
    </script>
</head>'''

new_script = '''    <script>
        // Password protection for this page (Prompt every time)
        document.documentElement.style.display = 'none'; // Hide content while prompting
        let pwd = prompt('このページの閲覧にはパスワードが必要です。');
        if (pwd === 'eakids123') {
            document.documentElement.style.display = ''; // Show content
        } else {
            alert('パスワードが間違っています。ホームページに戻ります。');
            window.location.href = 'index.html';
        }
    </script>
</head>'''

# Update existing protected files
protected_files = glob.glob('c:/EAKids-Portal/gamerize*.html') + ['c:/EAKids-Portal/gakudo.html']
for file in protected_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_script in content:
        content = content.replace(old_script, new_script)
    elif new_script not in content:
        # Just in case it wasn't added properly before
        content = content.replace('</head>', new_script)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Add to documents.html
doc_file = 'c:/EAKids-Portal/documents.html'
with open(doc_file, 'r', encoding='utf-8') as f:
    content = f.read()

if new_script not in content and old_script not in content:
    content = content.replace('</head>', new_script)
elif old_script in content:
    content = content.replace(old_script, new_script)

with open(doc_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated password protection scripts!')
