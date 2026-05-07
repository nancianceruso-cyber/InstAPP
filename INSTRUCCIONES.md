# Mis Saves — Guía de instalación

## Qué vas a lograr
Una PWA instalada en tu celular que aparece en el menú "Compartir" de Instagram.
Cuando compartís un reel o post → la app se abre con el link ya cargado.

---

## Paso 1 — Subir el código a GitHub

1. Entrá a https://github.com y creá una cuenta gratuita (si no tenés).
2. Hacé clic en **"New repository"** (botón verde arriba a la derecha).
3. Nombre: `mis-saves` → clic en **"Create repository"**.
4. En la página del repo, hacé clic en **"uploading an existing file"**.
5. Subí TODOS los archivos de esta carpeta:
   - `public/index.html`
   - `public/manifest.json`
   - `public/sw.js`
   - `public/icon-192.png`
   - `public/icon-512.png`
   - `vercel.json`
6. Clic en **"Commit changes"**.

---

## Paso 2 — Publicar en Vercel (gratis)

1. Entrá a https://vercel.com y hacé clic en **"Sign up"**.
2. Elegí **"Continue with GitHub"** → autorizá.
3. Clic en **"Add New Project"** → seleccioná el repo `mis-saves`.
4. En la configuración:
   - **Framework Preset**: Other
   - **Root Directory**: `public`
5. Clic en **"Deploy"** → en 1 minuto ya está publicada.
6. Vercel te da una URL del tipo: `https://mis-saves-abc123.vercel.app`

---

## Paso 3 — Instalar en tu celular (Android)

1. Abrí Chrome en tu celular.
2. Entrá a la URL de Vercel que te dieron.
3. Chrome va a mostrar un banner **"Agregar a pantalla de inicio"** → tocalo.
   - Si no aparece: tocá los 3 puntitos (menú) → "Agregar a pantalla de inicio".
4. Confirmá con **"Agregar"**.

¡Listo! La app aparece como ícono en tu pantalla de inicio.

---

## Paso 3 — Instalar en tu celular (iPhone)

1. Abrí **Safari** (importante: tiene que ser Safari, no Chrome).
2. Entrá a la URL de Vercel.
3. Tocá el ícono de compartir (cuadrado con flecha hacia arriba).
4. Tocá **"Agregar a pantalla de inicio"**.
5. Tocá **"Agregar"**.

---

## Paso 4 — Usar desde Instagram

### Android:
1. Abrí un reel o post en Instagram.
2. Tocá el ícono de **compartir** (flechita debajo del corazón).
3. En el menú de compartir del sistema, buscá **"Mis Saves"**.
   - La primera vez puede tardar un poco en aparecer.
4. Tocala → la app se abre con el link ya cargado.
5. Completá título, categoría y puntuación → Guardar.

### iPhone:
En iOS el Share Target de PWA tiene soporte limitado. 
La forma más práctica es:
1. Copiar el link del post (tocar los 3 puntitos → Copiar link).
2. Abrir la app desde la pantalla de inicio.
3. Pegar el link en el campo correspondiente.

---

## Tus datos
Los datos se guardan en el almacenamiento local del celular (localStorage).
Usá el botón "Exportar" para hacer un backup en CSV en cualquier momento.

---

## ¿Preguntas?
Si algo no funciona, revisá que:
- La URL de Vercel esté bien copiada.
- Estés usando Chrome (Android) o Safari (iPhone) para instalar.
- La app esté instalada desde la pantalla de inicio (no solo guardada como favorito).
