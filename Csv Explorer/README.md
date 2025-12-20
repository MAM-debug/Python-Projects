# 📊 CSV Data Explorer

A beginner-friendly web application built with Python, Pandas, and Streamlit that allows users to upload and explore CSV files with comprehensive data analysis features.

## 🎯 Project Overview

CSV Data Explorer is an interactive data analysis tool that provides instant insights into any CSV dataset. Upload your file and get immediate statistical summaries, column information, and missing value analysis - all through an intuitive web interface.

## ✨ Features

- **📁 File Upload**: Easy drag-and-drop CSV file upload
- **📊 Data Preview**: Interactive table view of your entire dataset
- **📏 Dataset Dimensions**: Display total rows and columns count
- **🔤 Column Information**: View all column names and their data types
- **📈 Statistical Summary**: Automatic calculation of mean, median, min, max, and quartiles for numeric columns
- **❓ Missing Values Analysis**: Identify columns with missing data and see percentage of missing values



## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis

## 📦 Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/MAM-debug/Csv explorer.git
cd csv-explorer
```

### Step 2: Install Dependencies

```bash
pip install streamlit pandas
```

## 🎮 Usage

### Running the Application

1. Navigate to the project directory
2. Run the Streamlit app:

```bash
streamlit run project3.py
```

3. Your browser will automatically open at `http://localhost:8501`
4. Click "Browse files" and select any CSV file
5. Explore your data!

### Sample Datasets

To test the application, you can use these public datasets:
- [Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file)
- [Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)
- Any CSV file from your own projects

## 📸 Screenshots

### File Upload Interface
The clean, intuitive upload interface welcomes users to begin their data exploration.

### Data Preview
Interactive table displaying your entire dataset with sorting and scrolling capabilities.

### Statistical Analysis
Comprehensive statistics including mean, median, standard deviation, and quartiles for numeric columns.

### Missing Values Report
Clear identification of columns with missing data and their respective percentages.

## 🧪 Example Output

For a dataset with 891 rows and 12 columns:

**Dataset Overview:**
- Number of Rows: 891
- Number of Columns: 12

**Missing Values Found:**
| Column Name | Missing Values | Percentage (%) |
|-------------|----------------|----------------|
| Age         | 177            | 19.87          |
| Cabin       | 687            | 77.10          |
| Embarked    | 2              | 0.22           |

## 💡 What I Learned

Building this project taught me:

- **File handling in web applications** using Streamlit's file uploader
- **Data exploration techniques** with Pandas (shape, describe, isnull)
- **Creating interactive web interfaces** without HTML/CSS/JavaScript
- **Data visualization** through tables and metrics
- **Handling missing data** and calculating percentages
- **Building user-friendly applications** with clear feedback messages

## 🔮 Future Enhancements

Potential features to add:
- [ ] Data visualization with charts (histograms, bar charts, scatter plots)
- [ ] Column filtering and selection
- [ ] Export cleaned data as CSV
- [ ] Handle multiple file uploads for comparison
- [ ] Add data type conversion options
- [ ] Implement basic data cleaning features
- [ ] Add correlation matrix for numeric columns

## 🤝 Contributing

This is a beginner learning project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Your Name**
- GitHub: [MAM-debug](https://github.com/MAM-debug)


## 🙏 Acknowledgments

- Thanks to the Streamlit team for the amazing framework
- Pandas library for powerful data manipulation tools
- Kaggle for providing free datasets for testing

## 📧 Contact

Have questions or suggestions? Feel free to reach out!

- Email: muhammadabdullahmateen7.email@gmail.com

---

⭐ If you found this project helpful, please give it a star!

**Built with ❤️ as a first data science project**
