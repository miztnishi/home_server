<template>
  <div class="homeGraph">
    <h1>温度計/高緯度計グラフ</h1>
    <ul>
      <li v-for="a in test" :key="a">{{ a }}</li>
      <li v-for="a in test" :key="a">{{ a }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";

export default defineComponent({
  name: "HomeView",
  components: {},
  data: () => {
    return {
      test: ["a", "b", "c"],
      game: ["bb", "aa"],
      endgame: "tesl",
    };
  },
});
</script>
