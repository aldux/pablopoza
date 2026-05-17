import glob

old_js = """    const carousel = document.getElementById('trayectoria-carousel');
    if (!carousel) return;
    
    let scrollInterval;
    const startScroll = () => {
      scrollInterval = setInterval(() => {
        const isAtEnd = carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10;
        if (isAtEnd) {
          carousel.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
          carousel.scrollBy({ left: carousel.clientWidth * 0.8, behavior: 'smooth' });
        }
      }, 3500);
    };

    startScroll();
    
    carousel.addEventListener('mouseenter', () => clearInterval(scrollInterval));
    carousel.addEventListener('mouseleave', startScroll);
    carousel.addEventListener('touchstart', () => clearInterval(scrollInterval), {passive: true});
    carousel.addEventListener('touchend', startScroll, {passive: true});"""

new_js = """    const carousel = document.getElementById('trayectoria-carousel');
    if (carousel) {
        let scrollInterval;
        const startScroll = () => {
          scrollInterval = setInterval(() => {
            const isAtEnd = carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10;
            if (isAtEnd) {
              carousel.scrollTo({ left: 0, behavior: 'smooth' });
            } else {
              carousel.scrollBy({ left: carousel.clientWidth * 0.8, behavior: 'smooth' });
            }
          }, 3500);
        };

        startScroll();
        
        carousel.addEventListener('mouseenter', () => clearInterval(scrollInterval));
        carousel.addEventListener('mouseleave', startScroll);
        carousel.addEventListener('touchstart', () => clearInterval(scrollInterval), {passive: true});
        carousel.addEventListener('touchend', startScroll, {passive: true});
    }"""

files_fixed = 0
for filename in glob.glob('c:/pablopoza/*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_js in content:
        content = content.replace(old_js, new_js)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        files_fixed += 1

print(f"Fixed JS in {files_fixed} files.")
