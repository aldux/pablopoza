import glob

old_js = "const elementsToReveal = document.querySelectorAll('h1, h2, h3, p, .glass-card');"
new_js = "const elementsToReveal = document.querySelectorAll('h1, h2, h3, p, .glass-card, .reveal');"

files_fixed = 0
for filename in glob.glob('c:/pablopoza/*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_js in content:
        content = content.replace(old_js, new_js)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        files_fixed += 1

print(f"Fixed querySelector in {files_fixed} files.")
