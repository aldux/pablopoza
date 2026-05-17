import os

with open('c:/pablopoza/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split HTML
header_part = html.split('<main class="pt-24">')[0]
footer_part = html.split('</main>')[1]

# Modify header to add a back button instead of the full nav
nav_start = header_part.find('<nav')
nav_end = header_part.find('</nav>') + 6
new_nav = '''<nav class="flex justify-between items-center px-gutter py-4 max-w-container-max mx-auto">
<a href="index.html" class="flex items-center gap-2 hover:opacity-80 transition-opacity">
<span class="material-symbols-outlined text-primary" data-icon="arrow_back">arrow_back</span>
<span class="font-label-caps text-label-caps tracking-widest text-on-surface dark:text-on-surface">VOLVER AL INICIO</span>
</a>
</nav>'''

header_part = header_part[:nav_start] + new_nav + header_part[nav_end:]

# The articles
articles = [
    {
        'file': 'insight-1.html',
        'title': 'Por qué el 80% de los proyectos de IA fallan (y cómo evitarlo).',
        'date': '12 MAY 2024',
        'category': 'ESTRATEGIA',
        'img': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCLprtA9IJI9lRBAzLf3ydOWH3UPFOZAaeBJLAla0WBkfNmXpNfx1AajcVXqWeGMQL8nNjQ-ZgNxK4liSETHpoN5MZPb-2Bdcrslzyr_ZIU_DwKWB8zHs2TGO-D1oOhIXxbiXUZO6FjHjXhBGEDSRfleqZ5gd-bRm5jHGMiJewrdhEEszPdUOqrXGwVZ9F3ucRUyMqlP-SAhJIpA6Xv35GmM5MeAUL2smwdLs88ZXTa1VQczhp-SOymSf5ic0vHsCTT8f3Olsv4yds',
        'content': '''
        <p class="mb-6 font-body-lg text-on-surface-variant">La fiebre por la Inteligencia Artificial Generativa ha llevado a miles de corporaciones a invertir millones en pruebas de concepto (PoCs) que jamás ven la luz en producción. Según estudios recientes, cerca del 80% de estas iniciativas mueren antes de escalar. ¿El motivo? Rara vez es tecnológico; casi siempre es estratégico.</p>
        
        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">1. Desconexión con el Caso de Uso de Negocio</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">Implementar IA por el simple hecho de "tener IA" es el camino más rápido al fracaso. Las soluciones tecnológicas deben nacer como respuesta a un problema de negocio cuantificable: reducir costes operativos, aumentar la retención de clientes o minimizar riesgos. Sin un ROI claro desde el día uno, el proyecto pierde tracción ejecutiva.</p>

        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">2. Cimientos de Datos Inestables</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">Un modelo de IA es tan bueno como los datos que lo alimentan. Las corporaciones a menudo intentan construir modelos predictivos sobre bases de datos fragmentadas, sucias o aisladas en silos. La estrategia correcta exige un trabajo fundacional de gobierno y calidad de datos antes de entrenar el primer algoritmo.</p>

        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">3. Ignorar el Factor Humano (Change Management)</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">El software más brillante fracasará si los empleados no lo adoptan. La resistencia al cambio, el miedo al reemplazo y la falta de capacitación son bloqueadores masivos. La implementación de IA debe ir acompañada de un programa robusto de gestión del cambio que posicione a la IA como un "copiloto" que potencia al talento, no que lo sustituye.</p>

        <div class="mt-16 p-8 glass-card border-l-4 border-primary">
            <h4 class="font-label-caps text-primary tracking-widest mb-2">CONCLUSIÓN</h4>
            <p class="font-body-lg text-on-surface">El éxito en IA no requiere los algoritmos más complejos, sino la integración más inteligente entre tecnología, procesos y personas.</p>
        </div>
        '''
    },
    {
        'file': 'insight-2.html',
        'title': 'La era del Chief AI Officer: ¿Necesitas este perfil hoy?',
        'date': '05 MAY 2024',
        'category': 'FUTURO',
        'img': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDm0v4Z0hBAVgKkVYatRTafptgqXUR-IuFhcOEQ_LeYi-HK9Odo0wCQybOr3fi7d7qyq1TLIpIfMyB1j1m532F4e_Zs9H6mJ4THbe9G6v2xEFgvk1Ai-DnsGNC-5cv0FSqsJQEw1iS5Q_gJPzWBzFxSGnTBE7T-8KVvChH30WBSVqB1NzylNw7MnZjAq5SJpf3xO2aUPPYbHvIn5Z-bj4REceVHRnyz5i18R1pPDYWEN4NI9f4CA0kMWLEIaEl5a1UzrdikZ-1Zs1w',
        'content': '''
        <p class="mb-6 font-body-lg text-on-surface-variant">Con la maduración de los modelos fundacionales (LLMs), ha surgido un nuevo rol en la mesa directiva: el Chief AI Officer (CAIO). A diferencia del CIO (enfocado en infraestructura) o el CDO (enfocado en gobierno de datos), el CAIO se sienta en la intersección entre la innovación cognitiva y la estrategia corporativa pura.</p>
        
        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">Más allá de la Tecnología: Un Rol Transversal</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">El CAIO no es un super-ingeniero; es un estratega de negocio con un profundo entendimiento de la Inteligencia Artificial. Su principal función es identificar cómo la automatización inteligente puede transformar el modelo operativo de la empresa, gestionar los riesgos éticos y regulatorios de la IA, y evangelizar esta cultura en toda la organización.</p>

        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">¿Toda empresa necesita un CAIO?</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">La respuesta corta es no. Para empresas medianas o en fases tempranas de madurez digital, sumar un rol C-Level especializado puede generar fricción burocrática. En estos casos, empoderar al CIO/CDO actual o contratar firmas de consultoría estratégica suele ser un camino más ágil y rentable.</p>

        <div class="mt-16 p-8 glass-card border-l-4 border-primary">
            <h4 class="font-label-caps text-primary tracking-widest mb-2">EL VERDADERO DESAFÍO</h4>
            <p class="font-body-lg text-on-surface">Tengas o no un CAIO, lo que tu empresa no puede permitirse es carecer de un comité o liderazgo que dirija la gobernanza de la Inteligencia Artificial de forma centralizada y alineada a los objetivos de negocio.</p>
        </div>
        '''
    },
    {
        'file': 'insight-3.html',
        'title': 'De Big Data a Smart Data: Calidad sobre cantidad.',
        'date': '28 APR 2024',
        'category': 'TECNOLOGÍA',
        'img': 'https://lh3.googleusercontent.com/aida-public/AB6AXuBafAogqcmG6LA_S16SJo9cNQ3rxdDSefwmt6wYG9U5FmIbwUIDPRcWEGSXnSpBRuOA99feDykZQ4Flq62c9QeCkduExoUizyG8QmKK4DxdFtpMF-TWScsEqi1eHIWgfuq4N-yZSZmrH-OXkLi9bqGnoA_60IMKR5Cx4SqNRg5nYbt00pUywdwbF7wTrehFrId8wttI2Ec69EZ0jalE8jOoPh3XWrG-wIwW0b-nr2ixTQq6R-_1AjbEBfpsy41xg4KJMHGvPYG0DcI',
        'content': '''
        <p class="mb-6 font-body-lg text-on-surface-variant">Durante la última década, la promesa del "Big Data" convenció a las corporaciones de que debían recolectar y almacenar cada byte de información posible. El resultado: masivos lagos de datos (Data Lakes) que, sin gobierno ni contexto, se han convertido en "pantanos de datos" inaccesibles y costosos.</p>
        
        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">El paradigma del Smart Data</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">Hoy entendemos que el valor no reside en el volumen, sino en la calidad y la accesibilidad. El *Smart Data* se enfoca en recolectar únicamente los datos que responden a preguntas de negocio específicas. Se trata de filtrar el "ruido digital" para quedarse exclusivamente con las señales accionables que impulsan decisiones ejecutivas.</p>

        <h3 class="font-h3 text-2xl mt-12 mb-4 text-on-surface">Arquitecturas Orientadas al Valor</h3>
        <p class="mb-6 text-on-surface-variant font-body-md">Para realizar esta transición, las empresas deben adoptar arquitecturas de datos modernas como Data Mesh o Data Fabric, que tratan a los datos como *productos* en lugar de como simples subproductos de sistemas transaccionales. Un producto de datos debe ser confiable, estar documentado y ser fácilmente consumible por usuarios no técnicos y algoritmos de IA por igual.</p>

        <div class="mt-16 p-8 glass-card border-l-4 border-primary">
            <h4 class="font-label-caps text-primary tracking-widest mb-2">LA REGLA DE ORO</h4>
            <p class="font-body-lg text-on-surface">1 GB de datos limpios, gobernados y alineados a una estrategia de negocio generará más ROI que 10 Terabytes de datos desestructurados sin contexto.</p>
        </div>
        '''
    }
]

for art in articles:
    main_content = f'''
    <main class="pt-32 pb-24 px-gutter max-w-3xl mx-auto">
        <article class="reveal">
            <div class="flex items-center gap-4 text-[10px] font-label-caps text-on-surface-variant mb-6">
                <span>{art['date']}</span>
                <span class="w-1 h-1 bg-primary rounded-full"></span>
                <span>{art['category']}</span>
            </div>
            
            <h1 class="font-h1 text-4xl md:text-5xl text-on-surface mb-8">{art['title']}</h1>
            
            <div class="aspect-video w-full rounded-xl overflow-hidden mb-12 border border-white/5 shadow-2xl">
                <img src="{art['img']}" alt="{art['title']}" class="w-full h-full object-cover">
            </div>
            
            <div class="prose prose-invert prose-lg max-w-none">
                {art['content']}
            </div>
        </article>
        
        <div class="mt-24 pt-12 border-t border-white/10 text-center reveal">
            <a href="index.html" class="inline-flex items-center justify-center px-8 py-4 border border-white/20 hover:border-primary transition-all duration-300 font-label-caps text-label-caps bg-white/5 hover:bg-white/10 rounded-sm">
                VOLVER A LA PÁGINA PRINCIPAL
            </a>
        </div>
    </main>
    '''
    
    with open(f"c:/pablopoza/{art['file']}", 'w', encoding='utf-8') as f:
        f.write(header_part + main_content + footer_part)

print("Generated 3 insight files.")
