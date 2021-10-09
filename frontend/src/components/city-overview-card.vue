<template>
  <v-card class="full-height d-flex flex-column" elevation="10" outlined>
    <v-card-title class="justify-center">{{
      clonedMeasurement.city
    }}</v-card-title>
    <v-card-text class="pa-8 d-flex flex-column text-left">
      Air quality data: {{ clonedMeasurement.measurements }}
    </v-card-text>
    <v-spacer></v-spacer>

    <v-card-actions>
      <router-link
        :to="{ name: 'Detail', params: { city: clonedMeasurement.city } }"
        tag="button"
        class="link card-footer-item"
      >
        <i class="fas fa-check"></i>
        <span>More</span>
      </router-link>
      <!-- <v-btn color="primary" outlined text :to="{ name: 'detail', params: { id: hero.id } }"> More </v-btn> -->
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
</style>

<script>
export default {
  name: "CityCard",
  props: {
    measurement: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      clonedMeasurement: { ...this.measurement },
    };
  },
};
</script>