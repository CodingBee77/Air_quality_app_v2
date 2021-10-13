<template>
  <v-row>
    <v-col cols="4">
      <city-overview-card :lat="'50.062006'" :long="'19.940984'" :cityName="'Cracow'" />
    </v-col>
    <v-col cols="4">
      <city-overview-card :lat="'51.920932'" :long="'4.486443'" :cityName="'Rotterdam'"  />
    </v-col>
    <v-col cols="4">
      <city-overview-card :lat="'41.891570'" :long="'12.492587'" :cityName="'Rome'"  />
    </v-col>
  </v-row>
</template>


<style scoped>
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
</style>

<script>
import axios from "axios";
import cityOverviewCard from "../components/city-overview-card.vue";

const lat = "50.062006";
const long = "19.940984";

export default {
  components: { cityOverviewCard },
  data() {
    return {
      measurements: [],
    };
  },
  async created() {
    // try {
    //   const response = await axios.get(
    //     "http://localhost:5000/api/v1/measurements/current/?lat=" +
    //       lat +
    //       "&long=" +
    //       long
    //   );
    //   this.measurements[0] = response.data;
    //   console.log(this.measurements);
    // } catch (e) {
    //   console.error(e);
    // }

    // await this.loadMeasurement();
  },
  // methods: {
  //   async loadMeasurement() {
  //     const response = await axios.get(
  //       "http://localhost:5000/api/v1/measurements/current/?lat=" +
  //         lat +
  //         "&long=" +
  //         long
  //     );

  //     this.measurements[0] = response.data;
  //   },
  // },
};
</script>
