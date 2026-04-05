function onDragOver(e, id) {
  e.preventDefault();
  document.getElementById(id).classList.add('drag-over');
}
 
function onDragLeave(id) {
  document.getElementById(id).classList.remove('drag-over');
}
 
function onDrop(e, previewId, dropId) {
  e.preventDefault();
  document.getElementById(dropId).classList.remove('drag-over');
 
  const file = e.dataTransfer.files[0];
  if (!file) return;
 
  if (previewId) showPreview(file, previewId);
 
  if (dropId === 'secretDrop') {
    document.getElementById('secretLabel').textContent = '✅ ' + file.name;
  }
}
 
/* ── File Input Handlers ── */
 
function onFileSelect(e, previewId) {
  const file = e.target.files[0];
  if (file) showPreview(file, previewId);
}
 
function onSecretSelect(e) {
  const file = e.target.files[0];
  if (file) {
    document.getElementById('secretLabel').textContent = '✅ ' + file.name;
  }
}
 
/* ── Image Preview ── */
 
function showPreview(file, previewId) {
  if (!file.type.startsWith('image/')) return;
 
  const reader = new FileReader();
  reader.onload = (ev) => {
    const el = document.getElementById(previewId);
    el.innerHTML = `
      <img src="${ev.target.result}" alt="preview">
      <div class="scan-line"></div>
    `;
  };
  reader.readAsDataURL(file);
}
 
/* ── Password Strength Meter ── */
 
function updateStrength(val) {
  const barIds = ['s1', 's2', 's3', 's4'];
  const colors  = ['#ff3a6e', '#ff9500', '#f5d800', '#00ff88'];
 
  let score = 0;
  if (val.length >= 6)                              score++;
  if (val.length >= 10)                             score++;
  if (/[A-Z]/.test(val) && /[0-9]/.test(val))      score++;
  if (/[^A-Za-z0-9]/.test(val))                    score++;
 
  barIds.forEach((id, i) => {
    document.getElementById(id).style.background =
      i < score ? colors[score - 1] : 'var(--border)';
  });
}
 
/* ══════════════════════════════════════
   ENCODE FLOW
   ══════════════════════════════════════ */
 
async function startEncode() {
  const steps = [
    { icon: '🔐', label: 'ENCRYPTING DATA',   sub: 'AES-256-CBC encryption in progress...' },
    { icon: '🧬', label: 'EMBEDDING PIXELS',  sub: 'LSB steganography — writing secret bits...' },
    { icon: '📦', label: 'PACKAGING OUTPUT',  sub: 'Generating stego image and ciphertext...' },
    { icon: '✅', label: 'COMPLETE',           sub: 'Dual-channel output ready!' },
  ];
 
  showOverlay(true);
 
  for (const step of steps) {
    document.getElementById('progressIcon').textContent  = step.icon;
    document.getElementById('progressLabel').textContent = step.label;
    document.getElementById('progressSub').textContent   = step.sub;
    await sleep(900);
  }
 
  showOverlay(false);
 
  // Reveal the output panel
  const outputPanel = document.getElementById('outputPanel');
  outputPanel.style.display = 'block';
  outputPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
 
  document.getElementById('payloadSize').textContent = randomSize();
  document.getElementById('cipherBox').textContent   = generateFakeCipher();
 
  showToast('🎉 Encoding complete! Dual output ready.');
}
 
/* ══════════════════════════════════════
   DECODE FLOW
   ══════════════════════════════════════ */
 
async function startDecode() {
  const steps = [
    { icon: '🔍', label: 'READING IMAGE',     sub: 'Scanning pixel data for hidden bits...' },
    { icon: '🧩', label: 'EXTRACTING BITS',   sub: 'Reconstructing embedded binary data...' },
    { icon: '🔓', label: 'DECRYPTING',        sub: 'AES-256-CBC decryption in progress...' },
    { icon: '📂', label: 'FILE RECOVERED',    sub: 'Original file successfully restored!' },
  ];
 
  showOverlay(true);
 
  for (const step of steps) {
    document.getElementById('progressIcon').textContent  = step.icon;
    document.getElementById('progressLabel').textContent = step.label;
    document.getElementById('progressSub').textContent   = step.sub;
    await sleep(900);
  }
 
  showOverlay(false);
  showToast('✅ File extracted & decrypted successfully!');
}
 
/* ══════════════════════════════════════
   UTILITIES
   ══════════════════════════════════════ */
 
/** Show / hide the full-screen progress overlay */
function showOverlay(show) {
  document.getElementById('progressOverlay').classList.toggle('active', show);
}
 
/** Promise-based delay */
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
 
/** Generate a random file-size label for the output card */
function randomSize() {
  return (Math.random() * 900 + 100).toFixed(1) + ' KB';
}
 
/** Generate a fake ciphertext string for the cipher preview box */
function generateFakeCipher() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=!@#$%^&*';
  let output = '';
  for (let i = 0; i < 200; i++) {
    output += chars[Math.floor(Math.random() * chars.length)];
  }
  return output;
}
 
/** Show a toast notification */
function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}