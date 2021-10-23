<template>
  <form>
    <v-text-field
      v-model="lattitude"
      :error-messages="lattitudeErrors"
      :counter="10"
      label="Lattitude"
      required
      @input="$v.lattitude.$touch()"
      @blur="$v.lattitude.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="longitude"
      :error-messages="longitudeErrors"
      label="Longitude"
      required
      @input="$v.longitude.$touch()"
      @blur="$v.longitude.$touch()"
    ></v-text-field>

    <v-btn class="mr-4" @click="submit"> submit </v-btn>
    <v-btn @click="clear"> clear </v-btn>
  </form>
</template>

<script>
import {
  required,
  minLength,
  maxLength,
  minValue,
  decimal,
} from "vuelidate/lib/validators";

export default {
  name: "formValidation",
  data: () => ({
    lattitude: 50.06,
    longitude: 19.94,
  }),

  validations: {
    lattitude: {
      required,
      decimal,
      minLength: minLength(4),
      maxLength: maxLength(9),
      minValue: minValue(0),
    },
    longitude: {
      required,
      decimal,
      minLength: minLength(4),
      maxLength: maxLength(9),
      minValue: minValue(0),
    },
  },

  computed: {
    lattitudeErrors() {
      const errors = [];
      if (!this.$v.lattitude.$dirty) return errors;
      !this.$v.lattitude.minLength &&
        errors.push("Lattitude must be at least 4 characters long");
      !this.$v.lattitude.maxLength &&
        errors.push("Lattitude must be at most 9 characters long");
      !this.$v.lattitude.required && errors.push("Lattitude is required.");
      !this.$v.lattitude.decimal &&
        errors.push("Lattitude must be decimal value");
      return errors;
    },
    longitudeErrors() {
      const errors = [];
      if (!this.$v.longitude.$dirty) return errors;
      !this.$v.longitude.minLength &&
        errors.push("Longitude must be at least 4 characters long");
      !this.$v.longitude.maxLength &&
        errors.push("Longitude must be at most 9 characters long");
      !this.$v.longitude.decimal &&
        errors.push("Longitude must be decimal value");
      !this.$v.longitude.required && errors.push("Longitude is required.");
      return errors;
    },
  },
  methods: {
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.lattitude = "";
      this.longitude = "";
    },
  },
};
</script>


<style scoped>
</style>