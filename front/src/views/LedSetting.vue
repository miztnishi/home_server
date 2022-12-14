<template>
  <v-container class="" fluid>
    <div class="ledSetting">
      <h1>LEDのON・OFF</h1>
      <v-card round variant="outlined">
        <v-row align="center">
          <v-col cols="6">
            <v-btn class="my-2" color="blue" @click="sendSignalLed('ON')"> ON </v-btn>
          </v-col>
          <v-col cols="6">
            <v-btn class="my-2" color="blue" @click="sendSignalLed('OFF')"> OFF </v-btn>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </v-container>
</template>


<script lang="ts">
import { HomeServerApi } from "@/api/api";
import { defineComponent, onMounted, ref } from "vue";
export default defineComponent({
  name: "LedSettingView",
  components: {},

  setup() {
    const sendSignalLed = async (mode: string) => {
      await HomeServerApi.sendSignalLed(mode);
    };

    return { sendSignalLed };
  },
});
</script>