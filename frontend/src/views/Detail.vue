<template>
  <h1>
    Detail view {{ city }}
              <router-link
        to="/"
        tag="v-btn"
      >
    <v-btn
      class="mx-2"
      fab
      dark
      color="cyan darken-2"
    >
      <v-icon>
        mdi-keyboard-return
      </v-icon>
    </v-btn>
    </router-link>
  </h1>
</template>

<style scoped>
.v-btn{
  left: 70%;
  top: 700px;
}
</style>

<script>
export default {
  name: "Detail",
  props: {
    city: {
      type: String,
      default: 0,
    },
  },
};
</script>
