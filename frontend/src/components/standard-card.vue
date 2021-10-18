 <template>
  <v-container fluid>
    <v-data-iterator
      :items="this.carddata"
      item-key="pollutant"
      :single-expand="singleExpand"
      hide-default-footer
      v-if="this.loaded"
    >
      <template v-slot:default="{ items, isExpanded, expand }">
        <v-row>
          <v-col
            v-for="item in items"
            :key="item.pollutant"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <v-card>
              <v-card-title>
                <h4>{{ item.pollutant }}</h4>
              </v-card-title>
              <v-switch
                :input-value="isExpanded(item)"
                :label="isExpanded(item) ? 'Expanded' : 'Closed'"
                class="pl-4 mt-0"
                @change="(v) => expand(item, v)"
              ></v-switch>
              <v-divider></v-divider>
              <v-list v-if="isExpanded(item)" dense>
                <v-list-item>
                  <v-list-item-content>Limit</v-list-item-content>
                  <v-list-item-content class="align-end">
                    {{ item.limit }}
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>Percent</v-list-item-content>
                  <v-list-item-content class="align-end">
                    {{ item.percent }}
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>Organization</v-list-item-content>
                  <v-list-item-content class="align-end">
                    {{ item.organization_name }}
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator></v-container
  >
</template>

 <style scoped>
.v-list-item__content {
  justify-content: center;
  display: grid;
  width: 100px;
}
</style>

<script>
import axios from "axios";

export default {
  name: "StandardCard",
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
  data: () => ({
    loaded: false,
    singleExpand: false,
  }),
  async mounted() {
    this.loaded = false;
    try {
      const response = await axios.get(
        "api/v1/measurements/standards/?lat=" + this.lat + "&long=" + this.long
      );
      this.carddata = response.data.factors;
      console.log(this.carddata);
    } catch (e) {
      console.error(e);
    }
    this.loaded = true;
  },
};
</script>