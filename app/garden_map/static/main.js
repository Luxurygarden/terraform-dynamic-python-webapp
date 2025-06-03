const map = L.map('map').setView([50.0615, 19.9366], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

fetch('/services')
  .then(resp => resp.json())
  .then(data => {
      data.forEach(service => {
          L.marker([service.lat, service.lng])
            .addTo(map)
            .bindPopup(`<b>${service.name}</b><br>${service.description}`);
      });
  })
  .catch(err => console.error(err));
