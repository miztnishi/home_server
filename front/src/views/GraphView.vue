<template>
  <div class="homeGraph">
    <h1>気温・湿度グラフ</h1>
    <!-- <v-row align="center" class="px-4">
      <v-col cols="6">
        <v-subheader> 期間選択</v-subheader>
      </v-col>
      <v-col cols="3">
        <v-select
          @change="changeDateSpan"
          v-model="selectedDateSpan"
          :hint="`${selectedDateSpan.text}, ${selectedDateSpan.value.start} 〜 ${selectedDateSpan.value.end}`"
          :items="targetDateSpan"
          item-title="text"
          item-value="value"
          label="Select"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
      <v-col cols="3">
        <v-btn color="blue" @click="changeDateSpan"> 変更 </v-btn>
      </v-col>
    </v-row> -->
    <Line
      id="my-chart-id"
      v-if="loaded"
      :height="height"
      :width="width"
      :options="option"
      :data="state"
    />
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, reactive, ref } from "vue";
import { Line } from "vue-chartjs";
import { HomeServerApi } from "../api/api";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Filler,
} from "chart.js";
import dayjs from "dayjs";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  PointElement,
  LineElement,
  LinearScale,
  Filler
);

interface ChartData {
  labels: string[];
  datasets: {
    label: string;
    backgroundColor: string;
    data: number[];
    fill: {
      target: "origin";
      above: string; // Area will be red above the origin
    };
    tension: number;
  }[];
}

export default defineComponent({
  name: "HomeView",
  components: { Line },
  setup() {
    var loaded = ref(false);
    const now = dayjs();

    const height = ref((8 * window.innerHeight) / 10);
    const width = ref(window.innerWidth);

    const state = reactive<ChartData>({
      labels: [],
      datasets: [],
    });
    const option = {
      maintainAspectRatio: true,
      responsive: false,
    };

    // let selectedDateSpan = ref({
    //   text: "今日",
    //   value: {
    //     start: now.startOf("d").format("YYYY-MM-DD HH:mm:ss"),
    //     end: now.format("YYYY-MM-DD HH:mm:ss"),
    //   },
    // });

    // const targetDateSpan = [
    //   {
    //     text: "今日",
    //     value: {
    //       start: now.startOf("d").format("YYYY-MM-DD HH:mm:ss"),
    //       end: now.format("YYYY-MM-DD HH:mm:ss"),
    //     },
    //   },
    //   {
    //     text: "今月",
    //     value: {
    //       start: now.startOf("month").format("YYYY-MM-DD HH:mm:ss"),
    //       end: now.format("YYYY-MM-DD HH:mm:ss"),
    //     },
    //   },
    //   {
    //     text: "3ヶ月",
    //     value: {
    //       start: now.startOf("month").subtract(3, "months").format("YYYY-MM-DD HH:mm:ss"),
    //       end: now.format("YYYY-MM-DD HH:mm:ss"),
    //     },
    //   },
    //   {
    //     text: "半年",
    //     value: {
    //       start: now.startOf("month").subtract(6, "months").format("YYYY-MM-DD HH:mm:ss"),
    //       end: now.format("YYYY-MM-DD HH:mm:ss"),
    //     },
    //   },
    //   {
    //     text: "1年",
    //     value: {
    //       start: now.startOf("month").subtract(1, "year").format("YYYY-MM-DD HH:mm:ss"),
    //       end: now.format("YYYY-MM-DD HH:mm:ss"),
    //     },
    //   },
    // ];

    // const changeDateSpan = async () => {
    //   console.log(selectedDateSpan.value.value);
    //   const data = await HomeServerApi.getThermometer(
    //     selectedDateSpan.value.value.start,
    //     selectedDateSpan.value.value.end
    //   );

    //   state.labels = data.map((i) => dayjs(i.date).format("MM/DD H時"));
    //   console.log(state.labels);
    //   state.datasets[0].data = [];
    //   state.datasets[1].data = [];
    //   state.datasets[0].data = data.map((i) => i.temperature);
    //   state.datasets[1].data = data.map((i) => i.humidity);
    //   console.log(state.datasets[0]);
    //   loaded.value = true;
    // };

    onMounted(async () => {
      const data = await HomeServerApi.getThermometer(
        now.subtract(1, "d").format("YYYY-MM-DD HH:mm:ss"),
        now.format("YYYY-MM-DD HH:mm:ss")
      );
      state.labels = data.map((i) => dayjs(i.date).format("MM/DD H時"));
      state.datasets.push({
        label: "気温",
        backgroundColor: "rgb(255, 0, 0, 0.4)",
        data: data.map((i) => i.temperature),
        fill: {
          target: "origin",
          above: "rgb(255, 0, 0, 0.4)", // Area will be red above the origin
        },
        tension: 0,
      });

      state.datasets.push({
        label: "湿度",
        backgroundColor: "rgb(255, 255, 0, 0.4)",
        data: data.map((i) => i.humidity),
        fill: {
          target: "origin",
          above: "rgb(255, 255, 0, 0.4)", // Area will be red above the origin
        },
        tension: 0,
      });

      loaded.value = true;
    });

    return {
      state,
      loaded,
      option,
      height,
      width,
      // selectedDateSpan,
      // targetDateSpan,
      // changeDateSpan,
    };
  },
});
</script>

<style scoped>
</style>