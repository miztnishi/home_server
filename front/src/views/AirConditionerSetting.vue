<template>
  <div class="airConditionerSetting">
    <h1>エアコン閾値設定</h1>
    <div class="column">
      <div class="ui form">
        <div class="grouped fields">
          <div class="field">
            <div class="ui radio checkbox">
              <input type="radio" name="冷房" value="cooling" v-model="mode" tabindex="0" />
              <label>冷房</label>
            </div>
          </div>
          <div class="field">
            <div class="ui radio checkbox">
              <input type="radio" name="暖房" value="heating" v-model="mode" tabindex="1" />
              <label>暖房</label>
            </div>
          </div>
          <div class="field">
            <div class="ui radio checkbox">
              <input type="radio" name="解除" value="nonActive" v-model="mode" tabindex="1" />
              <label>解除</label>
            </div>
          </div>
        </div>
      </div>

      <h2 class="ui gray header">{{ mode }}</h2>
      <h2 class="ui gray header">閾値設定</h2>
      <select v-model="threshold">
        <option
          v-for="temperature in temperatureList"
          v-bind:key="temperature"
          v-bind:value="temperature"
        >
          {{ temperature }}
        </option>
      </select>
      <h2 class="ui gray header">閾値 : {{ threshold }}</h2>

      <h2 class="ui gray header">設定温度</h2>
      <select v-model="airConTemperature">
        <option
          v-for="airConditionerSetting in airConditionerSettingList"
          v-bind:key="airConditionerSetting"
          v-bind:value="airConditionerSetting"
        >
          {{ airConditionerSetting }}
        </option>
      </select>
      <h2 class="ui gray header">設定温度: {{ airConTemperature }}</h2>
    </div>
    <button @click="updateAirConditionerSetting">設定</button>
  </div>
</template>


<script lang="ts">
import { HomeServerApi } from "@/api/api";
import { defineComponent, onMounted, ref } from "vue";
import { UpdateAirConditionerSetting } from "../type";
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
    console.log(temperatureList);
    let mode = ref();
    let threshold = ref();
    let airConTemperature = ref();

    onMounted(async () => {
      const setting = await HomeServerApi.getActiveAirConditionerSetting();
      if (!setting) {
        mode.value = "有効化しましょう";
      } else {
        mode.value = setting.mode;
        threshold.value = setting.threshold;
        airConTemperature.value = setting.temperature;
      }
    });
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
    };
    return {
      mode,
      temperatureList,
      threshold,
      airConTemperature,
      airConditionerSettingList,
      updateAirConditionerSetting,
    };
  },
});
</script>