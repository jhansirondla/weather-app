const backendUrl = 'http://127.0.0.1:5001';

async function getWeather() {
    const location = document.getElementById('location').value;
    const output = document.getElementById('weatherResult');
    output.innerText = 'Loading...';
  
    try {
      const res = await fetch(`${backendUrl}/weather`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ location })
      });
  
      const data = await res.json();
  
      if (data.error) {
        output.innerText = `Error: ${data.error}`;
      } else {
        output.innerText = `Location: ${data.location}, Temp: ${data.temp}°C, ${data.description}`;
      }
  
      await loadSaved();  // safe to run now
  
    } catch (error) {
      output.innerText = 'Failed to fetch weather data.';
      console.error(error);
    }
  }
  
async function loadSaved() {
    try {
      const res = await fetch(`${backendUrl}/weather`);
      const data = await res.json();
  
      const list = document.getElementById('savedList');
      list.innerHTML = '';
  
      data.forEach(entry => {
        const li = document.createElement('li');
        li.innerText = `#${entry.id} - ${entry.location}: ${entry.temperature}°C`;
        list.appendChild(li);
      });
    } catch (error) {
      console.error('Failed to load saved data:', error);
    }
}
  

async function updateEntry() {
  const id = document.getElementById('updateId').value;
  const newTemp = document.getElementById('updateTemp').value;

  const res = await fetch(`${backendUrl}/weather/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ temperature: newTemp })
  });

  const data = await res.json();
  alert(data.message || data.error);
  loadSaved();
}

async function deleteEntry() {
  const id = document.getElementById('deleteId').value;

  const res = await fetch(`${backendUrl}/weather/${id}`, {
    method: 'DELETE'
  });

  const data = await res.json();
  alert(data.message || data.error);
  loadSaved();
}
