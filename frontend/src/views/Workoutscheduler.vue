<template>
  <v-row>
    <v-col>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          :now="today"
          :value="today"
          :events="events"
          color="primary"
          type="week"
          class="mx-auto mt-14"
        ></v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
  export default {
    data: () => ({
      today: '2019-01-08',
      events: [
        {
          name: 'Weekly Meeting',
          start: '2019-01-07 09:00',
          end: '2019-01-07 10:00',
        },
        {
          name: `Thomas' Birthday`,
          start: '2019-01-10',
        },
        {
          name: 'Mash Potatoes',
          start: '2019-01-09 12:30',
          end: '2019-01-09 15:30',
        },
      ],
    }),
    mounted () {
      this.$refs.calendar.scrollToTime('08:00')
    },
  }
</script>