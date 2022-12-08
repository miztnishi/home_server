<template>
  <div class="homeGraph">
    <h1>気温・湿度グラフ</h1>
    <Line id="my-chart-id" v-if="loaded" :data="state" />
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onBeforeMount, onMounted, reactive, ref, toRefs } from "vue";
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
import { Thermometer } from "@/type";
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
    const state = reactive<ChartData>({
      labels: [],
      datasets: [],
    });
    // console.log("ddd");
    onMounted(async () => {
      const data = await HomeServerApi.getThermometer();
      state.labels = data.map((i) => dayjs(i.date).format("MM/DD H時"));
      state.datasets.push({
        label: "気温",
        backgroundColor: "rgb(255, 0, 0, 0.4)",
        data: data.map((i) => i.temperature),
        fill: {
          target: "origin",
          above: "rgb(255, 0, 0, 0.4)", // Area will be red above the origin
        },
        tension: 0.5,
      });

      state.datasets.push({
        label: "湿度",
        backgroundColor: "rgb(255, 255, 0, 0.4)",
        data: data.map((i) => i.humidity),
        fill: {
          target: "origin",
          above: "rgb(255, 255, 0, 0.4)", // Area will be red above the origin
        },
        tension: 0.5,
      });

      loaded.value = true;
    });

    return {
      state,
      loaded,
    };
  },
});
</script>
