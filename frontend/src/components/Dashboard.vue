<template>
  <div class="dashboard">
    <h2 class="dashboard-title">Vulnerabilities Dashboard</h2>
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Loading vulnerabilities data...</p>
    </div>
    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
      <button @click="loadVulnerabilities" class="retry-btn">Retry</button>
    </div>
    <div v-else>
      <div class="stats">
        <div class="stat-card" v-for="stat in stats" :key="stat.label">
          <h3>{{ stat.label }}</h3>
          <p class="stat-value">{{ stat.value }}</p>
        </div>
      </div>
      <div class="charts">
        <div class="chart-container">
          <h3>Severity Distribution</h3>
          <bar-chart :data="severityData" :options="chartOptions" />
        </div>
        <div class="chart-container">
          <h3>Vulnerability Types</h3>
          <pie-chart :data="typeData" :options="chartOptions" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { fetchVulnerabilities } from '../api';
import { Bar, Pie } from 'vue-chartjs';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ArcElement } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ArcElement);

export default {
  name: 'Dashboard',
  components: {
    BarChart: Bar,
    PieChart: Pie
  },
  data() {
    return {
      vulnerabilities: [],
      loading: true,
      error: null,
      stats: [
        { label: 'Total Vulnerabilities', value: 0 },
        { label: 'High Severity', value: 0 },
        { label: 'Medium Severity', value: 0 },
        { label: 'Low Severity', value: 0 }
      ],
      severityData: {
        labels: ['High', 'Medium', 'Low'],
        datasets: [{
          label: 'Severity',
          backgroundColor: ['#dc3545', '#ffc107', '#17a2b8'],
          data: [0, 0, 0]
        }]
      },
      typeData: {
        labels: ['SQL Injection', 'XSS', 'CSRF', 'Other'],
        datasets: [{
          label: 'Types',
          backgroundColor: ['#dc3545', '#ffc107', '#17a2b8', '#6c757d'],
          data: [0, 0, 0, 0]
        }]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom'
          }
        }
      }
    };
  },
  async mounted() {
    await this.loadVulnerabilities();
  },
  methods: {
    async loadVulnerabilities() {
      try {
        this.loading = true;
        this.error = null;
        const response = await fetchVulnerabilities();
        this.vulnerabilities = response.vulnerabilities;
        this.updateStats();
      } catch (error) {
        console.error('Error loading vulnerabilities:', error);
        this.error = 'Failed to load vulnerabilities. Please try again.';
      } finally {
        this.loading = false;
      }
    },
    updateStats() {
      const vulns = this.vulnerabilities;
      
      // Update total count
      this.stats[0].value = vulns.length;
      
      // Update severity counts
      const severityCounts = {
        High: 0,
        Medium: 0,
        Low: 0
      };
      
      // Update type counts
      const typeCounts = {
        'SQL Injection': 0,
        'XSS': 0,
        'CSRF': 0,
        'Other': 0
      };

      vulns.forEach(vuln => {
        if (severityCounts.hasOwnProperty(vuln.severity)) {
          severityCounts[vuln.severity]++;
        }
        
        
        if (typeCounts.hasOwnProperty(vuln.type)) {
          typeCounts[vuln.type]++;
        } else {
          typeCounts['Other']++;
        }
      });

      // Update stats cards
      this.stats[1].value = severityCounts.High;
      this.stats[2].value = severityCounts.Medium;
      this.stats[3].value = severityCounts.Low;

      // Update chart data
      this.severityData.datasets[0].data = Object.values(severityCounts);
      this.typeData.datasets[0].data = Object.values(typeCounts);
    }
  }
};
</script>

<style scoped>
.dashboard {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  padding: 2rem;
}

.dashboard-title {
  color: #2c3e50;
  margin-bottom: 2rem;
  font-size: 1.8rem;
  font-weight: 600;
}

.loading {
  text-align: center;
  padding: 2rem;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error {
  text-align: center;
  color: #dc3545;
  padding: 2rem;
}

.retry-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
}

.retry-btn:hover {
  background-color: #2980b9;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: #ffffff;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  border: 1px solid #e9ecef;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0,0,0,0.1);
}

.stat-card h3 {
  color: #6c757d;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.stat-value {
  color: #2c3e50;
  font-size: 2.2rem;
  font-weight: 700;
}

.charts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
}

.chart-container {
  background: #ffffff;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  height: 400px;
  border: 1px solid #e9ecef;
}

.chart-container h3 {
  color: #2c3e50;
  margin: 0 0 1rem;
  text-align: center;
}

@media (max-width: 768px) {
  .dashboard {
    padding: 1rem;
  }
  
  .charts {
    grid-template-columns: 1fr;
  }
  
  .chart-container {
    height: 300px;
  }
}
</style>