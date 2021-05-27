const labels = device_data.map(d => d.data);
const values = device_data.map(d => d.value);
const data = {
  labels: labels,
  datasets: [{
    label: data_type,
    backgroundColor: 'rgb(2, 117, 216)',
    borderColor: 'rgb(2, 117, 216)',
    data: values
  }]
};
const config = {
  type: 'line',
  data: data,
}
var myChart = new Chart(
    document.getElementById('chartCanvas').getContext('2d'),
    config
);