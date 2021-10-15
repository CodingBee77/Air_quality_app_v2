<template>
  <div class="container">
    <line-chart v-if="loaded" :chartdata="chartdata" :options="options" />
  </div>
</template>


<script>
import LineChart from "./chart.vue";
import axios from "axios";

export default {
  name: "LineChartContainer",
  props: {
    lat: {
      type: String,
    },
    long: {
      type: String,
    },
    cityName: {
      type: String,
    },
  },
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartdata: null,
  }),
  async mounted() {
    this.loaded = false;
    try {
      const response = await axios.get(
        "api/v1/measurements/history/?lat=" +
          this.lat +
          "&long=" +
          this.long
      );
      this.chartdata = response.data;
      console.log(this.chartdata);
    } catch (e) {
      console.error(e);
    }
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
  },
};
</script>