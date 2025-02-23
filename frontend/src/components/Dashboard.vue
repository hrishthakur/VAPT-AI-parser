<template>
  <div class="dashboard">
    <h2>Vulnerabilities Dashboard</h2>
    
    <!-- Loading and Error States -->
    <div v-if="loading" class="loading">Loading vulnerabilities...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <!-- Vulnerabilities Table -->
    <div v-if="!loading && !error" class="vulnerabilities-container">
      <div v-for="vuln in vulnerabilities" :key="vuln.id" class="vulnerability-card">
        <div class="card-header">
          <h3>{{ vuln.issue_name }}</h3>
          <span :class="'severity ' + vuln.severity.toLowerCase()">
            {{ vuln.severity }}
          </span>
        </div>

        <div class="card-body">
          <div class="info-row">
            <strong>Tech Stack:</strong> {{ vuln.tech_stack }}
          </div>
          <div class="info-row">
            <strong>CWE ID:</strong> {{ vuln.cwe_id }}
          </div>
          
          <div class="info-section">
            <h4>Business Impact</h4>
            <p>{{ vuln.business_impact }}</p>
          </div>

          <div class="info-section">
            <h4>Best Fix</h4>
            <p>{{ vuln.best_fix }}</p>
          </div>

          <div class="info-section">
            <h4>Business-Friendly Fix</h4>
            <p>{{ vuln.business_friendly_fix }}</p>
          </div>

          <div class="info-section">
            <h4>Temporary Mitigation</h4>
            <p>{{ vuln.temporary_mitigation }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { fetchVulnerabilities } from '../api';

export default {
  name: 'Dashboard',
  data() {
    return {
      vulnerabilities: [],
      loading: true,
      error: null
    };
  },
  async mounted() {
    await this.loadVulnerabilities();
  },
  methods: {
    async loadVulnerabilities() {
      try {
        this.loading = true;
        const response = await fetchVulnerabilities();
        this.vulnerabilities = response.vulnerabilities;
        this.loading = false;
      } catch (error) {
        console.error('Error loading vulnerabilities:', error);
        this.error = 'Failed to load vulnerabilities';
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.vulnerabilities-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.vulnerability-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.card-header {
  padding: 15px;
  background: #f5f5f5;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header h3 {
  margin: 0;
  font-size: 1.1em;
}

.severity {
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: bold;
  font-size: 0.9em;
}

.severity.high {
  background: #ffebee;
  color: #c62828;
}

.severity.medium {
  background: #fff3e0;
  color: #ef6c00;
}

.severity.low {
  background: #e8f5e9;
  color: #2e7d32;
}

.card-body {
  padding: 15px;
}

.info-row {
  margin-bottom: 10px;
}

.info-section {
  margin-top: 15px;
}

.info-section h4 {
  margin: 0 0 8px 0;
  color: #333;
  font-size: 1em;
}

.info-section p {
  margin: 0;
  color: #666;
  font-size: 0.9em;
  line-height: 1.4;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #666;
}

.error {
  color: #c62828;
  text-align: center;
  padding: 20px;
}
</style>