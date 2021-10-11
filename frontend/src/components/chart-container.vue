<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import LineChart from './chart.vue'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartdata: null
  }),

  async mounted () {
    this.loaded = false
    try {
      // const { historic_measurements } = await fetch('https://airapi.airly.eu/v2/measurements/nearest?lat=50.062006&lng=19.940984&maxDistanceKM=2&maxResults=1')
      // historic_measurements_PM1 = historic_measurements["history"][1]["values"][1]["value"]
      // this.chartdata = historic_measurements
      this.chartdata = {
        labels: ['January', 'February'],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [40, 20]
            }
          ]
      };
      this.options = {
        responsive: true,
        maintainAspectRatio: false
      };
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>