<template>
  <v-row>
    <v-col cols="4">
      <city-overview-card :lat="'50.062006'" :long="'19.940984'" :cityName="'Cracow'" />
    </v-col>
    <v-col cols="4">
      <city-overview-card :lat="'51.920932'" :long="'4.486443'" :cityName="'Rotterdam'"  />
    </v-col>
    <v-col cols="4">
      <city-overview-card :lat="'41.906551'" :long="'12.453617'" :cityName="'Rome'"  />
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
      measurements: [],
    };
  },
};
</script>
