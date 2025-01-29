# Threat-Asset Analysis Automation Tool 🔐

Welcome to the **Threat-Asset Analysis Automation Tool** repository! This project provides an intelligent way to analyze threats and associated assets by automating the creation of a **Threat-Asset Matrix**. The tool is designed to help cybersecurity teams visualize risk levels and mitigation measures efficiently. 🚀

---

## 💡 Project Overview

This project leverages **data analysis** and **visualization techniques** to generate a structured **Threat-Asset Matrix** from input data. It supports CSV and JSON file formats for easy integration with existing threat intelligence systems. The tool also integrates with **MITRE ATT&CK** to categorize known threats effectively.

The system includes:

- **Data Handling Module** to process threat and asset input data.
- **Matrix Generator** to compute risk scores based on **Impact** and **Likelihood**.
- **Visualization Interface** using **Streamlit** for an interactive analysis experience.

---

## 🚀 Key Features

### 1️⃣ Automated Threat-Asset Matrix Generation
- Parses **CSV/JSON** files containing threat and asset data.
- Computes a **Risk Score** using the formula:
  
  ```
  Risk Score = Impact × Likelihood
  ```
- Generates a structured matrix for analysis.

### 2️⃣ MITRE ATT&CK Integration
- Maps known threats to MITRE ATT&CK categories.
- Enhances security analysis with industry-recognized threat classifications.

### 3️⃣ Interactive Data Visualization
- **Heatmap** representation of the **Threat-Asset Matrix**.
- **Streamlit Dashboard** for real-time interaction and filtering.

### 4️⃣ User-Friendly Interface
- Supports **drag-and-drop file uploads**.
- Provides **downloadable reports** for documentation and analysis.

---

## 🛠️ Technologies & Tools

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation |
| **Numpy** | Numerical calculations |
| **Matplotlib & Seaborn** | Data visualization |
| **Streamlit** | Web-based UI for analysis |

---

## 📊 How It Works

### 🔹 Data Collection
- Upload a **CSV or JSON file** containing threats, assets, impact, and likelihood scores.

### 🔹 Risk Calculation
- The system calculates the **Risk Score** for each Threat-Asset pair.

### 🔹 Matrix Generation
- Converts the processed data into a **pivot table format**.
- Displays an interactive **heatmap** of risk levels.

### 🔹 Visualization & Reporting
- Users can explore risks via the **Streamlit interface**.
- Option to **export the matrix** for further analysis.

---

## 📥 Installation Instructions

### **Prerequisites:**
Ensure you have **Python 3.7+** installed.

### **Required Python Libraries:**
```sh
pip install pandas numpy matplotlib seaborn streamlit
```

### **Clone the Repository:**
```sh
git clone https://github.com/yourusername/Threat-Asset-Analysis-Tool.git
cd Threat-Asset-Analysis-Tool
```

### **Run the Visualization Tool:**
```sh
streamlit run visualizer.py
```

---

## 🧑‍💻 Contributing

We welcome contributions! To get started:
1. **Fork** the repository.
2. **Create a new branch** for your feature.
3. **Make changes and commit** them.
4. **Open a Pull Request** with a detailed description of the changes.

---

## 🎯 Future Improvements

- **Integration with more cybersecurity frameworks** (e.g., NIST, OWASP).
- **Advanced risk modeling techniques** (e.g., Bayesian Networks, Machine Learning models).
- **Multi-user collaboration features** with role-based access.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

### **📌 Stay Updated**
⭐ Star this repository to get the latest updates!

📩 Have questions? Feel free to open an **issue** or reach out!

---
