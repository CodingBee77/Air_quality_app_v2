<template>
  <v-row align="center">
    <v-col class="text-h4" cols="6">{{ infoText }}</v-col>
    <v-col cols="6">
      <v-img
        :src="require(`../assets/${this.imageName}`)"
        height="92px"
        width="92px"
      ></v-img>
    </v-col>
  </v-row>
</template>


<script>
export default {
  name: "MeasurementInfoCard",
  props: {
    infoText: {
      type: String,
    },
    imageName: {
      type: String,
    },
  }
};
</script>