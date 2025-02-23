<template>
  <div class="upload-container">
    <h2>Upload Vulnerability Report</h2>
    <form @submit.prevent="submitFile" class="upload-form">
      <input 
        type="file" 
        ref="fileInput"
        @change="handleFileChange"
        accept=".csv,.json,.pdf, .xlsx, .xls"
      />
      <button type="submit" :disabled="!selectedFile">Upload</button>
    </form>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="success" class="success">{{ success }}</div>
  </div>
</template>

<script>
import { uploadFile } from '../api';

export default {
  name: 'UploadFile',
  emits: ['fileUploaded'],
  data() {
    return {
      selectedFile: null,
      error: null,
      success: null
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
      this.error = null;
      this.success = null;
    },
    async submitFile() {
      if (!this.selectedFile) {
        this.error = 'Please select a file first';
        return;
      }

      try {
        this.error = null;
        this.success = null;
        
        const formData = new FormData();
        formData.append('file', this.selectedFile);
        
        await uploadFile(formData);
        this.success = 'File uploaded successfully';
        this.$emit('fileUploaded');
        
        // Reset form
        this.$refs.fileInput.value = '';
        this.selectedFile = null;
      } catch (error) {
        console.error('Error uploading file:', error);
        this.error = error.response?.data?.error || 'Failed to upload file';
      }
    }
  }
};
</script>

<style scoped>
.upload-container {
  padding: 20px;
}

.upload-form {
  margin: 20px 0;
  display: flex;
  gap: 10px;
  align-items: center;
}

.error {
  color: red;
  margin-top: 10px;
}

.success {
  color: green;
  margin-top: 10px;
}

button {
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style>