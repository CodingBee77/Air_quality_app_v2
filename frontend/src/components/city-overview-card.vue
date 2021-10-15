<template>
  <!--  -->

  <v-card class="ma-4 d-flex flex-column" elevation="12" outlined>
    <v-card-title class="text-h4 justify-center">{{ cityName }}</v-card-title>
    <v-card-text class="pa-8 d-flex flex-column text-left">
      <b>Air quality data:</b>
      <br /><br />
      <ul id="measurements">
        <li v-for="index in measurements.values.slice(0, 3)" :key="index">
          <v-list-item-title class="text-h8 mb-2">
            {{ index.name }} : {{ index.value }}
          </v-list-item-title>
        </li>
      </ul>
      <br /><br />

      <measurement-info-card
        :infoText="getTemperature + '°C'"
        :imageName="'sun.jpeg'"
      />

      <measurement-info-card
        :infoText="getHumidity + '%'"
        :imageName="'humidity.jpg'"
      />
      <measurement-info-card
        :infoText="getPressure + 'hPa'"
        :imageName="'pressure.png'"
      />
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
import measurementInfoCard from "./measurement-info-card.vue";

export default {
  components: { measurementInfoCard },
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
    };
  },
  computed: {
    getTemperature: function () {
      return this.measurements.values.filter(
        (el) => el.name === "TEMPERATURE"
      )[0].value;
    },
    getPressure: function () {
      return this.measurements.values.filter((el) => el.name === "PRESSURE")[0]
        .value;
    },
    getHumidity: function () {
      return this.measurements.values.filter((el) => el.name === "HUMIDITY")[0]
        .value;
    },
    getPhoto() {
      let url = "../assets/humidity.jpg";
      return url;
    },
  },
};
</script>