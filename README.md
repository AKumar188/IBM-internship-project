# Employee Attrition and Workforce Analysis

> **IBM SkillsBuild Data Analytics with AI Academic Internship Program**  
> Conducted by **BharatCares** in association with **AICTE**  
> **Student:** Anish Kumar

---

## Project Overview

This project is a complete end-to-end Data Analytics study on employee attrition using the IBM HR Analytics Employee Attrition & Performance dataset. The project follows the full data analytics lifecycle — from data loading and cleaning through exploratory analysis, visualization, correlation analysis, and actionable business recommendations.

The goal is to help HR management understand *why* employees leave and *which employee profiles* are at highest attrition risk, enabling data-driven workforce planning and targeted retention strategies.

---

## Problem Statement

Employee attrition is a costly business challenge. High turnover leads to increased recruitment and training costs, loss of institutional knowledge, and reduced team morale. Despite having large volumes of HR data, many organizations lack a structured analytical approach to identify the root causes of attrition. This project addresses that gap by applying data analytics techniques to reveal patterns in employee departure across multiple workforce dimensions.

---

## Objectives

1. Load, explore, and understand the structure and quality of the IBM HR dataset.
2. Perform data quality checks and clean the dataset.
3. Engineer derived features to support group-level analysis.
4. Calculate key business metrics including attrition rate, average salary, and satisfaction scores.
5. Conduct exploratory data analysis (EDA) across department, job role, age, gender, overtime, travel, and more.
6. Create professional, readable data visualizations.
7. Perform correlation analysis on numerical variables.
8. Identify key data-backed insights.
9. Provide practical, evidence-based HR recommendations.

---

## Dataset

- **Name:** IBM HR Analytics Employee Attrition & Performance
- **Source:** Kaggle
- **URL:** https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
- **File used:** `WA_Fn-UseC_-HR-Employee-Attrition.csv`---"https://drive.google.com/file/d/1UaPPlqL8rE5-9vdaK5ygBDNd6S1SMLH5/view?usp=sharing"
- **Records:** 1,470 employees
- **Features:** 35 columns

---

## Dataset Features

| Column | Description |
|---|---|
| Age | Employee age |
| Attrition | Whether employee left (Yes/No) |
| BusinessTravel | Travel frequency (Non-Travel, Travel_Rarely, Travel_Frequently) |
| Department | Employee's department (Sales, Research & Development, Human Resources) |
| DistanceFromHome | Distance from home to office (in km) |
| Education | Education level (1–5) |
| EducationField | Field of education |
| Gender | Male / Female |
| JobLevel | Job level (1=Entry to 5=Senior) |
| JobRole | Specific job title |
| JobSatisfaction | Job satisfaction rating (1=Low to 4=High) |
| MaritalStatus | Single / Married / Divorced |
| MonthlyIncome | Monthly salary in USD |
| NumCompaniesWorked | Number of companies worked at previously |
| OverTime | Whether employee works overtime (Yes/No) |
| PercentSalaryHike | Last percentage salary hike |
| TotalWorkingYears | Total years of work experience |
| WorkLifeBalance | Work-life balance rating (1=Bad to 4=Best) |
| YearsAtCompany | Years at the current company |
| YearsInCurrentRole | Years in the current job role |
| YearsSinceLastPromotion | Years since last promotion |
| YearsWithCurrManager | Years with current manager |

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Pandas | Data loading, cleaning, manipulation |
| NumPy | Numerical computations |
| Matplotlib | Base charting library |
| Seaborn | Statistical visualizations, heatmaps |
| Jupyter Notebook | Interactive analysis environment |

---

## Project Workflow

```
Dataset
  → 1. Data Collection & Loading
  → 2. Data Quality Check
  → 3. Data Cleaning
  → 4. Feature Engineering
  → 5. Key Business Metrics
  → 6. Exploratory Data Analysis
  → 7. Data Visualization
  → 8. Correlation Analysis
  → 9. Key Insights
  → 10. Business Recommendations
  → 11. Conclusion
```

---

## Key Analysis Areas

| Area | Description |
|---|---|
| **Attrition Rate** | Overall and segmented attrition rates |
| **Department** | Attrition and income by department |
| **Job Role** | Role-specific attrition and salary analysis |
| **Gender** | Gender-based attrition comparison |
| **Age Group** | Attrition across age bands (18–25, 26–35, etc.) |
| **Overtime** | Overtime vs non-overtime attrition |
| **Business Travel** | Travel frequency and attrition relationship |
| **Marital Status** | Attrition by single/married/divorced |
| **Job Level** | Entry-level vs senior-level attrition |
| **Job Satisfaction** | Satisfaction scores and attrition link |
| **Work-Life Balance** | WLB rating and attrition patterns |
| **Salary/Compensation** | Income comparison between stayers and leavers |
| **Experience/Tenure** | Years at company and attrition relationship |

---

## How to Run the Project

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Step-by-Step Instructions

**1. Install Python**  
Download and install Python from https://www.python.org/downloads/

**2. Clone or Download the Project**  
```bash
git clone <repository-url>
# OR download and extract the ZIP file
```

**3. Navigate to the Project Folder**  
```bash
cd Employee_Attrition_Workforce_Analysis
```

**4. Install Required Libraries**  
```bash
pip install -r requirements.txt
```

**5. Place the Dataset**  
Download the dataset from Kaggle and place the file named:
```
WA_Fn-UseC_-HR-Employee-Attrition.csv
```
in the `Employee_Attrition_Workforce_Analysis/` folder.

**6. Launch Jupyter Notebook**  
```bash
jupyter notebook
```

**7. Open and Run the Notebook**  
- Open `AnishKumar_EmployeeAttritionWorkforceAnalysis.ipynb`
- Click **Kernel → Restart & Run All** to execute all cells in order

---

## Project Files

```
Employee_Attrition_Workforce_Analysis/
│
├── AnishKumar_EmployeeAttritionWorkforceAnalysis.ipynb   ← Main analysis notebook
├── AnishKumar_ProjectReport.docx                         ← Academic project report
├── requirements.txt                                      ← Python dependency list
├── README.md                                             ← This file
└── WA_Fn-UseC_-HR-Employee-Attrition.csv                ← Dataset (download from Kaggle)
```

| File | Description |
|---|---|
| `AnishKumar_EmployeeAttritionWorkforceAnalysis.ipynb` | Complete Jupyter Notebook with all code, outputs, charts, and analysis |
| `AnishKumar_ProjectReport.docx` | Professional academic report in DOCX format |
| `requirements.txt` | All Python packages required to run the notebook |
| `README.md` | Project documentation (this file) |
| `WA_Fn-UseC_-HR-Employee-Attrition.csv` | IBM HR dataset (must be downloaded from Kaggle) |

---

## Key Insights

All insights below are derived from the actual dataset (1,470 employees):

1. **Overall Attrition Rate: 16.12%** — 237 out of 1,470 employees left.

2. **Overtime is the #1 attrition driver:** Employees working overtime have a **30.53%** attrition rate vs **10.44%** for non-overtime workers — nearly 3× higher.

3. **Sales Representatives** have the highest role-specific attrition at **39.76%** and also earn the lowest average salary ($2,626/month).

4. **Young employees (18–25)** show the highest age-group attrition at **34.78%**; entry-level (Job Level 1) employees at **26.34%**.

5. **Frequent business travelers** leave at **24.91%** vs **8.00%** for non-travelers — a 3× difference.

6. **Work-life balance level 1 (Bad)** employees leave at **31.25%**, vs 14.22% at level 3 (Good).

7. **Single employees** have a **25.53%** attrition rate vs 12.48% (married) and 10.09% (divorced).

8. **Compensation gap:** Employees who left earned on average **$4,787/month** vs **$6,833/month** for those who stayed — a 30% difference.

9. **The Sales department** has the highest departmental attrition at **20.63%**, followed by Human Resources (19.05%).

10. **Tenure is protective:** Attrition drops consistently as years at the company increase.

---

## Business Recommendations

1. **Overtime Management:** Monitor and limit excessive overtime; flag high-risk employees for engagement check-ins.
2. **Sales Retention:** Review Sales Representative compensation; introduce bonuses and career ladders.
3. **Early-Career Onboarding:** Strengthen 90-day and 12-month onboarding programs with mentorship and clear career paths.
4. **Business Travel Policy:** Evaluate necessity of all frequent travel; explore virtual alternatives.
5. **Work-Life Balance Programs:** Introduce flexible work arrangements and wellness initiatives for employees with poor WLB scores.
6. **Job Satisfaction Initiatives:** Regular pulse surveys, recognition programs, and acting on feedback.
7. **Compensation Benchmarking:** Ensure entry and mid-level salaries are competitive with the market.
8. **Career Progression Transparency:** Implement Individual Development Plans (IDPs) and visible promotion criteria.

---

## Conclusion

This project demonstrated the complete data analytics lifecycle applied to an HR attrition problem. Using Python (Pandas, NumPy, Matplotlib, Seaborn) on the IBM HR Analytics dataset, the analysis quantified attrition across 14+ dimensions and identified eight critical, data-backed risk factors. The findings provide HR management with a concrete, evidence-based roadmap to reduce the 16.12% attrition rate through targeted interventions in overtime policy, compensation, onboarding, and work-life balance programs.

---

## Author

**Name:** Anish Kumar  
**Program:** IBM SkillsBuild Data Analytics with AI Academic Internship Program  
**Organization:** BharatCares in association with AICTE  
**Project Type:** Academic Data Analytics Project

---

*Dataset source: IBM HR Analytics Employee Attrition & Performance — Kaggle*  
*https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset*
