import glob
import re

# 1. Update gakudo.html buttons
gakudo_path = 'c:/EAKids-Portal/gakudo.html'
with open(gakudo_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the quick-access-grid
new_grid = '''<div class="quick-access-grid">
                <a href="assets/docs/rules/rules_gakudo.pdf" target="_blank" class="quick-card">
                    <i class="fas fa-file-pdf" style="color: #e74c3c;"></i>
                    <h3 style="font-size: 1.1rem;">繧ｬ繧ｯ繝峨え縺ｮ豎ｺ縺ｾ繧・/h3>
                    <p>PDF繧帝幕縺・/p>
                </a>
                
                <a href="https://sites.google.com/view/eakids-clil-topic-k-song/%E3%83%9B%E3%83%BC%E3%83%A0/clil%E3%83%88%E3%83%94%E3%83%83%E3%82%AF" target="_blank" class="quick-card">
                    <i class="fas fa-chalkboard-teacher" style="color: #3498db;"></i>
                    <h3 style="font-size: 1.1rem;">CLIL繝医ヴ繝・け</h3>
                    <p>螟夜Κ繧ｵ繧､繝医∈</p>
                </a>

                <a href="assets/docs/calendar/calendar_2_gakudo.pdf" target="_blank" class="quick-card">
                    <i class="fas fa-calendar-alt" style="color: #2ecc71;"></i>
                    <h3 style="font-size: 1.1rem;">繧ｬ繧ｯ繝峨え繧ｫ繝ｬ繝ｳ繝繝ｼ</h3>
                    <p>PDF繧帝幕縺・/p>
                </a>

                <a href="https://www.eiken.or.jp/eiken-junior/" target="_blank" class="quick-card">
                    <i class="fas fa-award" style="color: #f1c40f;"></i>
                    <h3 style="font-size: 1.1rem;">闍ｱ讀廱r.縺ｮ縺顔衍繧峨○</h3>
                    <p>螟夜Κ繧ｵ繧､繝医∈</p>
                </a>

                <a href="https://cambridgecentre.jp/exams/yle/" target="_blank" class="quick-card">
                    <i class="fas fa-globe-europe" style="color: #9b59b6;"></i>
                    <h3 style="font-size: 1.05rem; line-height: 1.4;">繧ｱ繝ｳ繝悶Μ繝・ず繝､繝ｳ繧ｰ繝ｩ繝ｼ繝翫・繧ｺ<br>闍ｱ隱樊､懷ｮ・YLE)縺ｮ縺顔衍繧峨○</h3>
                    <p>螟夜Κ繧ｵ繧､繝医∈</p>
                </a>
            </div>
        </section>'''

content = re.sub(r'<div class="quick-access-grid">[\s\S]*?</section>', new_grid, content)

with open(gakudo_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Add password protection script to gakudo and all gamerize pages
pwd_script = '''    <script>
        // Password protection for this page
        if (sessionStorage.getItem('auth_pages') !== 'eakids123') {
            document.documentElement.style.display = 'none'; // Hide content while prompting
            let pwd = prompt('縺薙・繝壹・繧ｸ縺ｮ髢ｲ隕ｧ縺ｫ縺ｯ繝代せ繝ｯ繝ｼ繝峨′蠢・ｦ√〒縺吶・);
            if (pwd === 'eakids123') {
                sessionStorage.setItem('auth_pages', 'eakids123');
                document.documentElement.style.display = ''; // Show content
            } else {
                alert('繝代せ繝ｯ繝ｼ繝峨′髢馴＆縺｣縺ｦ縺・∪縺吶ゅ・繝ｼ繝繝壹・繧ｸ縺ｫ謌ｻ繧翫∪縺吶・);
                window.location.href = 'index.html';
            }
        }
    </script>
</head>'''

protected_files = glob.glob('c:/EAKids-Portal/gamerize*.html') + [gakudo_path]
for file in protected_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid adding multiple times
    if 'auth_pages' not in content:
        content = content.replace('</head>', pwd_script)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print('Updated gakudo and added password protection!')

