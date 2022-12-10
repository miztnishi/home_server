<template>
  <v-container class="" fluid>
    <div class="airConditionerSetting">
      <h1>エアコン閾値 更新</h1>
      <v-card round variant="outlined">
        <v-row class="">
          <v-col cols="12">
            <v-radio-group
              class="d-flex justify-center mt-1"
              v-model="mode"
              @change="fetchSettings(mode)"
            >
              <v-radio class="my-n1" color="blue" value="cooling"
                ><template v-slot:label>冷房 {{ showActive("cooling") }}</template>
              </v-radio>
              <v-radio class="my-n1" color="red" value="heating">
                <template v-slot:label>暖房 {{ showActive("heating") }}</template>
              </v-radio>
              <v-radio class="my-n1" label="解除" color="black" value="nonActive"></v-radio>
            </v-radio-group>
          </v-col>
        </v-row>
        <v-divider class="py-2"></v-divider>
        <v-row align="center">
          <v-col cols="6">
            <v-subheader> 閾値設定 </v-subheader>
          </v-col>
          <v-col cols="6">
            <v-select
              v-model="threshold"
              :items="temperatureList"
              label="選択"
              persistent-hint
              return-object
              single-line
            ></v-select>
          </v-col>
        </v-row>
        <v-divider class="py-2"></v-divider>
        <v-row align="center">
          <v-col cols="6">
            <v-subheader> エアコン設定温度 </v-subheader>
          </v-col>
          <v-col cols="6">
            <v-select
              v-model="airConTemperature"
              :items="airConditionerSettingList"
              label="選択"
              persistent-hint
              return-object
              single-line
            ></v-select>
          </v-col>
        </v-row>
        <div class="text-center">
          <v-dialog v-model="isDialogOpen">
            <template v-slot:activator="{ props }">
              <v-btn class="my-2" color="blue" @click="updateAirConditionerSetting" v-bind="props">
                更新する
              </v-btn>
            </template>
            <v-card class="text-center">
              <v-card-text> 更新完了 </v-card-text>
            </v-card>
          </v-dialog>
        </div>
      </v-card>
    </div>
  </v-container>
</template>


<script lang="ts">
import { HomeServerApi } from "@/api/api";
import { defineComponent, onMounted, ref } from "vue";
import { AirConditionerSetting, UpdateAirConditionerSetting } from "../type";
export default defineComponent({
  name: "AirConditionerSettingView",
  components: {},

  setup() {
    const temperatureList: number[] = ref([]).value;
    const airConditionerSettingList: number[] = ref([]).value;
    for (let i = 0; i <= 40; i++) {
      temperatureList.push(i);
      if (i >= 17 && i <= 30) {
        airConditionerSettingList.push(i);
      }
    }
    let mode = ref();
    let threshold = ref();
    let airConTemperature = ref();
    let isOpenAlert = ref(false);
    let isDialogOpen = ref(false);
    let settings: AirConditionerSetting[] = [];

    onMounted(async () => {
      settings = await HomeServerApi.getActiveAirConditionerSetting();
      fetchSettings();
    });

    const fetchSettings = async (selectedMode?: string) => {
      let activeSetting = selectedMode
        ? settings.find((i) => i.mode === selectedMode)
        : settings.find((i) => i.isActive === true);

      if (!activeSetting) {
        mode.value = "nonActive";
        threshold.value = null;
        airConTemperature.value = null;
      } else {
        mode.value = activeSetting.mode;
        threshold.value = activeSetting.threshold;
        airConTemperature.value = activeSetting.temperature;
      }
    };

    const showActive = (mode: string) => {
      const setting = settings.find((i) => i.mode === mode);
      return setting?.isActive === true ? "有効済" : "無効済";
    };
    const updateAirConditionerSetting = async () => {
      if (mode.value === "nonActive") {
        await HomeServerApi.updateAirConditionerToNonActive();
      } else {
        const dto: UpdateAirConditionerSetting = {
          temperature: airConTemperature.value,
          threshold: threshold.value,
        };
        await HomeServerApi.updateAirConditionerSetting(mode.value, dto);
      }
      isOpenAlert.value = true;

      settings = await HomeServerApi.getActiveAirConditionerSetting();
    };

    return {
      mode,
      temperatureList,
      threshold,
      airConTemperature,
      airConditionerSettingList,
      isOpenAlert,
      isDialogOpen,
      updateAirConditionerSetting,
      showActive,
      fetchSettings,
    };
  },
});
</script>