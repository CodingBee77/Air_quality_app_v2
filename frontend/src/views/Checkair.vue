<template>
  <div id="app" class="container mt-5 mb-5" style="width: 500px">
    <check-air @measurements="getMeasurements" />

    <v-hover v-slot="{ hover }" open-delay="200">
      <v-card
        :class="{ 'on-hover': hover }"
        class="mx-auto pa-8 mt-14"
        height="350"
        max-width="400"
      >
        <v-card-text class="text--primary mt-12 text-center text-subtitle-1">
          <span v-html="getFormatedMeasurements"></span>
        </v-card-text>
      </v-card>
    </v-hover>
  </div>
</template>


<script>
import CheckAir from "../components/check-air.vue";

export default {
  name: "Checkair",
  components: {
    CheckAir,
  },
  data() {
    return {
      currentmeasurement: {},
    };
  },
  methods: {
    getMeasurements(value) {
      this.currentmeasurement = value;
      console.dir(value);
    },
  },
  computed: {
    getFormatedMeasurements() {
      let formated_measurements = "";
      var all_measurements = this.currentmeasurement.values;
      // for (var key in all_measurements) {
      //   formated_measurements += all_measurements[key].name;
      //   formated_measurements += all_measurements[key].value + "\n";
      // }
      if (typeof all_measurements != "undefined") {
        all_measurements.forEach(function (measurement) {
          formated_measurements += measurement.name + ":" + measurement.value;
          formated_measurements += "<br/>";
        });

        return formated_measurements;
      }
    },
  },
};
</script>
