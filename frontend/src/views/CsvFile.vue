<template>
  <div>
    <template v-if="file.created_at">
      <h1>{{ file.created_at }}</h1>

      <a
        v-for="h in allHeaders"
        :key="h"
        role="button"
        :class="filters.includes(h) ? 'contrast' : ''"
        @click.prevent="setFilter(h, $event)"
        style="margin: 10px 10px 10px 0px"
      >
        {{ h }}
      </a>

      <div style="overflow-x: auto">
        <table role="grid">
          <thead>
            <tr>
              <th v-for="h in file.header" :key="h" scope="col">{{ h }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in file.results" :key="r.id">
              <td v-for="(attr, i) in r" :key="i + attr">{{ attr }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <button @click="loadMore" :disabled="filters.length > 0">
        Load more
      </button>
    </template>
  </div>
</template>

<script>
import { apiClient } from "@/api";

export default {
  props: ["id"],
  data() {
    return {
      file: {
        header: [],
        results: [],
        allHeaders: [],
        created_at: null,
      },
      filters: [],
      page: 0,
    };
  },
  async mounted() {
    await this.fetchFile();
  },
  methods: {
    async fetchFile() {
      try {
        const data = await apiClient.fetchCsv(this.$route.params.id, this.page);
        this.file.header = data.header;
        this.allHeaders = data.header;
        this.file.results = this.file.results.concat(data.results);
        this.file.created_at = data.created_at;
        this.$notify({ type: "success", text: "Success" });
      } catch (error) {
        this.$notify({ type: "error", text: "Error" });
        console.log(error);
      }
    },
    async groupByCsv() {
      try {
        const data = await apiClient.groupByCsv(
          this.$route.params.id,
          this.filters
        );
        this.file = data;
        this.$notify({ type: "success", text: "Success" });
      } catch (error) {
        this.$notify({ type: "error", text: "Error" });
        console.log(error);
      }
    },
    async loadMore() {
      this.page += 1;
      await this.fetchFile();
    },
    async setFilter(h) {
      this.page = 0;

      if (this.filters.includes(h)) {
        this.filters = this.filters.filter((f) => f !== h);
      } else {
        this.filters.push(h);
      }

      await this.groupByCsv();
    },
  },
};
</script>