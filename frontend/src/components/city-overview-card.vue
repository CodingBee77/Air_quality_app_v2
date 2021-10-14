<template>
  <!--  -->
  <v-card class="full-height d-flex flex-column" elevation="10" outlined>
    <v-card-title class="justify-center">{{ cityName }}</v-card-title>
    <v-card-text class="pa-8 d-flex flex-column text-left">
      <b>Air quality data:</b>
      <br /><br />
      <p>{{ measurements.values }}</p>
    </v-card-text>

    <v-spacer></v-spacer>
    <v-card-actions>
      <router-link
        :to="{
          name: 'Detail',
          params: { lat: lat, long: long, cityName: cityName },
        }"
        tag="button"
        class="card-actions"
      >
        <v-col class="text-right">
          <v-btn elevation="10">Explore</v-btn>
        </v-col>
      </router-link>
    </v-card-actions>
  </v-card>
</template>

<style>
.full-height {
  margin: auto;
  margin-top: 80px;
  height: 120%;
  width: 80%;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  background: linear-gradient(
    180deg,
    rgba(65, 195, 203, 1) 0%,
    rgba(122, 193, 190, 1) 14%,
    rgba(195, 214, 214, 1) 100%
  );
  text-align: center;
}
.card-actions {
  position: relative;
  bottom: 0;
}
</style>

<script>
import axios from "axios";

export default {
  name: "CityCard",
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
    // measurements: {
    //   type: Object,
    //   default: () => {},
    // },
  },
  async mounted() {
    try {
      const response = await axios.get(
        "http://localhost:5000/api/v1/measurements/current/?lat=" +
          this.lat +
          "&long=" +
          this.long
      );
      this.measurements = response.data;
      console.log(this.measurements);
    } catch (e) {
      console.error(e);
    }
  },
  data() {
    return {
      measurements: {},
      clonedMeasurement: { ...this.measurements },
    };
  },
};
</script>