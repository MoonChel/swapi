<template>
  <div>
    <button @click="fetch" :aria-busy="loading">Fetch</button>

    <ul>
      <li v-for="file in csvFiles" :key="file.id">
        <router-link :to="'/csv-file/' + file.id">
          {{ file.created_at }}
        </router-link>
      </li>
    </ul>

    <h2 v-if="csvFiles.length === 0">No files found</h2>
  </div>
</template>

<script>
import { apiClient } from "@/api";

export default {
  data() {
    return {
      csvFiles: [],
      loading: false,
    };
  },
  async mounted() {
    await this.fetchFiles();
  },
  methods: {
    async fetchFiles() {
      try {
        this.csvFiles = await apiClient.fetchFiles();
        this.$notify({ type: "success", text: "Success" });
      } catch (error) {
        this.$notify({ type: "error", text: "Error" });
        console.log(error);
      }
    },
    async fetch() {
      this.loading = true;
      try {
        await apiClient.fetch();
        await this.fetchFiles();
        this.$notify({ type: "success", text: "Success" });
      } catch (error) {
        this.$notify({ type: "error", text: "Error" });
      }
      this.loading = false;
    },
  },
};
</script>
