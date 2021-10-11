<template>
  <h1>
    Detail view {{ city }}
    <router-link to="/">
      <v-btn class="mx-2" fab dark color="cyan darken-2">
        <v-icon> mdi-keyboard-return </v-icon>
      </v-btn>
    </router-link>

    <div class="small">
      <chart-container-vue />
    </div>

  </h1>
</template>

<style scoped>
.v-btn {
  left: 70%;
  top: 700px;
}
</style>

<script>
import chartContainerVue from "../components/chart-container.vue";

export default {
  components: { chartContainerVue },
  name: "Detail",
  props: {
    city: {
      type: String,
      default: 0,
    },
  },
};
</script>
