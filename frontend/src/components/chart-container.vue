<template>
  <div class="container">
    <line-chart v-if="loaded" :chartdata="chartdata" :options="options" />
  </div>
</template>


<script>
import LineChart from "./chart.vue";

export default {
  name: "LineChartContainer",
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartdata: null,
  }),

  async mounted() {
    this.loaded = false;
    try {
      // const { historic_measurements } = await fetch('https://airapi.airly.eu/v2/measurements/nearest?lat=50.062006&lng=19.940984&maxDistanceKM=2&maxResults=1')
      // historic_measurements_PM1 = historic_measurements["history"][1]["values"][1]["value"]
      // this.chartdata = historic_measurements
      this.chartdata = {
        labels: ["January", "February", "March"],
        datasets: [
          {
            label: "PM1",
            backgroundColor: "#51B8A9A8",
            data: [40, 20, 30],
          },
          {
            label: "PM25",
            backgroundColor: "#5FA833A8",
            data: [50, 10, 60],
          },
        ],
      };
      this.options = {
        // responsive: false,
        maintainAspectRatio: false,
        title: {
          display: true,
          text: "History air quality data - 1 DAY",
        },
        tooltips: {
          callbacks: {
            label(tooltipItem, chartdata) {
              // Get the dataset label.
              const label = chartdata.datasets[tooltipItem.datasetIndex].label;

              // Format the y-axis value.
              const value = tooltipItem.yLabel;

              return `${label}: ${value}`;
            },
          },
        },
      };
      this.loaded = true;
    } catch (e) {
      console.error(e);
    }
  },
};
</script>