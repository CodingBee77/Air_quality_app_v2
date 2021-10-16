<template>
  <h1 class="pt-0">
    <v-container class="blue lighten-5">
      <v-row dense>
        <v-spacer>
          <v-card class="pa-0" outlined tile>
            <div>
              <chart-history-container
                :lat="this.lat"
                :long="this.long"
                :cityName="this.cityName"
              />
            </div>
          </v-card>
        </v-spacer>
      </v-row>

      <v-row>
        <v-col v-for="n in 6" :key="n" cols="sm">
          <v-card class="pa-16" outlined tile raised> col </v-card>
        </v-col>
      </v-row>

      <v-row style="height: 500px">
        <v-spacer>
          <v-col>
            <v-card height="450px" outlined tile>
              <div>
                <chart-forecast-container
                  :lat="this.lat"
                  :long="this.long"
                  :cityName="this.cityName"
                />
              </div>
            </v-card>
          </v-col>
        </v-spacer>
      </v-row>
    </v-container>

    <router-link to="/">
      <v-btn class="mx-2" fab dark color="cyan darken-2">
        <v-icon> mdi-keyboard-return </v-icon>
      </v-btn>
    </router-link>
  </h1>
</template>

<style scoped>
.v-btn {
  left: 90%;
  bottom: 10px;
}
</style>

<script>
import chartHistoryContainer from "../components/history-chart-container.vue";
import chartForecastContainer from "../components/forecast-chart-container.vue";

export default {
  components: { chartHistoryContainer, chartForecastContainer },
  name: "Detail",
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
};
</script>
