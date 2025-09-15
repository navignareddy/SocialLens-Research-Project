const API = 'http://localhost:8000';

const input = document.getElementById('inputText');
const misinfoOut = document.getElementById('misinfoOut');
const biasOut = document.getElementById('biasOut');
const debateOut = document.getElementById('debateOut');

async function postJson(path, body) {
  const res = await fetch(`${API}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error('Request failed');
  return res.json();
}

document.getElementById('btnMisinformation').addEventListener('click', async () => {
  misinfoOut.textContent = 'Running…';
  try {
    const data = await postJson('/api/analyze/misinformation', { text: input.value });
    misinfoOut.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    misinfoOut.textContent = 'Error: ' + e.message;
  }
});

document.getElementById('btnBias').addEventListener('click', async () => {
  biasOut.textContent = 'Running…';
  try {
    const data = await postJson('/api/moderation/bias', { text: input.value });
    biasOut.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    biasOut.textContent = 'Error: ' + e.message;
  }
});

document.getElementById('btnDebate').addEventListener('click', async () => {
  debateOut.textContent = 'Running…';
  try {
    const data = await postJson('/api/debate/structure', { text: input.value });
    debateOut.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    debateOut.textContent = 'Error: ' + e.message;
  }
});


