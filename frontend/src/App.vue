<template>
  <div id="app">
    <div class="main-content">
      <div class="top-bar">
        <button class="menu-btn" @click="togglePanel">
          <i class="fas fa-bars"></i>
        </button>
        <div class="logo">
          <h2>VAPT AI Parser</h2>
        </div>
      </div>
      <div class="content-wrapper">
        <div class="left-panel" :class="{ 'panel-open': isPanelOpen }">
          <div class="panel-content">
            <router-link to="/dashboard" class="panel-item" active-class="active">
              <i class="fas fa-chart-bar"></i>
              Dashboard
            </router-link>
            <router-link to="/upload" class="panel-item" active-class="active">
              <i class="fas fa-upload"></i>
              Upload Report
            </router-link>
          </div>
        </div>
        <div class="main-view" :class="{ 'content-shifted': isPanelOpen }">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isPanelOpen: false
    }
  },
  methods: {
    togglePanel() {
      this.isPanelOpen = !this.isPanelOpen;
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  min-height: 100vh;
  background-color: #f8f9fa;
}

.main-content {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.top-bar {
  height: 60px;
  display: flex;
  align-items: center;
  background-color: #ffffff;
  padding: 0 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  z-index: 100;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}

.menu-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #2c3e50;
  cursor: pointer;
  padding: 0.5rem;
  margin-right: 1rem;
}

.menu-btn:hover {
  color: #3498db;
}

.logo h2 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.5rem;
}

.content-wrapper {
  display: flex;
  flex: 1;
  margin-top: 60px; /* Height of top bar */
  height: calc(100vh - 60px); /* Viewport height minus top bar */
}

.left-panel {
  position: fixed;
  left: 0;
  top: 60px; /* Height of top bar */
  height: calc(100vh - 60px);
  width: 250px;
  background-color: #ffffff;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
  transform: translateX(-100%);
  transition: transform 0.3s ease;
  z-index: 99;
}

.left-panel.panel-open {
  transform: translateX(0);
}

.panel-content {
  padding: 1.5rem;
  height: 100%;
  overflow-y: auto;
}

.main-view {
  flex: 1;
  padding: 1.5rem;
  margin-left: 0;
  transition: margin-left 0.3s ease;
  overflow-y: auto; /* Enable scrolling */
  width: 100%;
}

/* Shift content when panel is open */
.main-view.content-shifted {
  margin-left: 250px;
}

.panel-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  margin-bottom: 0.5rem;
  text-decoration: none;
  color: #6c757d;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.panel-item i {
  margin-right: 1rem;
  width: 20px;
}

.panel-item:hover {
  background-color: #f8f9fa;
  color: #3498db;
}

.panel-item.active {
  background-color: #e3f2fd;
  color: #3498db;
}

.main-view {
  flex: 1;
  padding: 1.5rem;
  margin-left: 0;
  transition: margin-left 0.3s ease;
  overflow-y: auto;
  width: 100%;
}

.main-view.content-shifted {
  margin-left: 250px;
}

@media (max-width: 768px) {
  .main-view.content-shifted {
    margin-left: 0;
  }
  
  .left-panel {
    width: 240px;
  }
  
  .panel-content {
    padding: 1rem;
  }
  
  .main-view {
    padding: 1rem;
  }
}
</style>