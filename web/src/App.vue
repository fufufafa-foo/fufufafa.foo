<template>
  <div>
    <section>
      <Banner />
    </section>
    <main>
      <input v-model="search" type="search" placeholder="Search quote" />
      <template v-if="filteredContents.length">
        <Quote v-for="content in filteredContents" :key="content.id" v-bind="content" />
      </template>
      <p v-else>No results</p>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import Quote from "./components/Quote.vue";
import Banner from "./components/Banner.vue";
import { parseContents, filterContent } from "./utils.ts";

const search = ref("");
const contents = parseContents();
const filteredContents = computed(() => contents.filter(filterContent(search.value)));
</script>
