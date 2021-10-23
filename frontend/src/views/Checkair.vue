<template>
  <div id="app" class="container mt-5 mb-5" style="width: 500px">
    <form-validation />
  </div>
</template>


<script>
import FormValidation from "../components/form-validation.vue";

export default {
  name: "Check air",
  components : {
    FormValidation
  },
  data: () => ({
    loaded: false,
    chartdata: null,
  }),
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
  }
</script>
