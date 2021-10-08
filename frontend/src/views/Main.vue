<template>
  <v-card class="mx-auto" max-width="344" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="text-h4 mb-3 text-center">
          Rotterdam
        </v-list-item-title>
        <v-list-item-subtitle>Location</v-list-item-subtitle>
        <div class="text-overline mb-4">
          Air quality data sfsfsf sdfsdfs sdfsdsdfcsd sdfsdzfz szdfszf
          szdfszfszfsdzf szfszf
        </div>
      </v-list-item-content>
      <!-- <v-icon right top>mdi-grease-pencil</v-icon> -->
    </v-list-item>
    <v-card-actions>
      <v-btn color="primary" outlined text> More </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
   data() {
    return {
      measurements: [
        {
          id: 1,
          measurements: {'PM1':2,'PM25':18, 'PM10':35, 'PRESSURE':1043},
          airly_caqi: 34,
        }       ],
            };
          },   
}
</script>
