<template>
  <figure>
    <img :src="img" :alt="title" />
    <hr />
    <figcaption>
      <span>{{ id }}. {{ title }}</span>
      <a v-if="link" :href="link" target="_blank" rel="nofollow">source</a>
    </figcaption>
  </figure>
</template>

<script setup lang="ts">
import type { Content } from "../utils.ts";

defineProps<Content>();
</script>

<style scoped>
figure {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
}
figure img {
  margin-left: unset;
}

hr {
  margin-bottom: 0.75rem;
}

figcaption {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}
</style>
