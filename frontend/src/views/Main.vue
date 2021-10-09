<template>
  <v-row>
    <v-col cols="4">
      <city-overview-card :measurement="measurements[0]" />
    </v-col>
    <v-col cols="4">
      <city-overview-card :measurement="measurements[1]" />
    </v-col>
    <v-col cols="4">
      <city-overview-card :measurement="measurements[2]" />
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
import cityOverviewCard from "../components/city-overview-card.vue";

export default {
  components: { cityOverviewCard },
  data() {
    return {
      measurements: [
        {
          id: 1,
          city: "Rotterdam",
          measurements: { PM1: 2, PM25: 18, PM10: 35, PRESSURE: 1043 },
          airly_caqi: 34,
        },
        {
          id: 2,
          city: "Cracow",
          measurements: { PM1: 2, PM25: 18, PM10: 35, PRESSURE: 1043 },
          airly_caqi: 34,
        },
        {
          id: 3,
          city: "Rome",
          measurements: { PM1: 2, PM25: 18, PM10: 35, PRESSURE: 1043 },
          airly_caqi: 34,
        },
      ],
    };
  },
};
</script>
