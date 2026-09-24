"""
Build Report Script
Creates AnishKumar_ProjectReport.docx with embedded charts.
Run: python build_report.py
"""
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os, copy

BASE = os.path.dirname(os.path.abspath(__file__))

def img(name):
    return os.path.join(BASE, name)

# ── helpers ───────────────────────────────────────────────────────────────────
def set_cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_color)
    tcPr.append(shd)

def set_col_width(table, col_idx, width_cm):
    for row in table.rows:
        row.cells[col_idx].width = Cm(width_cm)

def add_heading(doc, text, level, color_hex='1e293b'):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor.from_string(color_hex)
    return h

def add_kv_row(table, key, value, row_idx, shade=False):
    row = table.rows[row_idx]
    row.cells[0].text = key
    row.cells[1].text = value
    for i, cell in enumerate(row.cells):
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0:
                    run.font.bold = True
        if shade:
            set_cell_bg(cell, 'f1f5f9')

def add_insight_box(doc, number, title, body):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(6)
    para.paragraph_format.space_after  = Pt(2)
    run = para.add_run(f'  {number}  {title}')
    run.font.bold  = True
    run.font.size  = Pt(11)
    run.font.color.rgb = RGBColor(37, 99, 235)
    p2 = doc.add_paragraph(body)
    p2.paragraph_format.left_indent   = Cm(0.5)
    p2.paragraph_format.space_after   = Pt(8)
    p2.runs[0].font.size = Pt(10)

# ── Document ──────────────────────────────────────────────────────────────────
doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin    = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# ── COVER PAGE ────────────────────────────────────────────────────────────────
doc.add_paragraph()
doc.add_paragraph()

title_para = doc.add_paragraph()
title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title_para.add_run('Employee Attrition and\nWorkforce Analysis')
run.font.size  = Pt(28)
run.font.bold  = True
run.font.color.rgb = RGBColor(37, 99, 235)

sub1 = doc.add_paragraph()
sub1.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub1.add_run('Academic Project Report')
r.font.size = Pt(16); r.font.color.rgb = RGBColor(71, 85, 105)

doc.add_paragraph()

prog = doc.add_paragraph()
prog.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = prog.add_run('IBM SkillsBuild Data Analytics with AI Academic Internship Program')
r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = RGBColor(30, 41, 59)

org = doc.add_paragraph()
org.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = org.add_run('BharatCares in association with AICTE')
r.font.size = Pt(12); r.font.color.rgb = RGBColor(71, 85, 105)

doc.add_paragraph()

stud = doc.add_paragraph()
stud.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = stud.add_run('Submitted by:  Anish Kumar')
r.font.size = Pt(13); r.font.bold = True

ds = doc.add_paragraph()
ds.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = ds.add_run('Dataset: IBM HR Analytics Employee Attrition & Performance')
r.font.size = Pt(11); r.font.color.rgb = RGBColor(71, 85, 105)

src = doc.add_paragraph()
src.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = src.add_run('https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset')
r.font.size = Pt(10); r.font.color.rgb = RGBColor(37, 99, 235)

doc.add_page_break()

# ── ABSTRACT ──────────────────────────────────────────────────────────────────
add_heading(doc, 'Abstract', 1, '1e293b')
doc.add_paragraph(
    'This project presents a comprehensive data analytics study on employee attrition '
    'using the IBM HR Analytics Employee Attrition & Performance dataset, comprising '
    '1,470 employee records across 35 variables. The full data analytics lifecycle was '
    'applied: data loading, quality checking, cleaning, feature engineering, exploratory '
    'data analysis, visualization, correlation analysis, and business recommendations. '
    'The overall attrition rate was 16.12% (237 employees). Key findings: overtime workers '
    'leave at 30.53% vs 10.44% for non-overtime employees; Sales Representatives have the '
    'highest role attrition at 39.76%; the 18–25 age group has 34.78% attrition; frequent '
    'travelers leave at 24.91%; and employees who left earned on average $2,046/month less '
    'than those who stayed. Eight actionable business recommendations are provided.'
)

# ── SECTION 1 ─────────────────────────────────────────────────────────────────
add_heading(doc, '1.  Introduction', 1, '1e293b')
doc.add_paragraph(
    'Employee attrition — the voluntary or involuntary departure of employees — is one of the '
    'most significant challenges facing modern HR management. High turnover leads to direct '
    'costs (recruitment, training) and indirect costs (loss of institutional knowledge, reduced '
    'team morale, productivity decline). Data analytics provides a structured, evidence-based '
    'approach to understanding why employees leave and which segments are at highest risk, '
    'enabling proactive, targeted interventions.'
)
doc.add_paragraph(
    'This project applies the full data analytics workflow to the IBM HR Analytics dataset to '
    'uncover patterns of employee attrition across departments, job roles, demographics, '
    'compensation, overtime, business travel, and satisfaction scores — and to provide '
    'practical, data-backed HR recommendations.'
)

# ── SECTION 2 ─────────────────────────────────────────────────────────────────
add_heading(doc, '2.  Problem Statement', 1, '1e293b')
doc.add_paragraph(
    'Despite having access to substantial HR data, many organizations lack analytical frameworks '
    'to systematically identify why employees leave. This project addresses five core questions:'
)
for q in [
    'What is the overall attrition rate and how is it distributed across departments?',
    'Which departments and job roles have the highest attrition rates?',
    'How do overtime, business travel, and work-life balance relate to attrition?',
    'What are the demographic and compensation characteristics of employees who leave?',
    'What data-backed recommendations can help reduce attrition?',
]:
    p = doc.add_paragraph(q, style='List Bullet')
    p.runs[0].font.size = Pt(11)

# ── SECTION 3 ─────────────────────────────────────────────────────────────────
add_heading(doc, '3.  Project Objectives', 1, '1e293b')
objectives = [
    'Load and explore the IBM HR Analytics dataset using Python and Pandas.',
    'Perform a thorough data quality check and clean the dataset appropriately.',
    'Engineer derived features (AgeGroup, TenureGroup, IncomeGroup) to support analysis.',
    'Calculate key business metrics including attrition rate, average income, and satisfaction scores.',
    'Conduct exploratory data analysis (EDA) across 15+ dimensions.',
    'Create professional, readable data visualizations using Matplotlib and Seaborn.',
    'Perform a correlation analysis on key numerical variables.',
    'Identify data-backed insights and provide practical HR recommendations.',
]
for i, obj in enumerate(objectives, 1):
    p = doc.add_paragraph(f'{i}.  {obj}', style='List Number')
    p.runs[0].font.size = Pt(11)

# ── SECTION 4 ─────────────────────────────────────────────────────────────────
add_heading(doc, '4.  Dataset Description', 1, '1e293b')
doc.add_paragraph(
    'The IBM HR Analytics Employee Attrition & Performance dataset is a widely used benchmark '
    'for HR analytics, originally created by IBM data scientists and available on Kaggle.'
)
add_heading(doc, '4.1  Dataset Summary', 2, '1e40af')
tbl = doc.add_table(rows=6, cols=2)
tbl.style = 'Table Grid'
tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
rows_data = [('Attribute', 'Value', True),
             ('Total Records', '1,470 employees', False),
             ('Total Features', '35 columns', True),
             ('Target Variable', 'Attrition (Yes = 237 / No = 1,233)', False),
             ('Missing Values', 'None', True),
             ('Duplicate Records', 'None', False)]
for i, (k, v, shade) in enumerate(rows_data):
    r = tbl.rows[i]
    r.cells[0].text = k; r.cells[1].text = v
    for cell in r.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(cell, '1e40af')
        elif shade: set_cell_bg(cell, 'eff6ff')

doc.add_paragraph()
add_heading(doc, '4.2  Key Dataset Columns', 2, '1e40af')
col_data = [
    ('Column', 'Type', 'Description'),
    ('Age', 'Numerical', 'Employee age (range: 18–60)'),
    ('Attrition', 'Categorical', 'Left the organization? (Yes/No) — target variable'),
    ('BusinessTravel', 'Categorical', 'Non-Travel / Travel_Rarely / Travel_Frequently'),
    ('Department', 'Categorical', 'Sales / Research & Development / Human Resources'),
    ('JobLevel', 'Numerical', 'Seniority level (1 = Entry to 5 = Senior)'),
    ('JobRole', 'Categorical', 'Specific job title (9 roles)'),
    ('JobSatisfaction', 'Numerical', 'Rating 1 (Low) to 4 (High)'),
    ('MonthlyIncome', 'Numerical', 'Monthly salary in USD'),
    ('OverTime', 'Categorical', 'Works overtime? (Yes/No)'),
    ('MaritalStatus', 'Categorical', 'Single / Married / Divorced'),
    ('WorkLifeBalance', 'Numerical', 'Rating 1 (Bad) to 4 (Best)'),
    ('YearsAtCompany', 'Numerical', 'Tenure at current company'),
    ('TotalWorkingYears', 'Numerical', 'Total years of work experience'),
    ('EducationField', 'Categorical', 'Field of academic study'),
    ('Gender', 'Categorical', 'Male / Female'),
]
tbl2 = doc.add_table(rows=len(col_data), cols=3)
tbl2.style = 'Table Grid'
for i, (c1, c2, c3) in enumerate(col_data):
    r = tbl2.rows[i]
    r.cells[0].text = c1; r.cells[1].text = c2; r.cells[2].text = c3
    for cell in r.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(cell, '1e40af')
        elif i % 2 == 0: set_cell_bg(cell, 'eff6ff')
tbl2.columns[0].width = Cm(4.2)
tbl2.columns[1].width = Cm(3.0)
tbl2.columns[2].width = Cm(9.3)

# ── SECTION 5 ─────────────────────────────────────────────────────────────────
doc.add_paragraph()
add_heading(doc, '5.  Technologies and Tools Used', 1, '1e293b')
tech_data = [
    ('Technology', 'Version / Notes', 'Purpose'),
    ('Python 3',   '3.8+',            'Core programming language'),
    ('Pandas',     '1.5+',            'Data loading, cleaning, groupby analysis'),
    ('NumPy',      '1.24+',           'Numerical operations and array computations'),
    ('Matplotlib', '3.6+',            'Base charting library (bar, histogram, pie)'),
    ('Seaborn',    '0.12+',           'Statistical visualizations, correlation heatmap'),
    ('Jupyter',    'Notebook / Lab',  'Interactive development and output display'),
]
tbl3 = doc.add_table(rows=len(tech_data), cols=3)
tbl3.style = 'Table Grid'
for i, (c1, c2, c3) in enumerate(tech_data):
    r = tbl3.rows[i]
    r.cells[0].text = c1; r.cells[1].text = c2; r.cells[2].text = c3
    for cell in r.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(cell, '1e40af')
        elif i % 2 == 0: set_cell_bg(cell, 'eff6ff')

# ── SECTION 6 ─────────────────────────────────────────────────────────────────
doc.add_paragraph()
add_heading(doc, '6.  Data Visualizations', 1, '1e293b')
doc.add_paragraph(
    'All charts below are generated directly from the dataset using Python (Matplotlib / Seaborn). '
    'Red bars indicate attrition rates above the company average (16.12%); '
    'blue bars indicate below-average rates. Dashed grey lines mark the company average.'
)

chart_specs = [
    ('chart_00_kpi_dashboard.png',  6.4, 'Figure 1 — Key Performance Indicators Dashboard\nCore attrition metrics at a glance.'),
    ('chart_01_attrition_overview.png', 4.8, 'Figure 2 — Overall Attrition (Donut Chart)\n83.88% of employees stayed; 16.12% left.'),
    ('chart_02_attrition_department.png', 5.2, 'Figure 3 — Attrition Rate by Department\nSales (20.63%) and HR (19.05%) exceed the company average.'),
    ('chart_03_attrition_jobrole.png',  5.8, 'Figure 4 — Attrition Rate by Job Role\nSales Representatives top the list at 39.76%; Research Directors lowest at 2.50%.'),
    ('chart_04_overtime.png',  5.2, 'Figure 5 — Overtime vs Attrition\nOvertime workers leave at 30.53% — nearly 3× the rate of non-overtime employees.'),
    ('chart_05_age_group.png', 5.0, 'Figure 6 — Attrition by Age Group\nYoung employees (18–25) leave most frequently at 34.78%.'),
    ('chart_06_business_travel.png', 5.0, 'Figure 7 — Attrition by Business Travel Frequency\nFrequent travelers: 24.91% vs non-travelers: 8.00%.'),
    ('chart_07_gender.png', 5.0, 'Figure 8 — Attrition by Gender\nMale employees (17.01%) have a slightly higher attrition rate than female (14.80%).'),
    ('chart_08_marital_status.png', 4.8, 'Figure 9 — Attrition by Marital Status\nSingle employees leave at 25.53% — more than double divorced employees (10.09%).'),
    ('chart_09_job_level.png', 5.0, 'Figure 10 — Attrition by Job Level\nEntry-level (Level 1): 26.34% vs senior (Level 5): 7.25%.'),
    ('chart_10_job_satisfaction.png', 5.0, 'Figure 11 — Attrition by Job Satisfaction\nLowest satisfaction (Level 1) drives 22.84% attrition vs 11.33% at highest (Level 4).'),
    ('chart_11_work_life_balance.png', 5.0, 'Figure 12 — Attrition by Work-Life Balance\nPoor WLB (Level 1): 31.25% attrition.'),
    ('chart_12_income.png', 5.8, 'Figure 13 — Average Monthly Income by Department and Job Role\nManagers earn most ($17,182); Sales Representatives earn least ($2,626).'),
    ('chart_13_distributions.png', 5.0, 'Figure 14 — Years at Company & Monthly Income Distributions\nLeavers averaged 5.1 years tenure vs stayers at 7.4 years.'),
    ('chart_14_stayed_vs_left.png', 5.0, 'Figure 15 — Employee Profile: Stayed vs Left\nSystematic differences in age, income, tenure, and experience between the two groups.'),
    ('chart_15_correlation.png', 6.5, 'Figure 16 — Correlation Heatmap (11 Variables)\nStrong career-progression correlations; attrition binary correlates negatively with seniority.'),
    ('chart_16_income_group.png', 5.0, 'Figure 17 — Attrition by Income Group\nLow-income employees (<$3K/month) leave at 34.71% — the highest of any income band.'),
]

for chart_file, height_in, caption in chart_specs:
    chart_path = img(chart_file)
    if os.path.exists(chart_path):
        try:
            doc.add_picture(chart_path, width=Inches(6.3))
            last_para = doc.paragraphs[-1]
            last_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap = doc.add_paragraph(caption)
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap.paragraph_format.space_after = Pt(14)
            for run in cap.runs:
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(71, 85, 105)
        except Exception as e:
            print(f'  Warning: could not embed {chart_file}: {e}')
    else:
        print(f'  Warning: chart not found: {chart_path}')

# ── SECTION 7 ─────────────────────────────────────────────────────────────────
doc.add_page_break()
add_heading(doc, '7.  Key Business Metrics', 1, '1e293b')
doc.add_paragraph('All metrics below were calculated directly from the 1,470-record dataset.')

metrics_data = [
    ('Metric', 'Value'),
    ('Total Employees', '1,470'),
    ('Employees Who Left', '237'),
    ('Active Employees', '1,233'),
    ('Overall Attrition Rate', '16.12%'),
    ('Average Age', '36.92 years'),
    ('Average Monthly Income', '$6,502.93'),
    ('Average Years at Company', '7.01 years'),
    ('Average Job Satisfaction', '2.73 / 4'),
    ('Average Work-Life Balance', '2.76 / 4'),
    ('Average Years in Current Role', '4.23 years'),
]
tbl4 = doc.add_table(rows=len(metrics_data), cols=2)
tbl4.style = 'Table Grid'
for i, (k, v) in enumerate(metrics_data):
    r = tbl4.rows[i]
    r.cells[0].text = k; r.cells[1].text = v
    for cell in r.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(11)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(cell, '1e40af')
        elif i % 2 == 0: set_cell_bg(cell, 'eff6ff')
tbl4.columns[0].width = Cm(8)
tbl4.columns[1].width = Cm(5)

# ── SECTION 8 ─────────────────────────────────────────────────────────────────
doc.add_paragraph()
add_heading(doc, '8.  Exploratory Data Analysis', 1, '1e293b')

add_heading(doc, '8.1  Attrition by Department', 2, '1e40af')
tbl5 = doc.add_table(rows=4, cols=4)
tbl5.style = 'Table Grid'
dept_data = [('Department','Total','Left','Attrition Rate'),
             ('Sales','446','92','20.63%'),
             ('Human Resources','63','12','19.05%'),
             ('Research & Development','961','133','13.84%')]
for i, row_data in enumerate(dept_data):
    r = tbl5.rows[i]
    for j, val in enumerate(row_data):
        r.cells[j].text = val
        for para in r.cells[j].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(r.cells[j], '1e40af')
        elif i % 2 == 0: set_cell_bg(r.cells[j], 'eff6ff')
doc.add_paragraph('Sales exceeds the company average (20.63%); R&D is below average (13.84%).').runs[0].font.size = Pt(10)

doc.add_paragraph()
add_heading(doc, '8.2  Attrition by Job Role', 2, '1e40af')
role_data_tbl = [('Job Role','Total','Left','Attrition Rate'),
                 ('Sales Representative','83','33','39.76%'),
                 ('Laboratory Technician','259','62','23.94%'),
                 ('Human Resources','52','12','23.08%'),
                 ('Sales Executive','326','57','17.48%'),
                 ('Research Scientist','292','47','16.10%'),
                 ('Manufacturing Director','145','10','6.90%'),
                 ('Healthcare Representative','131','9','6.87%'),
                 ('Manager','102','5','4.90%'),
                 ('Research Director','80','2','2.50%')]
tbl6 = doc.add_table(rows=len(role_data_tbl), cols=4)
tbl6.style = 'Table Grid'
for i, row_data in enumerate(role_data_tbl):
    r = tbl6.rows[i]
    for j, val in enumerate(row_data):
        r.cells[j].text = val
        for para in r.cells[j].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(r.cells[j], '1e40af')
        elif i % 2 == 0: set_cell_bg(r.cells[j], 'eff6ff')

doc.add_paragraph()
add_heading(doc, '8.3  Other Key Attrition Dimensions', 2, '1e40af')
other_data = [('Dimension','Category','Attrition Rate'),
              ('Overtime','Yes','30.53%'),
              ('Overtime','No','10.44%'),
              ('Age Group','18-25','34.78%'),
              ('Age Group','26-35','19.14%'),
              ('Age Group','36-45','9.19%'),
              ('Business Travel','Travel_Frequently','24.91%'),
              ('Business Travel','Travel_Rarely','14.96%'),
              ('Business Travel','Non-Travel','8.00%'),
              ('Marital Status','Single','25.53%'),
              ('Marital Status','Married','12.48%'),
              ('Marital Status','Divorced','10.09%'),
              ('Job Level','Level 1 (Entry)','26.34%'),
              ('Job Level','Level 5 (Senior)','7.25%'),
              ('Work-Life Balance','Level 1 (Bad)','31.25%'),
              ('Work-Life Balance','Level 3 (Good)','14.22%'),
              ('Job Satisfaction','Level 1 (Low)','22.84%'),
              ('Job Satisfaction','Level 4 (High)','11.33%')]
tbl7 = doc.add_table(rows=len(other_data), cols=3)
tbl7.style = 'Table Grid'
for i, row_data in enumerate(other_data):
    r = tbl7.rows[i]
    for j, val in enumerate(row_data):
        r.cells[j].text = val
        for para in r.cells[j].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(r.cells[j], '1e40af')
        elif i % 2 == 0: set_cell_bg(r.cells[j], 'eff6ff')

doc.add_paragraph()
add_heading(doc, '8.4  Employee Profile Comparison: Stayed vs Left', 2, '1e40af')
profile_data = [('Attribute','Stayed','Left'),
                ('Average Age','37.56 years','33.61 years'),
                ('Average Monthly Income','$6,832.74','$4,787.09'),
                ('Average Job Satisfaction','2.77 / 4','2.47 / 4'),
                ('Average Work-Life Balance','2.78 / 4','2.66 / 4'),
                ('Average Years at Company','7.37 years','5.13 years'),
                ('Average Total Working Years','11.86 years','8.24 years'),
                ('Average Job Level','2.15','1.64')]
tbl8 = doc.add_table(rows=len(profile_data), cols=3)
tbl8.style = 'Table Grid'
for i, row_data in enumerate(profile_data):
    r = tbl8.rows[i]
    for j, val in enumerate(row_data):
        r.cells[j].text = val
        for para in r.cells[j].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
                if i == 0: run.font.bold = True; run.font.color.rgb = RGBColor(255,255,255)
        if i == 0: set_cell_bg(r.cells[j], '1e40af')
        elif i % 2 == 1 and i > 0: set_cell_bg(r.cells[j], 'eff6ff')

# ── SECTION 9 — KEY FINDINGS ──────────────────────────────────────────────────
doc.add_page_break()
add_heading(doc, '9.  Key Findings', 1, '1e293b')
doc.add_paragraph('All findings below are derived from actual dataset calculations.')

insights = [
    ('01', 'Overtime is the Strongest Attrition Predictor',
     'Employees working overtime leave at 30.53% vs 10.44% for non-overtime workers — '
     'nearly 3× higher. With 28.3% of the workforce (416 employees) doing overtime, '
     'this segment represents a critical retention risk.'),
    ('02', 'Sales Representatives Are the Highest-Risk Role',
     'Sales Representatives have a 39.76% attrition rate — the highest of any role — '
     'while also earning the lowest average salary at $2,626/month. The combination of '
     'high performance pressure and low base pay is likely driving rapid turnover.'),
    ('03', 'Early-Career Employees Leave Most Frequently',
     'The 18–25 age group shows 34.78% attrition; Job Level 1 employees show 26.34%. '
     'The 0–2 year tenure band is the highest-risk period. Onboarding quality, early '
     'engagement, and competitive entry-level pay are critical retention levers.'),
    ('04', 'Frequent Business Travel Triples Attrition Risk',
     'Frequent travelers leave at 24.91% vs 8.00% for non-travelers — a 3× difference. '
     'Travel burden clearly degrades quality of life and contributes to departure.'),
    ('05', 'Work-Life Balance Level 1 Has Alarm-Level Attrition',
     'Employees with the worst work-life balance (Level 1) leave at 31.25%, more than '
     'double the rate at Level 3 (14.22%). Poor WLB is one of the strongest attrition drivers.'),
    ('06', 'There Is a $2,046/Month Compensation Gap Between Leavers and Stayers',
     'Employees who left earned $4,787/month on average vs $6,833/month for those who stayed — '
     'a 30% difference. This is the most consistent gap across the entire dataset.'),
    ('07', 'Single Employees Are More Likely to Leave',
     'Single employees have a 25.53% attrition rate vs 12.48% (married) and 10.09% (divorced). '
     'Fewer financial obligations and greater mobility may contribute.'),
    ('08', 'Tenure Is Strongly Protective',
     'Attrition decreases consistently as years at the company increases. The first 2 years '
     'are the highest-risk period, emphasising the importance of early engagement programs.'),
    ('09', 'Job Satisfaction Inversely Correlates with Attrition',
     'Level 1 satisfaction: 22.84% attrition. Level 4 satisfaction: 11.33% attrition. '
     'Improving satisfaction scores has a measurable impact on retention.'),
    ('10', 'Senior Roles Are Well Retained',
     'Manager (4.90%), Research Director (2.50%), and Manufacturing Director (6.90%) '
     'show very low attrition. Career progression to senior levels is a powerful retention mechanism.'),
]
for num, title, body in insights:
    add_insight_box(doc, num, title, body)

# ── SECTION 10 — RECOMMENDATIONS ─────────────────────────────────────────────
doc.add_page_break()
add_heading(doc, '10.  Business Recommendations', 1, '1e293b')
doc.add_paragraph(
    'The following recommendations are directly grounded in the data findings above. '
    'Each recommendation cites the specific metric that supports it.'
)

recs = [
    ('R1', 'Implement Overtime Policies and Monitoring',
     'Based on: Overtime attrition 30.53% vs 10.44%.',
     'Monitor overtime hours per employee and introduce mandatory limits or compensation '
     'adjustments. Flag employees consistently working long hours for engagement check-ins. '
     'Redistribute workloads or add headcount in roles where overtime is systemic.'),
    ('R2', 'Prioritize Retention in Sales',
     'Based on: Sales Representative attrition 39.76%; avg income $2,626/month.',
     'Review the compensation structure for Sales Representatives. Introduce performance '
     'bonuses, clear career ladders, mentorship programs, and manageable travel requirements.'),
    ('R3', 'Strengthen Early-Career Onboarding',
     'Based on: 18-25 age group attrition 34.78%; Job Level 1 attrition 26.34%.',
     'Introduce structured 90-day and 12-month onboarding with assigned mentors. Provide '
     'clear 12–24 month career roadmaps and competitive entry-level compensation.'),
    ('R4', 'Redesign Business Travel Policy',
     'Based on: Frequent travelers 24.91% vs non-travelers 8.00%.',
     'Evaluate whether all frequent travel is necessary. Explore virtual alternatives. '
     'Where travel is mandatory, improve allowances, provide recovery time, and offer '
     'flexible scheduling to reduce the quality-of-life burden.'),
    ('R5', 'Formalize Work-Life Balance Initiatives',
     'Based on: Work-Life Balance Level 1 attrition 31.25%.',
     'Launch formal WLB programs: flexible hours, remote work where feasible, wellness '
     'initiatives. Run regular pulse surveys to identify early-stage burnout.'),
    ('R6', 'Conduct Compensation Benchmarking',
     'Based on: Leavers earned $4,787/month vs stayers $6,833/month (30% gap).',
     'Benchmark salaries for entry and mid-level roles against the market. Offer '
     'transparent salary progression milestones and stock option plans.'),
    ('R7', 'Improve Job Satisfaction Programs',
     'Based on: Job satisfaction Level 1 attrition 22.84% vs Level 4 attrition 11.33%.',
     'Run quarterly satisfaction surveys and take visible, measurable action on feedback. '
     'Recognize achievements and connect employee work to organizational goals.'),
    ('R8', 'Create Clear Career Progression Pathways',
     'Based on: Job Level 1 attrition 26.34%; Job Levels 4–5 attrition < 7.25%.',
     'Implement Individual Development Plans (IDPs), promote internally first, and '
     'communicate promotion criteria transparently to all employees.'),
]
for code, title, basis, body in recs:
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(8)
    r_code = p_title.add_run(f'[{code}]  ')
    r_code.font.bold = True; r_code.font.color.rgb = RGBColor(37, 99, 235); r_code.font.size = Pt(11)
    r_title = p_title.add_run(title)
    r_title.font.bold = True; r_title.font.size = Pt(11)
    p_basis = doc.add_paragraph(basis)
    p_basis.paragraph_format.left_indent = Cm(0.5)
    p_basis.runs[0].font.size = Pt(9); p_basis.runs[0].font.italic = True
    p_basis.runs[0].font.color.rgb = RGBColor(100, 116, 139)
    p_body = doc.add_paragraph(body)
    p_body.paragraph_format.left_indent = Cm(0.5)
    p_body.paragraph_format.space_after = Pt(6)
    p_body.runs[0].font.size = Pt(10)

# ── SECTION 11 — CONCLUSION ───────────────────────────────────────────────────
doc.add_page_break()
add_heading(doc, '11.  Conclusion', 1, '1e293b')
doc.add_paragraph(
    'This project conducted a comprehensive data analytics study on employee attrition using '
    'the IBM HR Analytics dataset. The full analytics lifecycle was applied to 1,470 employee '
    'records, following a structured workflow from data loading through cleaning, feature '
    'engineering, EDA, visualization, correlation analysis, and business recommendations.'
)
doc.add_paragraph(
    'Key conclusions:'
)
conclusions = [
    'The overall attrition rate is 16.12% — 237 of 1,470 employees left.',
    'Overtime work is the strongest single driver: 30.53% attrition for overtime workers vs 10.44%.',
    'Sales Representatives face the highest role-specific attrition (39.76%) with the lowest pay ($2,626/month).',
    'Young employees (18–25: 34.78%) and entry-level employees (Level 1: 26.34%) are the most vulnerable segments.',
    'Business travel frequency, poor work-life balance, and low job satisfaction all correlate strongly with higher attrition.',
    'A consistent $2,046/month compensation gap exists between employees who leave and those who stay.',
]
for c in conclusions:
    p = doc.add_paragraph(c, style='List Bullet')
    p.runs[0].font.size = Pt(11)
doc.add_paragraph(
    '\nData analytics transformed this HR challenge from a general concern into specific, '
    'quantified, actionable insights. HR management now has a concrete, evidence-based '
    'roadmap — eight targeted recommendations addressing overtime, compensation, onboarding, '
    'travel policy, work-life balance, and career development — to measurably reduce the '
    '16.12% attrition rate and build a more engaged, stable workforce.'
)

# ── SECTION 12 — LIMITATIONS ─────────────────────────────────────────────────
add_heading(doc, '12.  Limitations', 1, '1e293b')
for lim in [
    'The dataset is a static snapshot and does not capture attrition trends over time.',
    'Findings apply to a single organization and may not generalize to other industries.',
    'Correlation does not imply causation — identified relationships do not prove direct causality.',
    'The dataset lacks qualitative data (e.g., exit interview reasons, manager quality).',
    'Self-reported satisfaction scores are subjective and may carry response bias.',
]:
    p = doc.add_paragraph(lim, style='List Bullet')
    p.runs[0].font.size = Pt(11)

# ── SECTION 13 — FUTURE SCOPE ─────────────────────────────────────────────────
add_heading(doc, '13.  Future Scope', 1, '1e293b')
for fs in [
    'Develop predictive attrition models (Logistic Regression, Random Forest, XGBoost) to identify high-risk employees proactively.',
    'Build a live HR analytics dashboard (Power BI, Tableau, or Streamlit) for real-time monitoring.',
    'Apply clustering (K-Means) to segment employees by attrition risk profile for targeted interventions.',
    'Conduct time-series analysis to identify seasonal and trend patterns in attrition rates.',
    'Apply NLP to exit interview text data to extract qualitative departure reasons.',
]:
    p = doc.add_paragraph(fs, style='List Bullet')
    p.runs[0].font.size = Pt(11)

# ── SECTION 14 — REFERENCES ───────────────────────────────────────────────────
add_heading(doc, '14.  References', 1, '1e293b')
refs = [
    'IBM HR Analytics Employee Attrition & Performance Dataset. Kaggle. https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset',
    'Pandas Documentation. https://pandas.pydata.org/docs/',
    'Matplotlib Documentation. https://matplotlib.org/stable/contents.html',
    'Seaborn Documentation. https://seaborn.pydata.org/',
    'NumPy Documentation. https://numpy.org/doc/',
    'IBM SkillsBuild Data Analytics with AI Academic Internship Program. BharatCares in association with AICTE.',
]
for i, ref in enumerate(refs, 1):
    p = doc.add_paragraph(f'{i}. {ref}')
    p.runs[0].font.size = Pt(10)
    p.paragraph_format.space_after = Pt(4)

# ── Save ──────────────────────────────────────────────────────────────────────
out = os.path.join(BASE, 'AnishKumar_ProjectReport.docx')
doc.save(out)
print(f'Report saved: {out}')
print(f'Pages (approx): {len(doc.paragraphs) // 30 + 1}')
