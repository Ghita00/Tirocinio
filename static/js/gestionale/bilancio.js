const ctx = document.getElementById('myChart').getContext('2d');
let ricavi = document.getElementById('ricavi').innerHTML;
let costi = document.getElementById('costi').innerHTML;

const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Costi', 'Ricavi'],
        datasets: [{
            label: '# of Votes',
            data: [costi, ricavi],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive : true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                }
            }],
            yAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                }
            }]
        },
        plugins: {
            legend: {
                display: true,
                position: "right",
                labels: {
                    color: 'black'
                }
            },
        }
    }
});
