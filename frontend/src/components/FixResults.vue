<template>
    <div v-if="fixes">
      <h2>Generated Fixes</h2>
      <p><b>Best Security Fix:</b> {{ fixes[0] }}</p>
      <p><b>Business-Friendly Fix:</b> {{ fixes[1] }}</p>
      <p><b>Temporary Mitigation:</b> {{ fixes[2] }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ["fixes"]
  };
  </script>
  
  <style scoped>
  h2 {
    margin-top: 20px;
  }
  </style>
  