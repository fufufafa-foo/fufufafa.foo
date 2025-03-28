<template>
  <figure>
    <img :src="img" :alt="title" />
    <hr />
    <figcaption>{{ id }}. {{ title }}</figcaption>
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
</style>
