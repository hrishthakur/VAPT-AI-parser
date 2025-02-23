<template>
  <div id="app">
    <h1>VAPT AI Parser</h1>
    <UploadFile @fileUploaded="refreshDashboard" />
    <Dashboard ref="dashboard" />
  </div>
</template>

<script>
import UploadFile from './components/UploadFile.vue';
import Dashboard from './components/Dashboard.vue';

export default {
  name: 'App',
  components: {
    UploadFile,
    Dashboard
  },
  methods: {
    refreshDashboard() {
      this.$refs.dashboard.loadVulnerabilities();
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 20px;
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}
</style>