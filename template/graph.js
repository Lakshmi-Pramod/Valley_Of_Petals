document.addEventListener('DOMContentLoaded', function () {
  // Manually code the exportRates and costPerHectare arrays based on marketvalue table data
  const exportRates = [500000.0, 750000.0, 600000.0, 450000.0, 700000.0, 550000.0, 800000.0, 650000.0, 900000.0, 600000.0, 750000.0, 500000.0, 850000.0, 700000.0, 950000.0, 800000.0, 600000.0, 750000.0, 500000.0, 700000.0];
  const costPerHectare = [200.0, 300.0, 250.0, 180.0, 280.0, 220.0, 320.0, 260.0, 360.0, 240.0, 300.0, 200.0, 340.0, 280.0, 380.0, 320.0, 240.0, 300.0, 200.0, 280.0];

  // Retrieve unique flora names from the flora table
  const countryNamesQueryResult = [
    'Rhododendron arboreum', 'Cedrus deodara', 'Prunus cerasoides', 'Aconitum heterophyllum', 'Saussurea obvallata',
    'Juniperus indica', 'Rheum australe', 'Abies spectabilis', 'Anaphalis triplinervis', 'Taxus wallichiana',
    'Swertia chirayita', 'Ephedra gerardiana', 'Primula denticulata', 'Arnebia euchroma', 'Bergenia ciliata',
    'Saraca asoca', 'Pedicularis hoffmeisteri', 'Viola biflora', 'Paeonia emodi', 'Buddleja crispa'
  ];

  // Create a bar graph for Export Rates using Chart.js
  const ctxExport = document.getElementById('flowerExportChart').getContext('2d');
  const flowerExportChart = new Chart(ctxExport, {
    type: 'bar',
    data: {
      labels: countryNamesQueryResult,
      datasets: [{
        label: 'Export Rates',
        data: exportRates,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  // Create a bar graph for Cost per Hectare using Chart.js
  const ctxCost = document.getElementById('costPerHectareChart').getContext('2d');
  const costPerHectareChart = new Chart(ctxCost, {
    type: 'bar',
    data: {
      labels: countryNamesQueryResult,
      datasets: [{
        label: 'Cost per Hectare',
        data: costPerHectare,
        backgroundColor: 'rgba(255, 99, 132, 0.2)', // Adjust color as needed
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});